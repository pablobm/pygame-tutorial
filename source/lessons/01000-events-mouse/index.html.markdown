---
title: Mouse events
---

To know when the player is using the mouse, we use events. When the players moves the mouse, clicks a button, or presses a key, an event joins the event queue. This event will have the type `pygame.MOUSEMOTION`, and will include other useful information, such as its position, or what buttons were pressed.

This is an example of use:

```python
for event in pygame.event.get():
    if event.type == pygame.MOUSEMOTION:
        print("The mouse moved")
        print("The X position is now" + event.pos[0])
        print("The Y position is now" + event.pos[1])
```

This is what the program does:

  1. It loops through every event in the event queue.
  2. For each event, it checks if its about mouse movement.
  3. If it's about mouse movement, we print a message telling us, as well as two other messages reporting its position.

Challenges:

  * Try the example above in your program. Where do you think it goes?
  * Ensure that the program responds both to mouse movement and to the window being closed.

## The position of the mouse (and a bit about lists)

The example above does something strange to read the position. It uses `event.pos[0]` and `event.pos[1]`, which look a bit complicated. Let's look into that.

Each `event` comes with a few things inside. For example, it has `event.type`, which tells what type of event it is. Remember that the dot `.` means "inside", so the `type` is something inside `event`, therefore we use it as `event.type`. The same with `MOUSEMOTION`: it lives inside `pygame`, so we refer to it as `pygame.MOUSEMOTION`.

Apart from the type, each event will have other things inside, which depend on the type of event. A `MOUSEMOTION` event has a `pos`, which is the position of the mouse. This position is represented as a list of two elements: X and Y.

Remember how lists work? This is an example of a list with two elements:

```python
position = [123, 456]
```

We have seen how to loop through a list and do something with each element, but we haven't seen how to work with a specific element of the list. For example, how to do something only with the first element, or only with the hundredth element. Let's see that.

Computers have a funny way to count. When people count (for example with their fingers), we start counting at 1, and then go 2, 3, 4... Computers don't do that: they normally start at 0 and then go 1, 2, 3... This is important now. For a computer, the first element of a list is the element number 0, and the second element is the element number 1. The 100th element is element 99 and so on.

We can read inside a list using square brackets `[]` and a number, like this:

```python
position = [123, 456]
print("The first element is " + position[0])
print("The second element is " + position[1])
```

## Challenges

Let's see how well you understood all that:

  * Write a program where you move a small image using the mouse.
    * Nothing complicated: simply that the image will be in the same position as the mouse.
    * You will have to read the mouse position from the event, and use it to set the position to the image.
    * If you follow the example from the "Objects" chapter, you should be able to do something like `actor.x = event.pos[0]`.
