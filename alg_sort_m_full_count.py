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
    
n = int(input())
inputs = [input() for i in range(n)]
values = []

for i in inputs:
    order, val = i.split(' ')
    values.append([int(order), val])
    
def print_in_order(inputs):
	store = [[] for x in range(len(inputs))]
	for i, value in enumerate(inputs):
		store[value[0]].append(i)
	mid = len(inputs)//2

	result = []
	for order in store:
		for position in order:
			if position < mid:
				result.append('-')
			else:
				result.append(inputs[position][1])	

	print(' '.join(result))

print_in_order(values)
