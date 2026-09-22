import cv2
import numpy as np
from PIL import Image, ImageFilter


def ghiblify_image(
    input_path,
    output_path,
    saturation_factor=1.4,
    brightness_factor=1.1,
    edge_preserve=True,
    cartoon_strength=3,
    blur_radius=1,
):
    """
    Apply a Studio Ghibli-inspired artistic style to an image.

    Parameters:
    - input_path: Path to the input image
    - output_path: Path to save the output image
    - saturation_factor: Increase color saturation (1.0 = no change)
    - brightness_factor: Adjust brightness (1.0 = no change)
    - edge_preserve: Whether to preserve edges
    - cartoon_strength: Strength of cartoon effect (1-5)
    - blur_radius: Radius for edge-preserving blur
    """

    # Read the image
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError("Image not found or unable to read")

    # Convert to PIL Image for some operations
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # 1. Soften the image with edge-preserving blur
    if edge_preserve:
        blurred = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    else:
        blurred = cv2.GaussianBlur(img, (5, 5), 0)

    # 2. Enhance colors (Ghibli style often has vibrant colors)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    hsv[..., 1] = np.clip(hsv[..., 1] * saturation_factor, 0, 255)
    hsv[..., 2] = np.clip(hsv[..., 2] * brightness_factor, 0, 255)
    color_enhanced = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # 3. Apply a slight painterly effect
    painterly = cv2.stylization(color_enhanced, sigma_s=60, sigma_r=0.45)

    # 4. Add a subtle glow effect (Ghibli-style lighting)
    glow = cv2.addWeighted(
        painterly, 0.7, cv2.GaussianBlur(painterly, (0, 0), 10), 0.3, 0
    )

    # 5. Optional cartoon effect
    if cartoon_strength > 0:
        gray = cv2.cvtColor(glow, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 7)
        edges = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,
            blockSize=9,
            C=2 + cartoon_strength,
        )
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        cartoon = cv2.bitwise_and(glow, edges)
        final = cv2.addWeighted(glow, 0.7, cartoon, 0.3, 0)
    else:
        final = glow

    # 6. Apply a slight vignette effect
    rows, cols = final.shape[:2]
    vignette = np.zeros((rows, cols, 3), dtype=np.float32)
    x = np.linspace(-1, 1, cols)
    y = np.linspace(-1, 1, rows)
    X, Y = np.meshgrid(x, y)
    radius = np.sqrt(X**2 + Y**2)
    radius = radius / np.max(radius)
    vignette = 1 - 0.6 * radius**2
    vignette = np.dstack([vignette] * 3)
    final = (final * vignette).astype(np.uint8)

    # Convert back to PIL and apply final touches
    final_pil = Image.fromarray(cv2.cvtColor(final, cv2.COLOR_BGR2RGB))

    # 7. Soften highlights
    final_pil = final_pil.filter(ImageFilter.GaussianBlur(radius=blur_radius))

    # Save the result
    final_pil.save(output_path)
    print(f"Ghibli-fied image saved to {output_path}")


# Example usage
if __name__ == "__main__":
    input_image = "input.jpg"  # Replace with your image path
    output_image = "ghibli_output.jpg"
    ghiblify_image(input_image, output_image)
