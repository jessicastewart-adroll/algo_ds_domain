from collections import Counter, defaultdict

def print_anagramic_pairs(string):
	counts = defaultdict(int)
	for i in range(len(string)):
		for j in range(i+1, len(string)+1):
			key = frozenset(Counter(string[i:j]).items())
			counts[key] += 1

	print(counts)
	
# n = int(input())
# strings = [input() for i in range(n)]
#tests = ['abba', 'abcd', 'ifailuhkqq', 'hucpoltgty', 'ovarjsnrbf', 'pvmupwjjjf', 'iwwhrlkpek']
tests = ['abba']
for string in tests:
    print_anagramic_pairs(string)
