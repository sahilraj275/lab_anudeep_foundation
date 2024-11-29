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
# print(string)
# for i in string:
#     rev = i + rev
# print(rev)


# 5.Write a Python program to count and display the vowels of a given text
#  String=”Welcome to python Training

str = "Welcome to python Training"

vowels = "aeiouAEIOU"

vowels_count = 0

print("vowels in the given string:")
for v in str:
    if v in vowels:
        print(v, end="")
        vowels_count += 1


print(f"\nNumber of vowels: {vowels_count}")
