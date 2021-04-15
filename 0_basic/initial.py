# For starts, checking how well PyCharm is integrated with github's services.

import pygame

pygame.init()

# Create drawing window
screen = pygame.display.set_mode([500, 500])

# Waiting for user loop
running = True
while running:

    # Evaluate if the user clicked the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white color
    screen.fill((255, 255, 255))

    # Draw circle at the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the diplay
    pygame.display.flip()

# Quit the game
pygame.quit()
