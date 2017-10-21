---
title: Intoduction to events
---

For a game, it's not enough with moving objects on a screen. We need to tell what the player is doing with the keyboard or the mouse, so that they can control the action.

Each time a key is pressed, or the mouse moves, or some other action takes place, Pygame creates an "event". Our program will need to collect these events, read them, and make changes to the game accordingly.

Events happen all the time while the program is running. They accumulate in a queue waiting for us to check them. Because there can be several of them waiting for us, we need a loop to deal with each and every one of them before we carry on drawing the scene.

This is the simplest loop to deal with events:

```python
for event in pygame.events.get():
  # deal with `event` here
```

This is what the codes does:

  * `pygame.events.get()` gives us the "queue" of events that need to be dealt with.
  * For each event, the code inside the loop will run. We'll be able to refer to the event as `event`.

Here's an useful example. The following snippet of code terminates the program when the user clicks the "close" button on the window:

```python
for event in pygame.event.get():
  if event.type == pygame.QUIT:
    exit(0)
```

Wait, how does that work? This is what each line of code is doing:

  1. It loops through every event in the event queue.
  2. For each event, it checks if its type is `pygame.QUIT`. This is the event that appears when the close button is clicked.
  3. If the event is indeed the "quit" event, it uses the `exit` function to terminate the program.

Go on and add that snippet to your current program. Where do you think it goes? (Hint: it's not at the end).
