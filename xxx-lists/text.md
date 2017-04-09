# Lists

Chances are that our programs won't have just one thing to draw, but many. It's boring and time-consuming to write code to handle each and every one thing that shows up in your program.

Fortunately, we can make "lists" of things. When we have lists, we can write code to deal with everything on the list, regardless of whether the list has one item or a thousand.

## A bit of theory: lists

Start a new program from scratch. Type it as follows:

```python
many_things = ["one", "two", "three"]

for thing in many_things:
    print(thing)
```

The words `for` and `in` above are special. They create a loop, similar to the ones we have already seen. We use this construct to loop over lists. We could do it with `while` too, but it's easier this way.

1. Run the program. What does it do?
2. How does it work?
3. Add other items to the list and run the program.
4. Try with things other than text in the list.

## Back to Pygame: moving many things

