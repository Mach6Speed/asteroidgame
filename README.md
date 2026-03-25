# Asteroid Game (Pygame)

A small arcade shooter built with Python and Pygame.

This project is a classic Asteroids-style game where you pilot a triangular ship, dodge incoming rocks, and break larger asteroids into smaller ones before they collide with you.

## Features

- Rotating ship controls with forward/backward thrust.
- Projectile shooting with a cooldown system.
- Procedural asteroid spawning from all screen edges.
- Asteroid splitting logic (large rocks break into smaller pieces).
- Collision detection for player hits and shot impacts.
- Built-in JSONL logging for game state snapshots and gameplay events.

## Tech Stack

- Python 3.13+
- Pygame 2.6.1

## Getting Started

## Controls

- `W`: Move forward
- `S`: Move backward
- `A`: Rotate left
- `D`: Rotate right
- `Space`: Shoot
- Close window: Quit game

## Project Structure

- `main.py`: Game loop, sprite groups, collision handling, rendering.
- `player.py`: Ship movement, rotation, shooting, and rendering.
- `asteroid.py`: Asteroid behavior and split mechanics.
- `asteroidfield.py`: Asteroid spawn system and edge-based spawning.
- `shot.py`: Projectile behavior.
- `circleshape.py`: Base class for circular game entities and collisions.
- `constants.py`: Tuning values (screen size, speeds, cooldowns, sizes).
- `logger.py`: Writes runtime state and game events to JSONL files.

## Logging Output

When the game runs, it produces:

- `game_state.jsonl`: Periodic snapshots of object positions and state.
- `game_events.jsonl`: Event stream (for example, asteroid hits/splits or player death).

This makes it easy to debug gameplay behavior or inspect what happened during a run.

## Gameplay Notes

- The game ends immediately when the player collides with an asteroid.
- Shooting an asteroid destroys it.
- Asteroids above the minimum radius split into two smaller asteroids.


