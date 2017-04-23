---
title: Drawing something on the screen
---

So far, our program is only showing a blank screen. Let's draw an image on it.

## Waiting

At the moment, the program opens an window and closes it immediately. We should make the window stay open for a bit first.

To make Python wait a bit before ending, we need to load a library that gives us that ability. The one we need now is called `time`, and includes code to help us deal with time. We can import it like this:

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

It's time to draw an image on the screen. Find an image you would like to draw, and put the file in the same folder as the code.

First we need to get hold of the screen. When we create a screen (a window) with `set_mode`, the function "returns" a screen. This means we can create a variable and store the screen there. **Modify** the existing code to do this when it creates the window:

```python
screen = pygame.display.set_mode([800, 600])
```

The function `set_mode` (which lives inside `display`, which in turn lives inside `pygame`) returns a result. We use the `=` symbol to give a name to this result. In this case, the result is an "object" that represents the screen. We call it `screen`, but we could have given it any other name. The important thing is that we give it a name that is easy to remember later.

## Loading the image

Next, we have to load the image and give it a name too. This is the line for that:

```python
image = pygame.image.load("my-image.png")
```

In this example, the image file is called `my-image.png`. It will be different for you. Make sure to type the name of the file you want to load.

What the line does is this:

1. It uses the function `pygame.image.load` to load an image into memory.
2. The function knows what image to read because we tell it the name of the file: "my-image.png". It will be different in your case.
3. The function "returns" an "object" that represents the image in the program.
4. We give a name to this "object" so that we can use it later. We call it `image`, using the equals `=` symbol. We could have called it anything else.

Now we draw the image on the screen. To do this, we use the function `blit`, which lives inside the object that we called `screen`:

```python
screen.blit(image, [0, 0])
```

"Blit" is a technical term, don't worry too much about the funny word. What it means here is "draw the thing we called `image` on the thing we called `screen`".

## Actually displaying the result

There's one last hitch. Pygame doesn't show things on screen as you draw them. Instead it waits until you tell it to do it. This can be a bit annoying at first, but it is much faster because it allows the computer to do less work.

Once you have drawn the image on the screen, you tell Pygame that the screen is ready by running this code:

```python
pygame.display.flip()
```

## Challenges

1. Where do you think you have to add the lines above on the program? Try adding them yourself and see where they would go.
2. Make the image appear in the centre of the screen
3. Draw the image four times on the screen, so that it appears on each of the four corners
