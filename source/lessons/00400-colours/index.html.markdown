---
title: Colours
---

In the previous section, we used the following code to fill the screen black before painting a new frame:

```python
screen.fill([0,0,0])
```

That line tells the screen to fill in the colour black. The numbers `[0, 0, 0]` represent the colour black, but what do the numbers have to do with the colour?

The most common way to represent colours in computers is using three numbers. These numbers tell how much red, green and blue light needs to be mixed together to give a specific color. For example, black is `[0, 0, 0]`, representing zero amounts of red light, green light and blue light. No light at all. As dark as it can be.

This way of representing colours with numbers is called RGB, standing for Red, Green, Blue. There are other ways of representing colours, always using three or four numbers. RGB is the most common system, especially when making video games.

In terms of RGB, "pure" red will only have red. "Pure" green will only have green. "Pure" blue will only have blue. This is how to represent those colours with numbers:

* Red: `[255, 0, 0]`
* Green: `[0, 255, 0]`
* Blue: `[0, 0, 255]`

## Challenges

* Paint the screen red
* Paint the screen green
* Paint the screen blue
* Try with other numbers

<div class="main-body__note"><div class="main-body__note-body">
<p>The number 255 is the maximum number we can use. When representing a colour, each of the three numbers must be between 0 and 255. The number 255 seems a bit random, but it is not arbitrary: it is a limit given by how all this works internally. Don't worry about that for now. Just know that 255 is the maximum possible value in many programming-related measures.</p>
</div></div>

## Mixing colours

To get other colours, we mix red, green and blue. For example:

* Yellow: `[255, 255, 0]`
* Magenta: `[255, 0, 255]`
* Cyan: `[0, 255, 255]`
* Brown: `[80, 40, 25]`
* Pink: `[255, 200, 200]`

## Challenges

1. How do you paint the screen white? Hint: white is all colours together, cranked up to the max
2. How many different colours can you possibly get with this system?

## These numbers are annoying

Don't worry about the numbers too much. You should know what they mean, but there's no need to memorise each combination. When you need a colour, you can just look it up on the Internet by name and copy its RGB values. There are many websites where you will find them.

To avoid typing down the numbers every time, you can give names to colours. For example:

```python
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
# etc...
```

Then we can use the above in our programs by name:

```python
# The same as screen.fill([255, 0, 0])
screen.fill(RED)
```

## Constants

Note that the example above uses names in all-capitals. This is no different from using all-lowercase names, but we do it because there is a common convention that many programmers use and understand: use all-capitals names for variables that will not change over time.

In previous examples, we had variables such as `count`. These changed over time within the program. However colours don't change. Red is always red. Things in your game may change colour, but the concept of a colour doesn't change.

Therefore, it's common among programmers to use all-capitals names to signify things that don't change. We call them **constants**. Compare this with the name **variables**, which signify things whose value may change over time.

## Challenges

1. Think of a few colours and look them up on the Internet. Find their RGB values and create constants to refer to them. Use them in your program.
2. Modify your program so that the background starts black, and changes gradually to white.
