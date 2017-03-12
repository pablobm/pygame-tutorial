# Drawing something on the screen

Let's draw something on the screen, as well as keep the screen open for a few seconds so that we can see what's on it.

## Waiting

To make Python wait a bit, we need to load a library that gives us that ability. This one is called `time`, and includes code to help us deal with time. For example, to make the program wait for a time. We can import it like this:

```python
import time
```

Inside the `time` library, there's a function called `sleep`. This function makes the program stop for a number of seconds. For example, to stop the program for 5 seconds, you would do this:

```python
time.sleep(5)
```

## Challenge

1. Where do you think the `import` and the `sleep` lines go in the program? Try to add them so that the window is open for 5 seconds.
2. How would you get the window to stay open for 10 seconds instead?

## Getting hold of the screen

It's time to draw an image on the screen. Find one you would like to draw, and put the file in the same folder as the code.

First we need to get hold of the screen. When we create a a screen (a window) with `set_mode`, the function "returns" a screen. This means we can create a variable and store the screen there. Modify the code to do this:

```python
screen = pygame.display.set_mode([800, 600])
```

The function `set_mode` (which lives inside `display`, which in turn lives inside `pygame`) returns a result. We use the `=` symbol to give a name to this result. We call it `screen`, but we could have given it any other name. The important thing is that we give it a name so that we can refer to it later.

## Loading the image

Next, we have to load the image and give it a name too. This is the line for that:

```python
image = pygame.image.load("my-image.png")
```

In this example, I assume that `my-image.png` is the name of the image file. Your file will have a different name, so change the code to reflect that.

Again, the `load` function gives us a result, and we use the `=` symbol to give this result a name: `image`. We could have called it anything else.

Now we draw the image on the screen. To do this, we use the function `blit`:

```python
screen.blit(image, [0, 0])
```

Notice that `blit` lives inside `screen`. "Blit" is a technical term, don't worry too much about the funny word. What it means here is "draw the image on the screen".

## Actually displaying the result

There's one last hitch. Pygame doesn't show things on screen as you draw them. Instead it waits until you tell it to do it. This can be a bit annoying at first, but it is much faster because it allows the computer to do less work.

Once you have drawn the image on the screen, you tell pygame that the screen is ready by running this code:

```python
pygame.display.flip()
```

## Challenges

* Where do you think you have to add the lines above on the program? Try adding them yourself and see where they would go.
* Make the image appear in the centre of the screen