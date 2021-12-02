f = open("input.txt",'r')
lines = f.readlines()
horizontal = 0
depth = 0
aimed_depth = 0
aim = 0
for x in lines:
   direction = x.split(' ')[0]
   value = int(x.split(' ')[1])
   if direction=='forward':
     horizontal=horizontal+value
     aimed_depth=aimed_depth+aim*value
   elif direction=='up':
     depth=depth-value
     aim=aim-value
   elif direction=='down':
     depth=depth+value
     aim=aim+value

print('Horizontal pos is ',horizontal, 'depth is ',depth, 'aimed_depth is ',aimed_depth)
print('Frist answer is ',horizontal*depth)
print('Second answer is ',horizontal*aimed_depth)
