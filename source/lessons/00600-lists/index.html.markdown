---
title: Lists
---

Chances are that our programs won't have just one thing to draw, but many. We could have a hundred characters moving around, and we don't want to write code for each and every one of them. It would be boring and time-consuming.

Fortunately, we can make "lists" of things. When we have lists, we can write code to deal with everything on the list, regardless of whether the list has one item or a thousand.

## A bit of theory: lists

Start a new program from scratch. Type it as follows:

```python
many_things = [2, 4, 6]
print(many_things)

for thing in many_things:
    print(thing)
```

The words `for` and `in` above are special. They create a loop, similar to the ones we have already seen. We use this construct to loop over lists. We could do it with `while` too, but it's easier this way.

1. Run the program. What does it do?
2. How does it work?
3. Add other items to the list and run the program.

You can use variables in lists too:

```python
some_number = 4
many_things = [2, some_number, 6]
print(many_things)

for thing in many_things:
    print(thing)
```

You can even have lists of lists:

```python
some_number = 4
first_list = [2, some_number, 6]
second_list = [first_list, 4, 5]
print(second_list)

for thing in second_list:
    print(thing)
```

## Back to Pygame: moving many things

Now we are going to use two concepts we just learned:

  * Objects: to keep together details related to each thing on the screen.
  * Lists: to deal with many things at once.

Let's try again to build a Pygame program from scratch. Start with a blank Python file and write code for each of the following, one at a time:

1. Import Pygame into the program.
2. Define the color black as a constant.
3. Initialize Pygame
4. Create a screen window and give it a name.

So far, it's all stuff we have done before. Next let's apply some of what we saw in the chapter about objects:

1. Define a class `Actor`.
2. Create an actor and put it in the variable `actor1`.
3. Set the `x` and the `y` coordinates for the actor. Use any numbers you like.
4. Set an image for this actor. Choose any image you like.
5. Create a second actor, `actor2`, with the same image, but different coordinates.
6. Create a list `actor_list` that has both `actor1` and `actor2`.

OK so far? Here comes the interesting part. After the code above, write code for the following:

1. A loop that runs 300 times. Each time it will do all the steps below:
    1. Paint the screen completely black.
    2. For each actor in `actor_list`, do the following:
        1. Increase the `y` coordinate.
        2. "Blit" the image for the actor on the screen.
    3. "Flip" the screen to update it.

Come on, get typing. I'll wait.

OK, how did it go? If you are having trouble, remember to address one thing at a time. Don't try to write all at once. Review the previous lessons if you need.
