import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init() # Initialize pygame before using any of its features

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Main game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(("black"))
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Cap the frame rate at 60 FPS and store delta time in seconds

if __name__ == "__main__":
    main()
