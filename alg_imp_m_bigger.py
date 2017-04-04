def next_lexographical_permutation(string):
	i = len(string)-1
	pivot = -1

	while i > 0:
		if string[i] > string[i-1]:
			pivot = i-1
			break
		i -= 1

	if pivot < 0:
		return 'no answer'
		return

	j = pivot+1
	successor = None
	while j < len(string):
		if string[j] > string[pivot]:
			if not successor:
				successor = j
			else:
				if string[successor] >= string[j]:
					successor = j
		j += 1
	
	string[pivot], string[successor] = string[successor], string[pivot]

	start = pivot+1
	end = len(string)-1

	while start < end:
		string[start], string[end] = string[end], string[start]
		start += 1
		end -= 1

	return string	


def next_lexographical_increase(string):
	parsed_input = [ord(c) for c in list(string)]
	result = next_lexographical_permutation(parsed_input)

	if result == 'no answer':
		print(result)
	else:
		print(''.join([chr(i) for i in result]))


test_count = int(input())
tests = [input() for i in range(test_count)]
for test in tests:
	next_lexographical_increase(test)
