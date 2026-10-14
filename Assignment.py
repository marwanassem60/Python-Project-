# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
students = ["Marwan", "Ahmed", "Ali", "Tamer", "Youssef"]

print("Student list:")
print(students)
print()

scores = [85, 92, 78, 90, 88]

print("Scores list:")
print(scores)
print()

student_dict = {
    "Marwan": 85,
    "Ahmed": 92,
    "Ali": 78,
    "Tamer": 90,
    "Youssef": 88,
    }

print("Student Dictionary:")
print(student_dict)
print()

students = [
    {"name": "Marwan", "course": "Math", "grade": "A"},
    {"name": "Ahmed", "course": "Physics", "grade": "B"},
    {"name": "Ali", "course": "Chemistry", "grade": "A"},
    {"name": "Tamer", "course": "Biology", "grade": "C"},
    {"name": "Youssef", "course": "Math", "grade": "B"}
]

print("List of Dictionaries")
for student in students:
    print(student)
print()

students = ["Marwan", "Ahmed", "Ali", "Tamer", "Youssef", "Marwan"]
unique_students = list(set(students))
print("Using set():", unique_students)

students = ["Marwan", "Ahmed", "Ali", "Tamer", "Youssef"]
scores = [85, 92, 78, 90, 88]
print("Using range()")
for i in range(len(students)):
    print(f"{students[i]} - {scores[i]}")
print()


scores = [85, 92, 78, 90, 88,]
high_scores = [score for score in scores if score > 80]

print("scores:", scores)
print("Scores greater than 80:", high_scores)

scores = [85, 92, 78, 90, 88,]
total_score = sum(scores)
average_score = total_score / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

print("Scores:", scores)
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")

score_input = input("Enter a score: ")

if score_input.isdigit():
    score = int(score_input)
    print(f"You entered: {score}")
else:
    print("Invalid Input")


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
score = 85
grade = get_grade(score)
print(f"Score: {score} -> Grade: {grade}")    







