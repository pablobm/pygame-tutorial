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

## Challenges

* Get the image moving horizontally
* Get the image moving vertically
* Get the image moving diagonally
* Any one of the above, but faster
* Get the image to start from the bottom right corner and move up