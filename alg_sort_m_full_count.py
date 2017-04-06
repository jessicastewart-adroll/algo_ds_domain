'''
[[0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [4, 'ij'], [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [0, 'ij'], [4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'], [4, 'is'], [2, 'to'], [4, 'the']]
print values in order
BUT don't print first half of ORIGINAL array
stable sort
'''
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
