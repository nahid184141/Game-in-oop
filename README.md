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
- Encapsulation is an OOP principle that bundles the data (attributes) and methods (operations) that manipulate the data into a single unit or class. It also restricts direct access to some of an object's components, which is a way of preventing accidental interference and misuse of the methods and data.
#### Example
```python
  class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, SNAKE_SIZE)
        self.body = [(x, y)]
        self.dx, self.dy = SNAKE_SIZE, 0
    def change_direction(self, dx, dy):
        self.dx, self.dy = dx, dy
```
- Here, Snake class, encapsulation is evident as it combines properties like body, dx, and dy, and methods like draw, update, and change_direction within a single class. Access to these properties is controlled through methods like change_direction, which manages how the snake's direction can be altered.
##### In this code have five class those are enncapsulated.
### Inheritance:
- Inheritance is a mechanism where a new class derives attributes and methods from an existing class. The new class is called a derived class or subclass, and the existing class is called a base class or superclass.
 #### Example
```python
class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, SNAKE_SIZE)
       

class Food(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, FOOD_SIZE)

```
- In this code  Snake and Food class are inherit from parent class Gameobject.

### Polymorphism:
- Polymorphism allows methods to be defined in a superclass and that have been overridden in a subclass to have different behaviors based on the object on which they are called.
 #### Example
```python
  class Snake(GameObject):
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, (0, 255, 0), (segment[0], segment[1], self.size, self.size))

 class Food(GameObject):
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))
```
- Here, draw and update methods of the GameObject class are abstract and are implemented differently in the Snake and Food subclasses. This showcases polymorphism where the same method name (draw, update) behaves differently depending on whether it's called on a Snake object or a Food object. 

### Abstract methods:
- Abstract methods are methods that are declared in an abstract class and must be implemented by all subclasses of this abstract class. An abstract class cannot be instantiated and is used to define a common interface for its subclasses.
 #### Example
 ```python
  from abc import ABC, abstractmethod

   class GameObject(ABC):
        @abstractmethod
     def draw(self, surface):
          pass

         @abstractmethod
     def update(self):
          pass```
- GameObject class defines draw and update as abstract methods, making GameObject an abstract class that cannot be instantiated. All classes that inherit from GameObject must provide an implementation for these methods.

### singleton pattern:

### Factory pattern:
