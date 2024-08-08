#Learning git

from collections import defaultdict, Counter

list_example = ["apple", "banana", "apple"]
appearance_of_elements = Counter(list_example)
# Allows to count how many times each element appeared in a collection
# Counter(collection)
print(appearance_of_elements)

dict_example = defaultdict(int)
print(dict_example["A"])
#By using default dict, we do not get error even if the key does not point to any value. Emulates default value
dict_example["A"] = "First letter of alphabet"
#Then, we can easily change its default value
print(dict_example["A"])

