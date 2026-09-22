import cv2
import numpy as np
import torch
from torchvision import transforms
from torchvision.models.segmentation import deeplabv3_resnet101
from PIL import Image


def apply_ghibli_effect(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image)

    # Define transformations
    transform = transforms.Compose(
        [
            transforms.Resize((512, 512)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    image_tensor = transform(image_pil).unsqueeze(0)

    # Load DeepLabV3 model for segmentation
    model = deeplabv3_resnet101(pretrained=True).eval()
    with torch.no_grad():
        output = model(image_tensor)["out"][0]
    mask = output.argmax(0).byte().cpu().numpy()

    # Smooth edges of segmentation mask
    mask = cv2.medianBlur(mask, 5)
    mask = cv2.resize(
        mask, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST
    )

    # Apply soft color grading
    image_smooth = cv2.bilateralFilter(image, 9, 75, 75)
    ghibli_tone = np.clip(image_smooth * np.array([1.2, 1.1, 0.9]), 0, 255).astype(
        np.uint8
    )

    # Apply cartoon effect
    gray = cv2.cvtColor(ghibli_tone, cv2.COLOR_RGB2GRAY)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )
    color = cv2.bilateralFilter(ghibli_tone, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Blend with original to soften effect
    final = cv2.addWeighted(cartoon, 0.7, ghibli_tone, 0.3, 0)

    # Save output
    final_image = Image.fromarray(final)
    final_image.save(output_path)


# Example usage
apply_ghibli_effect("input.jpg", "output_ghibli.jpg")
