# Arrays of objects
Once you've loaded your modules, and written your resource handling functions, you'll want to get on to writing some game objects. The way this is done is fairly simple, though it can seem complex at first. You write a class for each type of object in the game, and then create an instance of those classes for the objects. You can then use those classes' methods to manipulate the objects, giving objects some motion and interactive capabilities. So your game, in pseudo-code, will look like this:
## Simple ball class
Here is a simple class with the functions necessary for creating a ball object that will, if the update function is called in the main loop, move across the screen:

```python
#!/usr/bin/python

# [load modules here]

# [resource handling functions here]

class Ball:
    # [ball functions (methods) here]
    # [e.g. a function to calculate new position]
    # [and a function to check if it hits the side]

def main:
    # [initiate game environment here]

    # [create new object as instance of ball class]
    ball = Ball()

    while 1:
        # [check for user input]

        # [call ball's update function]
        ball.update()
```

Array version where we instantiate using a loop and update and drwaw in loops

```python
#!/usr/bin/python

# [load modules here]

# [resource handling functions here]

class Ball:
    # [ball functions (methods) here]
    # [e.g. a function to calculate new position]
    # [and a function to check if it hits the side]

def main:
    # [initiate game environment here]

    # [create new object as instance of ball class]
    balls = []
    
    for i in range(numballs):
        ball.append(Ball())
    
    while 1:
      for ball in balls:
          ball.update()
          ball.draw()
```


Here is a simple class with the functions necessary for creating a ball object that will, if the update function is called in the main loop, move across the screen:
```python
class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
```

