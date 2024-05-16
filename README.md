# snake Game-in-oop
<br>
Author:Md Nahid Hasan Rabbi

This is my first github project.
## Introduction
### Application:
The Snake Game is a classic game implemented in Python using the Pygame library.The player controls a snake, moving it around the screen to eat food while avoiding hitting its own tail.The game increases in difficulty as the snake grows longer with each piece of food eaten.
### Run program:
- Ensure Python and Pygame are installed on your system.
- Download the `snakegame.py` file to your local machine.
- Open a terminal or command prompt.<br>
- Navigate to the directory containing the downloaded file.
- Run the command: `snakegame.py`.
### Use of program
- Use the arrow keys (Up, Down, Left, Right) to control the direction of the snake.
- The game continues until the snake collides with itself.
- Press 'R' to restart the game after a game over.
- Press 'Esc' to exit the game.

# Analysis
***The Snake game is structured using Object-Oriented Programming (OOP) principles and includes the use of the Singleton and Factory design patterns.***
### Encapsulation:
-Encapsulation is an OOP principle that bundles the data (attributes) and methods (operations) that manipulate the data into a single unit or class. It also restricts direct access to some of an object's components, which is a way of preventing accidental interference and misuse of the methods and data.
#### Example
```python
  class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, SNAKE_SIZE)
        self.body = [(x, y)]
        self.dx, self.dy = SNAKE_SIZE, 0
```
-Here, Snake class, encapsulation is evident as it combines properties like body, dx, and dy, and methods like draw, update, and change_direction within a single class. Access to these properties is controlled through methods like change_direction, which manages how the snake's direction can be altered.
##### In this code have five class those are enncapsulated.
