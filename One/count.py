import numpy as np

def counter(differences):
  count = 0
  for diff in differences:
     if diff>0:
        count=count+1
  return count

#FIRST PROBLEM
array_from_file = np.genfromtxt("input", dtype=int)
differences = array_from_file[1:]-array_from_file[:-1]
print('First answer is ',counter(differences))

#SECOND PROBLEM
i = 0
sum_bunches = []
while i in range(array_from_file.size):
   groups = array_from_file[i:i+3:1]
   sum_bunches.append(sum(groups))
   i=i+1
sum_bunches = np.array(sum_bunches)
differences_sum_bunches = sum_bunches[1:]-sum_bunches[:-1]
print('Second answer is ',counter(differences_sum_bunches))
