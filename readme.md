# Pacman and Mushroom Game

## Overview

This is a simple Pacman game where the player controls Pacman to avoid or collect different types of mushrooms. The game features multiple levels with varying difficulty.

## Features

- **Multiple Levels**: Choose from different levels of difficulty (Easy, Medium, Hard).
- **Game Over Screen**: Displays a Game Over screen with a restart button.
- **Mushroom Interactions**: Different types of mushrooms affect the player's health differently.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/fshekofteh/pacman-mushroom-game.git
    cd pacman-mushroom-game
    ```

2. **Install dependencies**:
    ```sh
    pip install pygame
    ```

3. **Run the game**:
    ```sh
    python main.py
    ```

## How to Play

- **Movement**: Use the arrow keys to move Pacman.
- **Objective**: Avoid red mushrooms, collect blue mushrooms to gain health, and avoid pink mushrooms to prevent losing health.
- **Game Over**: The game ends when the timer runs out or Pacman's health reaches zero. Click the restart button to play again.

## Game Controls

- **Arrow Keys**: Move Pacman
- **Mouse**: Click on buttons in the menu and Game Over screen

## Levels

- **Easy**: Slower mushrooms, longer game duration.
- **Medium**: Moderate speed mushrooms, moderate game duration.
- **Hard**: Faster mushrooms, shorter game duration.

## Screenshots

![Menu Screen](screenshots/menu.png)
![Game Screen](screenshots/game.png)
![Game Over Screen](screenshots/game_over.png)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- Pygame library for game development.
- Sprites from [source of sprites].

Enjoy the game!