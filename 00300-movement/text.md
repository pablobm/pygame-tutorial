# Creating movement

To get images moving, we'll need to draw them, then draw them again a bit further, and again a bit further, etc. We can use a loop to get this effect.

## Loops

In Python, the word `while` is used to indicate a loop. Write this example program:

```python
count = 0
while count < 10:
  print count
  count = count + 1
```

* Run the program. What does it do?
* How does it work?

## Moving the image

Right, so how do we translate this to what we are trying to do?

Let's try step by step. Write a program that does the following:

1. Imports pygame
2. Initializes pygame
3. Creates a screen window
4. Loads an image
5. Draws the image on the screen 100 times, in different positions

## Deleting the previous frame

If you did everything correctly, you should have an image moving across the screen, but leaving a "wake" behind it. How can we avoid this?

The problem here is that we are drawing on top of the previous screen. Instead, we need to make sure that the screen is deleted before we start painting a new frame. You can use the following piece of code, which paints the whole screen black:

```python
screen.fill((0,0,0))
```

Where do you think that line should go?

## Challenges

* Get the image moving horizontally
* Get the image moving vertically
* Get the image moving diagonally
* Any one of the above, but faster
* Get the image to start from the bottom right corner and move up