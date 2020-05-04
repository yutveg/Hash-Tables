test_list = [
  [8, [4]], 
  [[90, 91], -1, 3], 
  [9, 62], 
  [[-7, -1, [-56, [-6]]]], 
  [201], 
  [[76, 0], 18],
]
total = 0
for sub_array in test_list:
    
    total += min(sub_array)

print(total)