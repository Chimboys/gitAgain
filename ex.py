#Learning git

from collections import defaultdict, Counter, deque

''' Counter , instead of creating dict and the iterate list, just use COUNTER'''
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


''' Time for deque in py , its Double-Ended queue (that is why deque (double ended queue)
    Add and Remove in both LIFO AND FIFO'''

basic_list = deque([1,2,3])
basic_list.appendleft(-1) #adding element in the beginning
basic_list.append(4) #adding element to the top, as the last element
last_element = basic_list.pop() #removes last element and returns it
first_element = basic_list.popleft() #removes fitst element and returns it
print(first_element, last_element, basic_list)
#Additional features of deque
basic_list.extend([5, 6])          # Add elements to the right end
basic_list.extendleft([-3, -2])    # Add elements to the left end

basic_list.rotate(2)  # Rotate two steps to the right
print(basic_list)     # deque([5, 6, -2, -3, 1, 2, 3])

basic_list.rotate(-1) # Rotate one step to the left
print(basic_list)     # deque([6, -2, -3, 1, 2, 3, 5])






