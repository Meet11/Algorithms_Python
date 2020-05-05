#Python implementation of max subset sum no adjacent
#Time Complexity - O(N)
#Space Complexity - O(1)

#Description - To find the max sum, we need to check previous two elements and take max of addition of self with the i-2th element or i-1th element
#Consider - [2, 1, 5, 6, 4]
#maxSums = [2, 2, 7, 8, 11]
#initialise the first element to the arrays first element, and the second to be the max of first element and the second element to get the base scenario for our solution

def maxSubsetSumNoAdjacent(array):
  if not len(array):
	return 0
  if len(array) == 1:
	return array[0]
  if len(array) == 2:
	return array[1]
  first = array[0]
  second = max(array[0], array[1])
  for i in range(2, len(array)):
  	maxSums = max(first + array[i], second)
	first = second
	second = maxSums
  return maxSums
