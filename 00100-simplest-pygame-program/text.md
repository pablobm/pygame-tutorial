# The simplest possible Pygame program

First we need to "import" the Pygame "library" into our program. A "library" is a bunch of code that somebody else wrote and we can use in our programs. By "importing", we mean reading a library from the hard disk and loading it in memory so that our program can use it. In Python, this is done with `import`, like this:

```python
import pygame
```

The next step is to tell pygame to get started, as this doesn't happen until we say so. For this, we use the `init` function inside `pygame`:

```python
pygame.init()
```

Finally, we create a window where we can display our game. When we do this, we have to specify what size of window we have. A typical window size is 800 pixels wide and 600 pixels high. We would do it like this:

```python
pygame.display.set_mode([800, 600])
```

The complete program looks like this:

```python
import pygame
pygame.init()
pygame.display.set_mode([800, 600])
```

## Questions

1. Explain with your own words what this program does at each step
2. How would you make the window be 640 pixels wide and 480 pixels high?