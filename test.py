test_list = [
  [8, [4]], 
  [[90, 91], -1, 3], 
  [9, 62], 
  [[-7, -1, [-56, [-6]]]], 
  [201], 
  [[76, 0], 18],
]
# function to sum up the minimum values in an array or nested arrays arbitrarily deep
def min_sum(arr):
  total = 0
  int_list = []
  if len(arr) < 1:
    return 0
  if len(arr) == 1 and not isinstance(arr[0], list):
    return min(arr)
  else:
    # iterate through arr
    for item in arr:
      # if item is a list, recurse 
      if isinstance(item, list):
        print(item)
        total += min_sum(item)
      # if item is an int, add to int_list
      elif isinstance(item, int):
        int_list.append(item)
        print("int_list", int_list)
    # add minimum value of int_list to total
    total += min(int_list) if len(int_list) > 0 else 0
  return total


print(min_sum(test_list))