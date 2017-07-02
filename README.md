# Left Rotation HackerRank Challenge!

Here is a solution/explanation for the [Left Rotation Challenge](https://www.hackerrank.com/challenges/ctci-array-left-rotation).

## The Challenge

We are given a task:

```
Given an array of n integers and a number, d, perform d left rotations on the array. Then print the updated array as a single line of space-separated integers.
```
So we will have an array and we must alter the array, shifting all the elements to the left by the number of rotations offered, and return the updated list.

## The Solution

[The index splice](https://stackoverflow.com/questions/509211/explain-slice-notation) 

```
def array_left_rotation(a, n, k):
    alist = list(a)
    b = alist[k:]+alist[:k]
    return b
```

Here we make a list with our array. Next we create a variable and give equal two index slice statements added together. With an index slice, an item that occurs before the `:` is the start, where an item that occurs after is the end. The first `alist[k:]` will return the elements beginning at `index[k:]`. So let's say our `k` happens to be 2 and we therefore must shift our elements 2 places to the left. In this example we have an list `a=(1,2,3,4,5,6,7,8)`, `index[k:]` will therefore return 3,4,5,6,7,8. Likewise our second statement only ends at 2, so it would return 1,2.  If we add those together we get a list of items shifted by 2 or 3,4,5,6,7,8,1,2.