---
title: Python basics
---

Before we get on with Pygame, we need to understand some basic concepts. These are:

1. Comments
2. Variables
3. Functions
4. Libraries

The above are concepts that exist in most programming languages, with subtle differences. Here we'll learn how they work in Python.

## Comments

In a program, there's the concept of "comments". Comments are not really code. They are parts of the program where we write something down in plain English, to help us or others understand what's going on.

In Python, comments start with a hash character `#`. This is an example:

```python
# This will be ignored by the program
```

You will see comments in the examples here. They are there only to guide you and don't have any special meaning.

## Variables

Computer programs deal with data. "Data" can be numbers, pieces of text, on/off states, etc, that the program keeps in memory. For example, the game _Minecraft_ needs to keep track of a bunch of things, such as:

* Your energy (a number).
* The time of the day (a number).
* Your position (three numbers).
* The position of anything in the game (three numbers for each single thing).
* The name of a save slot (a list of numbers, each representing a letter, together forming words).
* A block (five numbers: three for the position, one that tells the block type, one to tell the damage it has received).
* And many, many more things, one for each single concept in the game.

This is an example of variable:

```python
energy = 100
```

The code above creates a variable. We called it `energy` and decided its value was going to be 100. We could have called it anything else, or given it a different value (a different number).

Variables can have almost any name we can think of, with some restrictions. One restriction is that they cannot have spaces. It's possible to use underscores to have multiple words though:

```python
player_energy = 100
```

You can do math with variables. If the initial energy is 100 and an arrow takes 20 units from you, you could do this:

```python
player_energy = 100 - 20
```

We give descriptive names to variables to help us remember what's going on in the program. We can use variables in our math to get something like this:

```python
initial_energy = 100
arrow_damage = 20
player_energy = initial_energy - arrow_damage
```

Finally, they are called "variables" because they change. The game is more likely to go like this:

```python
initial_energy = 100
arrow_damage = 20

player_energy = initial_energy
# ... each time we get hit by an arrow ...
player_energy = player_energy - arrow_damage
```

In the code above, the variable `player_energy` started as 100, then changed to 80.

<div class="main-body__note"><div class="main-body__note-body">
<p>When we say `energy = 100`, this is not the same "equals" `=` that you normally use in math. The `energy` will not always be `100`. It will change over time.</p>
<p>Thing of it as "the `energy` is `100` for now".</p>
</div></div>

## Functions

Variables store data, but they don't do anything. To do stuff we use functions.

This is an example of a function being used:

```python
print()
```

The function is `print`, and we use it by writing parentheses (round brackets) after it.

`print` is used to show things on a terminal screen. In the example above we don't actually show anything, because we are not telling `print` what so show.

Functions use data. If we give data to `print`, it will print it out. The following program prints number 10 on the terminal:

```python
print(10)
```

The program tells the function `print` to use number 10. In programmer's lingo, we say that we pass `10` to the function, and that the function "receives" `10`. We can also use variables, or do math:

```python
energy = 100
print(energy)
print(energy - 20)
```

Write the program above and run it. What does it do?

Functions can take more than one piece of data. Here we print two numbers:

```python
initial_energy = 100
current_energy = 50
print(initial_energy, current_energy)
```

When passing more than one piece of data to a function, we use a comma `,` to separate them.

## Libraries

Libraries are collections of functions that we can use in our programs. Python comes bundled with many libraries, and we can download more or even create them ourselves.

To use a library, we use the special word `import`. When we import a library, it is read from the hard disk and loaded in memory. Here we import a library called `math`:

```python
import math
```

The library `math` comes included with Python, and has functions to do complex math.

When we import a library, a variable of the same name is created on our project. For example, we imported `math`, so we get a variable called `math`. Inside this variable, we can find functions. To look inside a variable, we use the full stop symbol `.`. This example uses a function to calculate the factorial of 10:

```python
import math
result = math.factorial(10)
print(result)
```

Some things happening here:

* We import `math` into our program.
* The function `factorial` lives in `math`.
* We use the full stop `.` symbol to reach inside `math` and get to the `factorial` function.
* We use `factorial` and pass it a `10`.
* The factorial has a result. We store it in a variable that we call `result` (it can have any name).
* We can see the result by printing it.

Another example, a bit more complicated:

```python
import math
print(math.pow(2, 3))
```

More notes on that:

* We pass two numbers to `math.pow`
* `math.pow` raises the first number to the power of the second (in this example, 2 to the power of 3).
* We print the result straightaway, without bothering with storing it on a variable first.

## Challenge

Write a program that does the following:

1. Import the `time` library
2. Print a number (any number)
3. Use the function `sleep` in the `time` library. Pass it the number 5.
4. Print a number (again, any number is ok)

What does the program do? What does `sleep` do?
