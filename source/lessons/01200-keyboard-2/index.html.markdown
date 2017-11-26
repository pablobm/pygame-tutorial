---
title: Keyboard without events
---

There are actually two different ways of checking if the player is pressing keys. One is with events, as we have seen. We'll see the second one next.

The function `pygame.key.get_pressed()` will get us a list of all keys that are pressed at the time. We use it like this:

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
  print("The LEFT arrow is pressed")
```

This is how the above works:

1. We get the list of the keys that are pressed right now. We put it in the variable `keys`.
2. We look into this list using square brakets. With `keys[pygame.K_LEFT]` we check if the left arrow was pressed.
3. If this is true (if the left arrow was pressed), we print a message.

This example uses `pygame.K_LEFT` same as we were using it earlier with events. The same will work for any other key.

## Challenges

* Use `pygame.key.get_pressed` to program the movement of a character (an image) on the screen.
* Ensure that you can also close the program by clicking on the "close" button of the window, or pressing Q, using events.
* Integrate the starfield of previous chapters on this game, so that the stars serve as background to your character.

## Should we use keyboard events or not?

So there are two ways of reading the keyboard. Which one is better? The answer is "it depends". You will use one or the other depending on the situation.

  * If the key can be kept pressed for a continuous action, use `pygame.key.get_pressed()`. For example, for movement.
  * If the key should be pressed only once at a time, for a quick action, use events. For example, for a jump, or a throw.
