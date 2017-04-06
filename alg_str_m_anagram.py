from collections import Counter, defaultdict

def print_anagramic_pairs(string):
	counts = defaultdict(int)
	for i in range(len(string)):
		for j in range(i+1, len(string)+1):
			key = frozenset(Counter(string[i:j]).items())
			counts[key] += 1

	total = 0
	for count in counts.values():
		total += (count*(count-1))//2

	print(total)	
	
# n = int(input())
# strings = [input() for i in range(n)]
# 4 0 3 2 2 6 3
tests = ['abba', 'abcd', 'ifailuhkqq', 'hucpoltgty', 'ovarjsnrbf', 'pvmupwjjjf', 'iwwhrlkpek']
for string in tests:
    print_anagramic_pairs(string)
