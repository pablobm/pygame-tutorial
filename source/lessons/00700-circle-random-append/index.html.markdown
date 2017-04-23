---
title: Circle, random, append
---

Before we go further, we need to stop again and learn a few things. For the next program, we'll need some new functions that we haven't seen before. Let's see them one by one.

## Drawing circles

Using Pygame we can draw circles on the screen. This is the code we need to use:

```python
pygame.draw.circle(screen, color, position, radius)
```

The words `screen`, `color`, `position` and `radius` are information that you'll have to provide. This is an example of use:

```python
pygame.draw.circle(screen, [255, 255, 255], [100, 100], 10)
```

The code above will draw a white circle with a 10-pixel radius at the position x=100 and y=100. You will have to provide a `screen` similar to how you have done before. Write a program to try it out. Then answer these questions:

* Why is the circle white?
* How would you make the circle red?
* How would you draw the circle at a different position?
* How would you draw a larger circle?

## Generating random numbers

In Python, there are several ways of generating random numbers. Regardless of how you do it, you'll need to import the `random` library into your program. Then you can use a function such as the following:

```python
random.randint(1, 10)
```

That code will generate a random number between 1 and 10.

* How would you generate a number between 100 and 200?
* Write a program that generates a random number, puts it in a variable, and then prints the value of the variable.

## Adding things to lists

We have seen how to create lists. Here's how to add things to list that already exist:

```python
my_list.append(new_item)
```

Calling `append` on a list that already exists, you can add a new element at the end of the list. This is an example:

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```

And here's a challenge:

* Write a program that creates a list, adds 100 numbers to it, and then prints the list.

## Putting it all together

OK, so now let's write a program that uses all the above. Write code for each one of the following steps, one by one:

1. Import the `random` library.
2. Import Pygame.
3. Define a class `Circle`.
4. Create an empty list where we'll put our circles.
5. Write a loop that will run 100 times. Each time it will do the following:
    1. Create a `Circle` object and put it in a variable.
    2. Give the object a random `x` coordinate, between 0 and 800.
    3. Give the object a random `y` coordinate, between 0 and 600.
    4. Give the object a random `radius`, between 5 and 50.
    5. Add the object to the list of circles.
6. Initialize Pygame
7. Create a window of size 800x600
8. Write a loop that, for each object in the list, it does the following:
    1. Draw a white circle on the screen, with the coordinates and radius given by the object in the list
9. Update the screen.
