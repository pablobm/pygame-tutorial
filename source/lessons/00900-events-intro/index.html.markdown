---
title: Intoduction to events
---

For a game, it's not enough with moving objects on a screen. We need to tell what the player is doing with the keyboard or the mouse, so that they can control the action.

Each time a key is pressed, or the mouse moves, or some other action takes place, Pygame creates an "event". An event is a message that the program leaves for us, to let us know that something has happened. These are some examples of events:

  * The 'up' key was pressed.
  * The mouse moved to the position x=143,y=21.
  * The user clicked the 'close' button on the window.

Our program will need to collect these events, read them, and make changes to the game accordingly.

Events happen all the time while the program is running. They accumulate in a queue waiting for us to check them. Because there can be several events waiting for us, we need a loop to deal with each and every one of them before we carry on drawing the scene.

This is the simplest loop to deal with events:

```python
for event in pygame.event.get():
  # deal with `event` here
```

This is what the codes does:

  * `pygame.event.get()` gives us a list of events that need to be dealt with. This is all the events that have been waiting in queue since the last time we checked.
  * For each event, the code inside the loop will run. We'll be able to refer to the event as `event`.

Here's a useful example. The following snippet of code closes the program when the user clicks the "close" button on the window:

```python
for event in pygame.event.get():
  if event.type == pygame.QUIT:
    exit(0)
```

So how does this work? This is what each line of code is doing:

  1. It loops through every event in the event queue.
  2. For each event, it checks if its type is `pygame.QUIT`. This is the event that appears when the close button is clicked.
  3. If the event is indeed the "quit" event, it uses the `exit` function to close the program.

Go on and add that snippet to your current program. Where do you think it goes? (Hint: it's not at the end).
