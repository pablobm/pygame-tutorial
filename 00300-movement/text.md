# Creating movement

To get images moving, we'll need to draw them many times, very fast, each time in a slightly different position. This way, we create an illusion of an object moving. We can use a loop to get this effect.

## A bit of theory: Loops

In Python, the word `while` is used to create a loop. Start a new program from scratch. Type it as follows:

```python
count = 0
while count < 10:
  print(count)
  count = count + 1
```

1. Run the program. What does it do?
2. How does it work?

## Back to Pygame: Moving the image

We needed to stop to learn loops because we need them to create animations. Now that let's go back to the program we were writing with Pygame and try to use this knowledge.

Let's try step by step. Write a program that does the following. Each line in the following list is a line of the program. Translate each line into a line of the program (revisit the previous lessons to remember how to do all this):

1. Import Pygame into the program
2. Initialize Pygame
3. Create a screen window and give it a name
4. Load an image into memory

When you are done with it, it's time to make the image move. To the program we just wrote, we are going to add code to do the following:

* Draw the image on the screen 100 times, in different positions

This is not going to be only one line of code, but several. You will have to combine the following:

* The code for the loop at the beginning of this chapter.
* Code to draw images on the screen as seen on previous chapters.

## Deleting the previous frame

If you did everything correctly, you should have an image moving across the screen, but leaving a "wake" behind it. How can we avoid this?

The problem here is that we are drawing on top of the previous screen. Instead, we need to make sure that the screen is deleted before we start painting a new frame. You can use the following piece of code, which paints the whole screen black:

```python
screen.fill([0,0,0])
```

Where do you think that line should go?

## Challenges

1. Get the image moving horizontally.
2. Get the image moving vertically.
3. Get the image moving diagonally.
4. Any one of the above, but faster.
5. Get the image to start from the bottom right corner and move up.
6. Get the two identical images moving on the screen in different directions.
7. Get two different images moving on the screen in different directions.
