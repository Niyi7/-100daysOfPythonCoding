import random

# List comprehension for numbers in calculation
numbers = [1, 2, 3]
new_number = [n + 1 for n in numbers]
print(new_number)  # type: ignore

# List comprehension for words
name = "Godspeed"
letters_list = [letter for letter in name]
print(letters_list)

# List comprehension for Range
num_range = range(1, 5)
new_range = [2 * n for n in num_range]
print(new_range)

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

# First Exercise - Squared Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_number = [n**2 for n in numbers]
print(squared_number)

# Second Exercise - Even numbers of the Squared Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]
print(result)

# Third Exercise - Comparing two files together and printing out the common numbers there
first_file = open("file1.txt", "r").readlines()
second_file = open("file2.txt", "r").readlines()

result = [int(item) for item in first_file if item in second_file]
print(result)

# Dictionary Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {scores: random.randint(0, 100) for scores in names}
print(student_scores)

passed_students = {
    names: scores for (names, scores) in student_scores.items() if scores > 59
}
print(passed_students)

# First Exercise - Create a new dictionary by splitting the words in a sentence and add up each words
sentence = "Mary Alison is a very good singer, she went to the Grammy Award Ceremony like a boss"
results = {words: len(words) for words in sentence.split()}
print(results)

# Second Exercise - create a dictionary that takes the weather forecast in celsius of an existing dictionary and converts that it to fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# Iterating over a Pandas DataFrame
student_dict = {"students": ["Angela", "James", "Lilly"], "scores": [56, 76, 98]}

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)
for index, row in student_data_frame.iterrows():
    if row.students == "Angela":
        print(row.scores)
