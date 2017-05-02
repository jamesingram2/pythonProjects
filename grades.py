# Create dictionaries of students and their names, homework grades, quiz grades, and test grades
# for Python 2.7

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Create function to determine average
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

# Create function to get weighted average for student
def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    test = average(student['tests'])
    return (.10 * homework)+(.30 * quizzes)+(.60 * test) 

# Create function to convert average to letter grade
def get_letter_grade(score):
    if score >= 90 : return "A"
    elif score >= 80 : return "B"
    elif score >= 70 : return "C"
    elif score >= 60 : return "D"
    else : return "F"

# Print grade for Lloyd
print get_letter_grade(get_average(lloyd))

# Create function to get class average
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

# Print class average
students = [lloyd, alice, tyler]
print get_class_average(students)

# Print class letter grade
print get_letter_grade(get_class_average(students))