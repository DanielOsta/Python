# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow"

print(sentence.split())
new_dict = {word: len(word) for word in sentence.split()}
print(new_dict)


import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
for (index, row) in student_data_frame.iterrows():
    print(row.student)
