#Learning git

from collections import defaultdict, Counter, deque, OrderedDict


'# Create an OrderedDict
ordered_dict = OrderedDict()

# Insert items
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

# Iterate over items
for key, value in ordered_dict.items():
    print(key, value)

# Output:
# a 1
# b 2
# c 3

# Move the last item to the end
ordered_dict.move_to_end('a')
print(ordered_dict)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Move the first item to the start
ordered_dict.move_to_end('c', last=False)
print(ordered_dict)  # Output: OrderedDict([('c', 3), ('b', 2), ('a', 1)])






