import itertools as it

transactions = [
    "MONKEY",
    "DONKEY",
    "MAKE",
    "MUCKY",
    "COKE"
]

items = set.union(*[set(t) for t in transactions])

def support(*item):
    return sum([1 for t in transactions if set(item).issubset(set(t))])

for k in range(1, len(items)+1):
    for item in it.combinations(items, k):
        sup = support(*item)
        if sup >= 3:
            print(''.join(sorted(item)), sup)
