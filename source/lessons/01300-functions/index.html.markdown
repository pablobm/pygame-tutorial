---
title: Functions
---

We have written a bunch of code so far, and our program is starting to look a bit confusing. There's a lot going on, and it can be difficult to read. Maybe you understand it well now, but if you leave it for a week or two and then come back, you'll have forgotten part of it. You'll have to read it again to remember what was going on. Also, if you decided to team up with someone else to develop this game, they'd have to figure it out from scratch, reading all that code.

At this point, we should take a step back for a moment and see how we can tidy this up. Neater code is easier for us and others to understand and extend. One tool to help us with this is *functions*.

## Repetitive code

To understand functions, it's better to go by example. Have a look at this chunk of code from our game:

```python
if keys[pygame.K_LEFT]:
    player.x = player.x - 5
if keys[pygame.K_RIGHT]:
    player.x = player.x + 5
if keys[pygame.K_DOWN]:
    player.y = player.y + 5
if keys[pygame.K_UP]:
    player.y = player.y - 5
```

This code checks if specific keys are pressed, and then moves the player horizontally or vertically. It's a bit difficult to read though. One possible improvement would be to write it like this:

```python
if keys[pygame.K_LEFT]:
    move_x(player, -5)
if keys[pygame.K_RIGHT]:
    move_x(player, 5)
if keys[pygame.K_DOWN]:
    move_y(player, 5)
if keys[pygame.K_UP]:
    move_y(player, -5)
```

Here we have changed the operations so that now they look like something that can be easier to read: `move_x` and `move_y`. But where do those instructions come from?

Those instructions are "function calls", and they don't exist yet. If you try to run the game now, it will break because it doesn't know what `move_x` and `move_y` mean. We need to define what they mean. We need to create *functions* with those names.

## Defining and using functions

Add this to your program, near the top but after the `import` lines:

```python
def move_x(sprite, change):
    sprite.x = sprite.x + change
```

This is an example of a *function definition*. It reads like follows:

1. `def` indicates that this is a function definition.
2. `move_x` will be the name of the function. Later we'll use it elsewhere in our code by writing "`move_x` something something".
3. Next, between round brackets, comes a list of the information that the function needs to do its work. In this specific case, we need two pieces of information, which we call `sprite` and `change`.
4. Finally we have the "body" of the function, which is the part where we do maths with the `sprite` and the `change`.

How do we use this? Well, wherever you had something like this:

```python
something.x = something.x + something_else
```

You can now instead write this:

```python
move_x(something, something_else)
```

That is called a "function call". It goes like follows:

1. The function `move_x` is "called" and given two pieces of information: `something` and `something_else`
2. The program jumps to where the function definition for `move_x` is.
3. At the function definition, `something` becomes `sprite`, and `something_else` becomes `change`. These are the two pieces of information that the function expected.
4. The function runs the code in the body: `sprite.x = sprite.x + change`.
5. When the code in the body ends, the function jumps back to the place where it was called from.

### A quick challenge

Write the function `move_y`, and use it in the code, same as we have done with `move_x` above. Run the program to check it works.

## Reusing functions

In the example above, the functions `move_x` and `move_y` are used twice each. Functions can be used and reused in many locations, as long as they make sense. For example, we can use `move_y` in the code that moves the stars. Initially, that code looks like this:

```python
for star in star_list:
    if star.y > SCREEN_HEIGHT:
        star.y = 0
        star.x = random.randint(0, SCREEN_WIDTH)
    else:
        star.y = star.y + star.speed
```

Pay attention to the last line. It reads:

```python
star.y = star.y + star.speed
```

This fits the following template:

```python
something.y = something.y + something_else
```

And therefore, it can be rewritten using the function `move_y`, like this:

```python
move_y(star, star.speed)
```

So the code to move the stars ends up reading like this:

```python
for star in star_list:
    if star.y > SCREEN_HEIGHT:
        star.y = 0
        star.x = random.randint(0, SCREEN_WIDTH)
    else:
        move_y(star, star.speed)
```

That reads a little bit better. Not a whole lot better, but it's definitely an improvement. Step by step we can make the code easier to understand.

## Functions that call other functions (that call other functions)

So far, we have created functions that we use in the main body of our code. We can also use functions inside other functions, without limit. Let's carry on tidying up the code and see what this means.

This is a piece of code that we could make clearer, it moves all the stars down, bringing them back to the top when they touch the bottom:

```python
for star in star_list:
    if star.y > SCREEN_HEIGHT:
        star.y = 0
        star.x = random.randint(0, SCREEN_WIDTH)
    else:
        move_y(star, star.speed)
```

We can can move it all into a function, pretty much verbatim:

```python
def move_stars(star_list):
    for star in star_list:
        if star.y > SCREEN_HEIGHT:
            star.y = 0
            star.x = random.randint(0, SCREEN_WIDTH)
        else:
            move_y(star, star.speed)
```

And then we simply call it like this:

```python
move_stars(star_list)
```

Make that change to the code. Do you know where the above goes?

Note that now we have a function `move_stars` that calls another function `move_y`. We are using a function within a function, and that's fine.

In fact, many other things we are using in our code are functions too: `random.randint`, `pygame.display.set_mode`, `screen.blit`, etc. They are just functions that Python and Pygame provide by default.

## Challenges

* Write a function called `draw_scene`. It will "flip" the screen to show all the changes in each new frame (see `pygame.display.flip()` at the end of your code). Use this function in your code.
* Write a function `blank_screen`. It will receive the screen and will paint it completely black. Use this function in your code.
* Write a function `draw_stars`. It will receive the screen and the list of stars, and will draw the stars on the screen. Use this function in your code.
* Write a function `draw_player`. It will receive the screen and the player sprite, and will draw the player on the screen. Use this function in your code.

## Was all this worth it?

If you completed the challenges, you should have a section of code that looks very similar to this:

```python
move_stars(star_list)
blank_screen(screen)
draw_stars(screen, star_list)
draw_sprite(screen, player)
draw_scene()
```

This is much easier to read and follow than we had before, and makes the `while` loop shorter. It may feel like we have swept the code under the carpet, moving it to functions. This is partly true, but now each of the functions is also easier to read and has a clear title (the name of the function) that describes what it's supposed to do.

Going forward, we'll want to use functions as often as possible. They make programming much easier, even if first we have think a bit more about how to best take advante of them.
