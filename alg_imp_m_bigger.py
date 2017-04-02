def next_bigger_word(word):
	# find smallest value greater than ones
	# order everything after smallest to largest

	end = len(word)-1
	word_nums = [ord(c) for c in word]
	i = 0

	# first case
	while i < end:
		if word_nums[end] > word_nums[i]:
			word_nums[i] > word_nums[end]
			print(''.join([chr(n) for n in word_nums]))
			return
		i += 1

	# second case
	i = 0
	smallest = -1
	while i < end:
		if i <
	
	# third case	
	print('no answer')

tests = ['ab', 'bb', 'hefg', 'dhck', 'dkhc']
for test in tests:
	next_bigger_word(test)	

# swap points -> 0, none, 2, 2, 0
