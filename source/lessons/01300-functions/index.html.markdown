---
title: Functions
---

We have written a bunch of code so far, and our program is starting to look a bit confusing. There's a lot going on, and it can be difficult to read. Maybe you understand it well now, but if you leave it for a week or two and then come back, you'll have forgotten part of it, and you'll have to read it again to remember what was going on. Also, if you decided to team up with someone else to develop this game, they'd have to figure it out from scratch, reading all that code.

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

Those instructions are "function calls", and they don't exist yet. If you try to run the game now, it will break because it doesn't know what `move_x` and `move_y` means. We need to define what they mean. We need to create *functions* with those names.

## Defining and using functions

Add this to your program, near the top but after the `import` lines:

```python
def move_x(sprite, change):
    sprite.x = sprite.x + change
```

This is an example of a *function definition*. It reads like follows:

1. `def` indicates that this is a function definition.
2. `move_x` will be the name of the function. Later we'll use it by writing "`move_x` something something".
3. Next comes a list of the information that the function needs to do its work. In this specific case, we need two pieces of information, which we call `sprite` and `change`.
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
