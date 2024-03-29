#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  # nums.sort()
  # for i,elem in enumerate(nums):
  #   while i < len(nums)-1 and elem == nums[i+1]:
  #     nums.pop(i+1)
  # return nums

  # What if the sequence must be the same as appeared in 'nums'? Sort() doesn't help here
  a=[]
  for nro in nums:
    try:
      a.index(nro)
    except ValueError:
      # nro is a non visited elem. Adding it up to results
      a.append(nro)
  return a

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
  sorted_merging=[]

  # # Check between list1 and list2 untill one of them runs out of elements
  # while len(list1) and len(list2):
  #   if list1[0] < list2[0]:
  #     sorted_merging.append(list1.pop())
  #   else:
  #     sorted_merging.append(list2.pop())
  
  # # Then add remaining elements and return list
  # sorted_merging.extend(list1)
  # return sorted_merging.extend(list2)

  # Note: the solution above is kind of cute, but unforunately list.pop(0)
  # is not constant time with the standard python list implementation, so
  # the above is not strictly linear time.
  # An alternate approach uses pop(-1) to remove the endmost elements
  # from each list, building a solution list which is backwards.
  # Then use reversed() to put the result back in the correct order. That
  # solution works in linear time, but is more ugly.

  while len(list1) and len(list2):
    # changes in the operator because running backwards you look to add the highers and then at the end, reverse its order
    if list1[-1] < list2[-1]:
      sorted_merging.append(list2.pop(-1))
    else:
      sorted_merging.append(list1.pop(-1))
  # Then add remaining elements and return list
  while len(list1):
    sorted_merging.append(list1.pop(-1))
  while len(list2):
    sorted_merging.append(list2.pop(-1))

  sorted_merging.reverse()
  return sorted_merging


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  # test(remove_adjacent([1, 3, 5, 7, 9, 2, 4, 6, 8, 9, 7, 5, 3, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
  test(remove_adjacent([1, 3, 5, 7, 9, 2, 4, 6, 8, 9, 7, 5, 3, 1]), [1, 3, 5, 7, 9, 2, 4, 6, 8])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
