# 1. Write a Python program to count the occurrences of each word in a
#  given sentence string = """To change the overall look of your document. To change the look available in the gallery"""


# string = """To change the overall look of your document. To change the look available in the gallery"""

# words = string.split()
# wordCount = {}

# for word in words:
#     if word in wordCount:
#         wordCount[word] += 1
#     else:
#         wordCount[word] = 1

# print(wordCount)


# 2.Write a Python program to remove a newline in Python
#  String = "\nBest \nDeeptech \nPython \nTraining\n"

# str = "\nBest \nDeeptech \nPython \nTraining\n"

# newStr = str.replace("\n", "")

# print(newStr)


# 3. Write a Python program to reverse words in a string
#  String = “Deeptech Python Training”

# string = "Deeptech Python Training"

# rev = ""

# for i in string:
#     rev = i + rev
# print(rev)


# 5.Write a Python program to count and display the vowels of a given text
#  String=”Welcome to python Training

# str = "Welcome to python Training"

# vowels = "aeiouAEIOU"

# vowels_count = 0

# print("vowels in the given string:")
# for v in str:
#     if v in vowels:
#         print(v, end="")
#         vowels_count += 1


# print(f"\nNumber of vowels: {vowels_count}")

#!list lab

#!  1.write a python program to sum all items in a list

# list_itmes = [1, 3, 6, 7]
# sum_list = 0

# for i in list_itmes:
#     sum_list += i


# print("sum of all list items: ", sum_list)


#! 2.write a python program to get the smallest and largest number without using builtin function

# list_items = [11, 13, 6, 7]
# smallest = list_items[0]
# largest = list_items[0]

# for i in list_items:
#     if i < smallest:
#         smallest = i

#     if i > largest:
#         largest = i


# print("smallest", smallest)
# print("largest", largest)

#! 3. write a python program to find duplicate values from a list and display those

# list_items = [1, 3, 4, 1, 4, 6, 7, 9, 10]

# duplicate_items = []

# for i in range(len(list_items)):
#     for j in range(i + 1, len(list_items)):
#         if list_items[i] == list_items[j]:

#             if list_items[i] not in duplicate_items:
#                 duplicate_items.append(list_items[i])

# print("Duplicate value:", duplicate_items)


#! 4.Write a Python program to split a given list into two parts where the length of the first part of the list is given. Original list: [1, 1, 2, 3, 4, 4, 5, 1] Length of the first part of the list: 3 Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])

# list_items = [1, 1, 2, 3, 4, 4, 5, 1]


# n = int(input("Enter the length of the first part of the list: "))

# # Split the list into two parts
# first_part = list_items[:n]
# second_part = list_items[n:]


# print("Splitted the list into two parts:", (first_part, second_part))


#! 5.Write a Python program to traverse a given list in reverse order, and print the elements with the original index. Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order: black white green red

# original_list = ["red", "green", "white", "black"]

# # Print reversed elements
# for element in reversed(original_list):
#     print(element)

# set lab
#! 1.Write a Python program to Get Only unique items from two sets.
#  Input:
#  set1 = {10, 20, 30, 40, 50}
#  set2 = {30, 40, 50, 60, 70}
#  Output:
#  {70, 40, 10, 50, 20, 60, 30}


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_items = set1.union(set2)
# print("Unique items from both sets:", unique_items)

#! 2.Write a Python program to Return a set of elements present in Set A or B, but not both.
#  Input:
#  set1 = {10, 20, 30, 40, 50}
#  set2 = {30, 40, 50, 60, 70}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

setSymmetricDifference = set1.symmetric_difference(set2)

# print(setSymmetricDifference)


#! 3. Write a Python program to Check if two sets have any elements in common. If
#  yes, display the common elements.
#  Input:
#  set1 = {10, 20, 30, 40, 50}
#  set2 = {60, 70, 80, 90, 10}


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

setIntersection = set1.intersection(set2)
# print(setIntersection)


#! 4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

setZ = set1.intersection(set2)
print(setZ)
