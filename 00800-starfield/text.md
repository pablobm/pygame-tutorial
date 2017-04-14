# Star field

So we have many things on the screen. Let's move them and try to create something useful. We can draw small circles moving down the screen and simulate a star field.

## A bit of theory: conditionals

You may have seen this before, but it's good to refresh our memories. Write a new program that does the following:

```python
number = 4
if number > 10:
  print("The number is greater than 10")
elif number == 10:
  print("The number is 10")
else:
  print("The number is less than 10")
```

* What does the program do?
* How can you change the first line so that a different message is printed?

## Flying though space

We can now use all we have learned so far to create a star field animation. As usual, start a new program from scratch that does the following:

1. Import the `random` library.
2. Import Pygame.
3. Define a class `Star`.
4. Create an empty list where we'll put our stars.
5. Write a loop that will run 100 times. Each time it will do the following:
    1. Create a `Star` object and put it in a variable.
    2. Give the star a random `x` coordinate, between 0 and 800.
    3. Give the star a random `y` coordinate, between 0 and 600.
    4. Give the star a random `size`, between 1 and 3.
    5. Give the star a random `speed`, between 1 and 3.
    6. Give the star a random `brightness`, between 0 and 255.
    7. Add the object to the list of circles.
6. Initialize Pygame
7. Create a window of size 800x600
8. Write a loop that will run 500 times. On each iteration, do the following:
    1. Paint the screen completely black
    2. For each star in the list, do the following:
        1. Draw a circle on the screen so that:
            * The radius is the size of the star
            * The colour is the brightness of the star, three times as a list. Eg: if the brightness is `150`, the colour will be `[150, 150, 150]`.
            * The position uses the `x` and `y` values for the star.
        2. Change the `y` coordinate of the star so that:
            * If it is less than 600, it increases by 1
            * Otherwise, it is set to 0
    3. Update the screen

