import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
HEART_SIZE = 100

# Colors
BACKGROUND_COLOR = (30, 30, 30)  # Dark background
HEART_COLOR = (255, 102, 153)  # Heart color
SPARKLE_COLOR = (255, 255, 255)  # Sparkle color

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beating Heart with Sparkles")

# Function to draw heart
def draw_heart(x, y, size):
    points = []
    for angle in range(360):
        rad = math.radians(angle)
        # Heart shape formula using parametric equations
        x_offset = size * 16 * math.sin(rad) ** 3
        y_offset = -size * (13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad))
        points.append((x + x_offset, y + y_offset))

    pygame.draw.polygon(screen, HEART_COLOR, points)

# Main loop
running = True
clock = pygame.time.Clock()
heart_scale = 1.0
scaling_up = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update heart size for heartbeat effect
    if scaling_up:
        heart_scale += 0.02
        if heart_scale >= 1.1:
            scaling_up = False
    else:
        heart_scale -= 0.02
        if heart_scale <= 1.0:
            scaling_up = True

    # Draw the heart
    draw_heart(WIDTH // 2, HEIGHT // 2, HEART_SIZE * heart_scale)

    # Draw sparkles
    for _ in range(10):  # Increase the number of sparkles
        sparkle_x = random.randint(0, WIDTH)
        sparkle_y = random.randint(0, HEIGHT)
        pygame.draw.circle(screen, SPARKLE_COLOR, (sparkle_x, sparkle_y), random.randint(2, 6))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
