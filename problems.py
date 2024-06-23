# file for doing problems 

# Problem 1: Counting Word Frequencies

# Description: Given a string of text, create a dictionary that counts the frequency of each word. Ignore punctuation and treat words as case-insensitive.

# string = "Throughout heaven and earth, I alone am the Honoured one"
# 
# punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
# 
# string = string.lower()
# for i in string:
#     if i in punc:
#         string = string.replace(i, "")
# 
# word_amount = {}
# 
# words = string.split()
# for i in words:
#     if i in word_amount:
#         word_amount[i] +=1
#     else:
#         word_amount[i] = 1
# 
# for k,v in word_amount.items():
#     print(f"{k}: {v}")
# 
# 
# 

# problem 2:

#student grades management

grade_book = {}
scores = []

stu_name = input("what is your name?: ")
math = int(input("what was your math score: "))
chem = int(input("what was your chem grade: "))
bio = int(input("what was your bio grade: "))

scores.append(math)
scores.append(chem)
scores.append(bio)

grade_book[stu_name] = scores

for stu, score in grade_book.items():
    avg_grade = sum(score) / len(score)
    print(f"{stu} average score is {avg_grade: .2f} ")


# corrections, using an infinite loop to add multiple students at the same time, and then typing 'done' to exit out the loop