import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Balloon settings
BALLOON_SIZE = 50
BALLOON_SPAWN_TIME = 1000  # milliseconds

# Game settings
GAME_DURATION = 30  # seconds

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Balloon Popping Game')

# Load balloon image
balloon_image = pygame.Surface((BALLOON_SIZE, BALLOON_SIZE))
pygame.draw.circle(balloon_image, RED, (BALLOON_SIZE // 2, BALLOON_SIZE // 2), BALLOON_SIZE // 2)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Font for displaying the score and time
font = pygame.font.Font(None, 36)

def main():
    # Game variables
    balloons = []
    score = 0
    start_ticks = pygame.time.get_ticks()

    # Balloon event
    BALLOON_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(BALLOON_EVENT, BALLOON_SPAWN_TIME)

    running = True
    while running:
        # Calculate remaining time
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        remaining_time = max(0, GAME_DURATION - int(seconds))
        
        if remaining_time == 0:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for balloon in balloons[:]:
                    if balloon.collidepoint(mouse_pos):
                        balloons.remove(balloon)
                        score += 1
            elif event.type == BALLOON_EVENT:
                x = random.randint(0, SCREEN_WIDTH - BALLOON_SIZE)
                y = random.randint(0, SCREEN_HEIGHT - BALLOON_SIZE)
                balloons.append(pygame.Rect(x, y, BALLOON_SIZE, BALLOON_SIZE))

        # Clear the screen
        screen.fill(WHITE)

        # Draw balloons
        for balloon in balloons:
            screen.blit(balloon_image, balloon.topleft)

        # Draw the score and time
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        time_text = font.render(f"Time: {remaining_time}", True, BLACK)
        screen.blit(time_text, (SCREEN_WIDTH - 150, 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    # Display the final score
    screen.fill(WHITE)
    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    # Wait for a few seconds before closing the game
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
