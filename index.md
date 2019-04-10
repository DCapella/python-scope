# Python Scope

#### [HackerRank](www.hackerrank.com)

> Complete the Difference class by writing the following:
> A class constructor that takes an array of integers as a parameter and saves it to the __elements instance variable.
> A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the maximumDifference instance variable.

## PreWork

Input: [1, 2, 3, 4]

Process:

* Do not need to repeat because  absolute 1 - 2 is absolute 2 - 1.

* Example steps:

absolute of 1 - 2

absolute of 1 - 3

absolute of 1 - 4

* Then

absolute of 2 - 3

absolute of 2 - 4

* Last number

absolute of 3 - 4

* Looks like two for loops. Will need at least an iteration index
* Need to return 1 before length
* list->set->list so will need to return 0 because [1, 1, 1]->(1)->[1] so absolute of 1-1 = 0

### Steps

* Instantiate variable maximumDifference to 0
* define method computeDifference, declared with results, arr, and arr_len
* return if arr_len is 0 else loop through range of arr_len
* set max of results and return if i is arr_len - 1
* loop through i + 1 as j and append absolute difference

## Code

### Instantiate variable maximumDifference to 0

```python
class Difference:
    def __init__(self, a):
        self.__elements = a
        # Set mD to 0 since that's the only number that will cause an error
        self.maximumDifference = 0
```

### define method computeDifference, declared with results, arr, and arr_len

```python
# Add your code here
    def computeDifference(self):
      # Declare results so we don't have to touch instance variable till the end
      results = []
      # Turn into a set to get rid of extra numbers and back to a list to be able
      # to enumerate through
      arr = list(set(self.__elements))
      # DRY
      arr_len = len(arr)
```

### return if arr_len is 0 else loop through range of arr_len

```python
# If all the numbers in the arr are the same, it will return 0
      # Which is what instance variable is already set to
      if arr_len == 1: return
  
      # Need iteration number
      for i in range(arr_len):
```

### set max of results and return if i is arr_len - 1

```python
# Stop before it gets to the end and raises an error
        if i == arr_len - 1:
          self.maximumDifference = max(results)
          return
```

### loop through i + 1 as j and append absolute difference

```python
# Second loop that starts after the first number since its absolute
        for j in range(i+1, arr_len):
          results.append(abs(arr[i] - arr[j]))
```

## Final Code

```python
class Difference:
    def __init__(self, a):
        self.__elements = a
        # Set mD to 0 since that's the only number that will cause an error
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
      # Declare results so we don't have to touch instance variable till the end
      results = []
      # Turn into a set to get rid of extra numbers and back to a list to be able
      # to enumerate through
      arr = list(set(self.__elements))
      # DRY
      arr_len = len(arr)
      # If all the numbers in the arr are the same, it will return 0
      # Which is what instance variable is already set to
      if arr_len == 1: return
  
      # Need iteration number
      for i in range(arr_len):
        # Stop before it gets to the end and raises an error
        if i == arr_len - 1:
          self.maximumDifference = max(results)
          return
        # Second loop that starts after the first number since its absolute
        for j in range(i+1, arr_len):
          results.append(abs(arr[i] - arr[j]))

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
```
## Conclusion

It was not difficult except for working within the restraints of [HackerRank](www.hackerrank.com).
