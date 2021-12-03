import numpy as np
f = np.genfromtxt('input.txt',dtype=str)
bit_count = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
for x in f:
   i = 0
   while i in range(len(x)):
      if x[i] == '1':
         bit_count[i]+=1
      i=i+1
print(bit_count)

gamma   = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
epsilon = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
i=0
while i in range(len(bit_count)):
   if bit_count[i]>500:
      gamma[i] = 1
   else:
      epsilon[i] = 1
   i=i+1

gamma_str = ''
epsilon_str = ''
for x,y in zip(gamma,epsilon):
    gamma_str=gamma_str+str(x)
    epsilon_str=epsilon_str+str(y)
print('First answer is ',int(gamma_str,2)*int(epsilon_str,2))
