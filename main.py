import pygame
from asteroid import Asteroid
from player import Player
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init() # Initialize pygame before using any of its features

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create the player at the center of the screen
    AsteroidField() # Create the asteroid field
    # Main game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(("black"))
        updatable.update(dt) # Update all sprites in the updatable group, passing the delta time
        for drawing in drawable: # Draw all sprites in the drawable group
            drawing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Cap the frame rate at 60 FPS and store delta time in seconds

if __name__ == "__main__":
    main()
