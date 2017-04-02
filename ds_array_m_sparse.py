from collections import defaultdict

n = int(input())
strings = [input() for i in range(n)]
q = int(input())
queries = [input() for i in range(q)]

# build lookup
lookup = defaultdict(lambda: 0)
for string in strings:
    lookup[string] += 1
    
# print with default
for query in queries:
    print(lookup.get(query, 0))
    
# big O = N + Q    
