# Example in Python
student_grades = [65, 45, 85, 92, 78, 90, 88]
print(student_grades)

# # Calculate Average Grade
average_grade = sum(student_grades) / len(student_grades)
print(f"the average grade is: {average_grade}")

# # Find the Highest Grade
highest_grade = max(student_grades)
print(f"the highest_grade is: {highest_grade}")
# # Identify Students Needing Improvement
students_needing_improvement = [index + 1 for index, grade in enumerate(student_grades) if grade < 70]
print(f"students needing improvement: {students_needing_improvement}")
# # Add a New Student
student_grades.append(95)
print(student_grades)
# # Update a Grade
student_grades[2] = 80
print(student_grades)
