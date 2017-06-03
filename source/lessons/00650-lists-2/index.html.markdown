---
title: Lists, part 2
---

So far, our lists don't change over time. If we create a list with 3 elements, it will always have the same 3 elements. But this doesn't need to be this way.

## A bit of theory: adding items to lists

We can add elements to a list during the program, using the function `append`, which lives inside lists. For example, try the following program:

```python
a = [2, 4, 8]
a.append(16)
print(a)
```

1. What does this program do?
2. How would you add another element to the list?

We can create long lists using loops. For example, type this program:

```python
a = []
count = 0
while count < 100:
  a.append(count)
  count += 2
print(a)
```

1. What does this program do?
2. How many numbers are there in the resulting list?
3. How would you list multiples of 3? How many numbers will there be in the list in that case?

## Back to Pygame

Let's improve on the program from the last lesson. If you don't have it at hand, type it from scratch. Then make the following changes:

1. Remove the references to `actor1` and `actor2`.
2. Make `actor_list` be an empty list.
3. Using a loop, create 20 actors and put them in `actor_list`, each one in a slightly different position.

Run the program. How did that go? If all is correct, there should be 20 images moving in the screen.
