import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game objects
paddle_width, paddle_height = 10, 100
ball_radius = 7

# Player paddles
paddle1 = pygame.Rect(10, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
paddle2 = pygame.Rect(WIDTH - 20, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)

# Ball
ball = pygame.Rect(WIDTH//2, HEIGHT//2, ball_radius*2, ball_radius*2)
ball_dx, ball_dy = 7, 7

# Scores
score1, score2 = 0, 0
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()

def reset_ball():
    global ball_dx, ball_dy
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_dx *= -1
    ball_dy = 7

while True:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= 8
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += 8
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= 8
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += 8

    # Move ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Collision with top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx *= -1

    # Scoring
    if ball.left <= 0:
        score2 += 1
        reset_ball()
    elif ball.right >= WIDTH:
        score1 += 1
        reset_ball()

    # Draw everything
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Draw scores
    score_text = font.render(f"{score1}   {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

    # Update display
    pygame.display.flip()
    clock.tick(60)
