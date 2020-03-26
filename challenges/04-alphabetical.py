# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

import random

def quick_sort(quick_list, start, end):
  # If start point is greater than end point, that list is sorted and can be returned
  if start >= end:
    # Printing each returned list because it won't print outside the function despite returning it.
    print("".join(quick_list))
    return quick_list
  
  # Get a random index in our list to start our comparison around
  pivot_idx = random.randrange(start, end+1)
  # Get the element at that index for comparisons
  pivot_element = quick_list[pivot_idx]

  # Swap our random element with the last element
  quick_list[end], quick_list[pivot_idx] = quick_list[pivot_idx], quick_list[end]

  # Create a copy of the start index to manipulate it without losing our start value
  start_pointer = start

  # Go through the list
  for index in range(start, end):
    # Check if the current element is less than the pivot element
    if quick_list[index] < pivot_element:
      # If yes, swap that element with the element at start pointer
      quick_list[index], quick_list[start_pointer] = quick_list[start_pointer], quick_list[index]
      # Increase start pointer index to go to the next
      start_pointer += 1
  
  # Swap element at the end index, which was placed at the pivot index earlier, with the element of our manipulated start index
  quick_list[end], quick_list[start_pointer] = quick_list[start_pointer], quick_list[end]

  # Now recursively call quick sort of the list in two parts. This will continue until it's become basically pairs that are easy to swap
  quick_sort(quick_list, start, start_pointer - 1)
  quick_sort(quick_list, start_pointer + 1, end)


user_input = input("What would you like alphabetized?\n")
user_list = list(user_input.lower())
quick_sort(user_list, 0, len(user_list) - 1)