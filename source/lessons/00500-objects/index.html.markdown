---
title: Objects
---

Before we go further, we need to stop a moment to organise our code a bit better. This will help us later to deal with many things moving at the same time.

## A bit of theory: objects

Until now, we have had one thing moving around the screen. This thing had three qualities that defined it:

  * A horizontal position.
  * A vertical position.
  * An image that represents it on the screen.

When things have several qualities, it's useful to store them together. This becomes helpful later as it makes it easier to know what belongs to what. In many programming languages, we have "objects" that help us do exactly that.

Start a new, blank program and type the following:

```python
class Student:
    pass

s = Student()
s.name = "Ash"
s.age = "10"
```

The two first lines define a new "class" of "objects". You can read it as "some things in this program are going to be 'students'". It may sound a bit weird, but it'll be useful later. Don't worry too much, you don't have to understand it completely.

The next three lines read as follows:

  * Create a new student and put it on a variable called `s`.
  * `s` has a name, and it's "Ash".
  * `s` has an age, and it's 10.

This is not very different from creating variables for names and ages as we have done in the past. The thing that is different is that `name` and `age` are going to live inside `s`. We'll use the dot `.` symbol to read and write the student's name and age.

Using the dot `.` symbol, we can access the name and age, same as we do with any other variable. For example, add this to the program:

```python
print("My name is")
print(s.name)
print("and I am")
print(s.age)
print("years old")
```

So nothing new. Only that now we are putting variables inside other variables to help us organise the program better. There's a lot more that can be done with objects, but we can do just with this for the moment.

## Back to Pygame: using an object in our game

We are going to create an object that will represent our moving image. A moment ago we used an object that had a name and an age. Now we are going to have an object that has horizontal and vertical positions (`x` and `y`), and an image.

Go back to your Pygame program and try make the following changes:

  * Before the main loop:
    * The things that move on screen on our program are going to be called "actors". Define a class called `Actor`. _(2 new lines)._
    * Create a variable representing an actor. _(1 new line)._
    * We had a variable for our image. Change it so that it is stored inside our actor instead. _(modify one existing line)._
    * Set the `x` and the `y` of the actor. Make them `0` at the start. _(2 new lines, one for each coordinate)._
  * In the main loop:
    * Change the `x` coordinate of the actor so that it increases by 1 on each iteration of the loop. _(1 new line)._
    * Modify the `screen.blit` line so that it works with our new object. _(modify the existing line)._

If everything goes according to plan, the program should do exactly the same thing it was doing before. This was not about adding something to the program, but about organising things before we go forward.
