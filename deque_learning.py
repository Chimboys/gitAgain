from collections import deque

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

