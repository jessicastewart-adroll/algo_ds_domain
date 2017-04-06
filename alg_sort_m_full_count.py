n = int(input())
inputs = [input() for i in range(n)]
values = []

for i in inputs:
    order, val = i.split(' ')
    values.append([int(order), val])
    
positions = [[]]*n    
for i, value in enumerate(values):
    positions[value[0]].append(i)
    
print(positions)    
