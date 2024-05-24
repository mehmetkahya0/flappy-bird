# Flappy Bird Game

This project is a simple implementation of the classic Flappy Bird game using Python's Tkinter library for the graphical interface. The game involves a bird controlled by the player that must navigate through gaps in moving pipes without colliding with them or the ground.

## Features

- User-friendly graphical interface built with Tkinter
- Bird character that can jump when the space key is pressed
- Randomly generated pipes with gaps for the bird to pass through
- Collision detection for pipes and ground
- Scoring system to keep track of the player's score
- High score tracking
- Game over screen with the option to restart by pressing the space key

## Installation

To run this project, you need to have Python installed on your machine. Additionally, you need to have Tkinter installed, which is usually included with Python by default. If it's not installed, you can install it using your package manager.

## Usage

1. Clone the repository and navigate to the project directory:

    ```sh
    git clone https://github.com/username/flappy-bird.git
    cd flappy-bird
    ```

2. Ensure you have an image file named `bird.png` in the `img` folder.

3. Run the script:

    ```sh
    python flappy_bird.py
    ```

## Code Overview

### Constants

- `WIDTH` and `HEIGHT`: Dimensions of the game window.
- `SPEED`: Speed at which the pipes move.
- `GRAVITY`: Gravity affecting the bird's fall.
- `JUMP_SPEED`: Speed at which the bird jumps.
- `PIPE_WIDTH`: Width of the pipes.
- `PIPE_GAP`: Gap between the top and bottom pipes.
- `PIPE_SPACING`: Distance between consecutive pipes.

### `Bird` Class

- **`__init__`**: Initializes the bird with an image and sets the initial velocity.
- **`update`**: Updates the bird's position based on its velocity and gravity.
- **`jump`**: Makes the bird jump when the space key is pressed.
- **`get_position`**: Returns the bird's position with padding to adjust the collision box.
- **`collides_with`**: Checks if the bird collides with a pipe.
- **`check_collision_with_ground`**: Checks if the bird collides with the ground.

### `Pipe` Class

- **`__init__`**: Initializes the pipes with random heights and positions.
- **`update`**: Updates the pipes' positions as they move across the screen.
- **`get_positions`**: Returns the positions of the top and bottom pipes.

### `gameUI` Class

- **`__init__`**: Sets up the game window, canvas, bird, pipes, score, and binds the space key.
- **`space_key_pressed`**: Handles the space key press to make the bird jump or restart the game.
- **`run`**: Starts the game loop.
- **`game_over`**: Displays the game over screen and updates the high score if necessary.
- **`restart_game`**: Restarts the game by resetting the game state and canvas items.
- **`update_game`**: Updates the game state, including bird and pipe positions, and checks for collisions.

## Example

After running the script, a window will appear where you control a bird by pressing the space key to jump. Avoid hitting the pipes and the ground. Your score increases each time you pass through a set of pipes. When the game is over, press the space key to restart.

## Author

Mehmet Kahya @mehmetkahya0

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
