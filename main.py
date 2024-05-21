import tkinter as tk
import random

WIDTH = 800
HEIGHT = 600
SPEED = 8
GRAVITY = 1.5
JUMP_SPEED = 15
PIPE_WIDTH = 100
PIPE_GAP = 200
PIPE_SPACING = 300

class Bird:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = tk.PhotoImage(file="bird.png")  # Load the image
        self.id = canvas.create_image(100, HEIGHT / 5, image=self.image)  # Display the image
        self.velocity = 0

    def update(self):
        self.canvas.move(self.id, 0, self.velocity)
        self.velocity += GRAVITY

    def jump(self, event):
        self.velocity = -JUMP_SPEED

    def get_position(self):
            position = self.canvas.bbox(self.id)
            if position is not None:
                x1, y1, x2, y2 = position
                padding = 30  # Adjust this value to shrink the collision box
                return (x1 + padding, y1 + padding, x2 - padding, y2 - padding)
            return None
        
    def collides_with(self, pipe):
        bird_position = self.get_position()
        pipe_positions = pipe.get_positions()

        for pipe_position in pipe_positions:
            if bird_position is not None and pipe_position is not None:
                if (bird_position[2] > pipe_position[0] and bird_position[0] < pipe_position[2] and
                    bird_position[3] > pipe_position[1] and bird_position[1] < pipe_position[3]):
                    return True

        return False
    

class Pipe:
    def __init__(self, canvas, x):
        self.canvas = canvas
        self.x = x
        self.top_height = random.randint(100, HEIGHT - 100 - PIPE_GAP)
        self.bottom_height = HEIGHT - self.top_height - PIPE_GAP
        self.top_id = canvas.create_rectangle(self.x, 0, self.x + PIPE_WIDTH, self.top_height, fill='green')
        self.bottom_id = canvas.create_rectangle(self.x, HEIGHT - self.bottom_height, self.x + PIPE_WIDTH, HEIGHT, fill='green')

    def update(self):
        self.canvas.move(self.top_id, -SPEED, 0)
        self.canvas.move(self.bottom_id, -SPEED, 0)
        self.x -= SPEED

    def get_positions(self):
        return [self.canvas.bbox(self.top_id), self.canvas.bbox(self.bottom_id)]

class gameUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Flappy Bird")
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg="#ADD8E6")
        self.canvas.pack()
        self.root.update()

        self.bird = Bird(self.canvas)
        self.pipes = [Pipe(self.canvas, i * PIPE_SPACING + WIDTH) for i in range(3)]
        self.score = 0
        self.score_display = self.canvas.create_text(100, 50, text="Score: 0", font=("Helvetica", 16), fill="black")
        self.high_score = 0  # Add a variable to keep track of the high score
        self.high_score_display = self.canvas.create_text(100, 80, text="High Score: 0", font=("Helvetica bold", 16), fill="black")

        self.root.bind("<space>", self.space_key_pressed)  # Bind the space key to space_key_pressed

        self.game_is_over = False  # New boolean flag to indicate whether the game is over

        self.run()
        
    def space_key_pressed(self, event):
        if self.game_is_over:
            self.restart_game(event)
        else:
            self.bird.jump(event)

    def run(self):
        self.update_game()
        self.root.mainloop()

    def game_over(self):
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text="GAME OVER", font=("Helvetica", 50, "bold"), fill="red")
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2 + 50, text="Press SPACE to restart", font=("Helvetica", 15), fill="black")
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2 + 80, text="Your score: " + str(self.score), font=("Helvetica", 20), fill="black")
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2 + 110, text="Mehmet Kahya - 230603035", font=("Helvetica", 15), fill="black")
        self.game_is_over = True
        if self.score > self.high_score:  # If the current score is higher than the high score
            self.high_score = self.score  # Update the high score
            self.canvas.itemconfig(self.high_score_display, text=f"High Score: {self.high_score}")  # Update the high score display

    def restart_game(self, event):
        if self.game_is_over:
            # Delete all canvas items
            self.canvas.delete("all")

            # Reset game state
            self.bird = Bird(self.canvas)
            self.pipes = [Pipe(self.canvas, i * PIPE_SPACING + WIDTH) for i in range(3)]
            self.score = 0
            self.game_is_over = False

            # Recreate the score display and high score display
            self.score_display = self.canvas.create_text(100, 50, text="Score: 0", font=("Helvetica", 16), fill="black")
            self.high_score_display = self.canvas.create_text(100, 80, text=f"High Score: {self.high_score}", font=("Helvetica bold", 16), fill="black")

            # Start the game loop
            self.update_game()
            
    def update_game(self):
        self.bird.update()
        for pipe in self.pipes:
            pipe.update()
            if pipe.x + PIPE_WIDTH < 0:
                self.canvas.delete(pipe.top_id)
                self.canvas.delete(pipe.bottom_id)
                self.pipes.remove(pipe)
                self.pipes.append(Pipe(self.canvas, self.pipes[-1].x + PIPE_SPACING))
                self.score += 1  # Increment the score when the bird passes a pipe
                self.canvas.itemconfig(self.score_display, text=f"Score: {self.score}")  # Update the score display
            if self.bird.collides_with(pipe):
                self.game_over()  # Display game over screen
                return  # End the game
        self.root.after(20, self.update_game)  # Schedule the next update


if __name__ == "__main__":
    game = gameUI()  # Create the gameUI object without passing any arguments      