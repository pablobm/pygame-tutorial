# Events

For a game, it's not enough with moving objects on a screen. We need to tell what the player is doing with the keyboard or the mouse, so that they can control the action.

Each time a key is pressed, or the mouse moves, or some other action takes place, Pygame notifies us with an "event". Our program will need to read these events, figure out what they mean, and make changes to the game accordingly.

Events happen all the time while the program is running. They accumulate in a queue waiting for us to check them. Because there can be several of them waiting for us, we need a loop to deal with each and every one of them before we carry on drawing the scene.

This is the simplest loop to deal with events:

```python
for event in pygame.events.get():
  # deal with `event` here
```

The word `for` in Python is similar to `while`, but works a bit differently. Don't worry about that for now. What you need to know is:

  * `pygame.events.get()` gives us the "queue" of events that need to be dealt with 
  * For each event, the code inside the loop will run and we'll be able to refer to the event as `event`
  
 
