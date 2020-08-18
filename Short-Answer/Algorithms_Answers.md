#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```
Based on the while loop and variable assignment I would say the runtime is
O(n^3) because regardless of how small the input is the while loop has to check for n^3 every single time.
```


b)
```
the for loop is a standard i to amount of indexed items in the input n so O(n)
I would say the runtime is O(n log n).

So let's say that n is equal to 3


sum = 0
i = 0
j = 1

while 1 is less than 3:
    j is equal to 1 * 2
    sum is equal to 1 + 1
    j now is equal to 2... go back to while loop

while 2 is less than 3:
    j is equal to 2 * 2
    sum is equal to 2 + 1
    j now is equal to 4... go back to while loop

while 4 is less than 3:
    in this case is false so go back to outer loop

and repeat this process for each element in n.
The inner loop executes approx half as much as the outer loop because we are
multiplying j times 2 each time thus decreasing the amount of time this loops
has to execute by about half. So I would say instead of it being a linear O(n) operation it becomes O(log(n))

Together it would be O(n log n)

```


c)

```
So for this one I would go for O(n) because all we are returning is 2 and the function runs n times. It is recursive yes but there is not any operations running to make it more than O(n). It is just running n times and adding a single value.

def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

the function itself is returning 2 + whatever the function returns which is always going to be 2 thus making bunnyEars(3) = 6
```

## Exercise II


```
def highestFloor(floor,eggs):
    
    


```