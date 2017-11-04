---
title: Keyboard events
---

To know when the player has pressed a key, we can use events. When a key is pressed, an event takes place. It will have the type `pygame.KEYDOWN`. To know which specific key it is, we compare it with the possible options. For example:

```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            exit(0)
        elif event.key == pygame.K_LEFT:
            print("You pressed LEFT")
        elif event.key == pygame.K_RIGHT:
            print("You pressed RIGHT")
```

This is what the program does:

  1. It loops through every event in the event queue.
  2. For each event, it checks if it's a keypress.
  3. If it's a keypress, it will check what key it was, asking one possibility at a time:
    * If it's the Q key, it closes the program.
    * If it's the left arrow key, it prints "You pressed LEFT".
    * If it's the right arrow key, it prints "You pressed RIGHT".

Each `KEYDOWN` event comes with a `key`, telling which key it was that the player pressed.

Inside `pygame` there are a bunch of things that represent each key, and we can use to compare. For example, `pygame.K_q` represents the 'Q' key in the keyboard. To know if the player pressed this key, we compare it with `event.key`, like this: `event.key == pygame.K_q`. If instead we want to know when the left arrow key was pressed, with compare with `pygame.K_LEFT`.

## Challenges

Let's see how well you understood all that:

  * Try the example above in your program. Where do you think it goes?
  * Add code to the example so that the program closes both when Q is pressed and when the player clicks on the 'close' button of the window.
  * Add code to the example so that it prints messages when pressing the up and down arrow keys.
