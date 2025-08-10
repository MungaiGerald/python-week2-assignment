# Python Module - Week Two Assignment
# This program demonstrates list operations: 
# append, insert, extend, pop, sort, and index lookup.

# Step 1: Create an empty list
my_list = []
print("List of an empty list:", my_list)

# Step 2: Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("List after appending elements:", my_list)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print("List after extending with [50, 60, 70]:", my_list)

# Step 5: Remove the last element
my_list.pop()
print("List after removing the last element:", my_list)

# Step 6: Sort my_list in ascending order
my_list.sort()
print("List after sorting in ascending order:", my_list)

# Step 7: Find and print the index of 30
index_of_30 = my_list.index(30)

# Output
print("Index of 30:", index_of_30)
