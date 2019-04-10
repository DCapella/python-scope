#########################
# !!! SOLUTION CODE !!! #
#########################



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

      # Need to enumerate so we can loop twice
      for i, n in enumerate(arr):
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
