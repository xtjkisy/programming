import pygame
import random
import sys
from typing import List

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

GAME_DURATION = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Balloon Popping Game')

balloon_image = pygame.image.load('balloon.png')
BALLOON_SIZE = 50
balloon_image = pygame.transform.scale(balloon_image, (BALLOON_SIZE, BALLOON_SIZE))

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

class Balloon(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.image = balloon_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

def main() -> None:
    balloons = pygame.sprite.Group()
    score = 0
    start_ticks = pygame.time.get_ticks()

    running = True
    while running:
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
                for balloon in balloons:
                    if balloon.rect.collidepoint(mouse_pos):
                        balloon.kill()
                        score += 1

        if random.random() < 0.02:
            x = random.randint(0, SCREEN_WIDTH - BALLOON_SIZE)
            y = random.randint(0, SCREEN_HEIGHT - BALLOON_SIZE)
            balloons.add(Balloon(x, y))

        screen.fill(WHITE)

        balloons.draw(screen)

        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        time_text = font.render(f"Time: {remaining_time}", True, BLACK)
        screen.blit(time_text, (SCREEN_WIDTH - 150, 10))

        pygame.display.flip()

        clock.tick(60)

    screen.fill(WHITE)
    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
