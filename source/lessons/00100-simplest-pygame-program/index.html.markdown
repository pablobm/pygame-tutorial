---
title: The simplest possible Pygame program
---

Let's put in practice what we learned. We are going to use the Pygame library. Pygame has functions to deal with graphics, sounds, keyboard, etc. It allows us to build games using Python.

First we need to import Pygame library into our program. As we have seen before, we do it like this:

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

This is the complete program:

```python
import pygame
pygame.init()
pygame.display.set_mode([800, 600])
```

## Questions

1. Type the program and run it. What does it do?
1. Explain in your own words what this program does at each step
1. How would you make the window be 640 pixels wide and 480 pixels high?
