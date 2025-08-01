# Create different sequence types
lst = [1, 2, 3]  # List
tup = (4, 5, 6)  # Tuple
s = "xyz"       # String

# Play with sequence properties
print(lst[0], tup[0], s[0])  # Index: 1, 4, 'x'
print(lst[1:], s[:2])       # Slice: [2, 3], 'xy'
print(len(lst), len(tup))   # Length: 3, 3
print(2 in lst, 'y' in s)   # Membership: True, True

# Iterate
for i, x in enumerate(lst):
    print(f"Index {i}: {x}")
