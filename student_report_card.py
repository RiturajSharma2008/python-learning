student_details = {
    "name": "Rituraj",
    "age": 18,
    "student_id": "S12345",
}

scores_rituraj = {
    "Mathematics": 85,
    "Physics": 90,
    "Chemistry": 85,
    "English": 89,
    "Computer Science": 90,
}

total_score = sum(scores_rituraj.values())

average_score = total_score / len(scores_rituraj)

highest_subject = max(scores_rituraj, key=scores_rituraj.get)

lowest_subject = min(scores_rituraj, key=scores_rituraj.get)

if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"--------------------------------------------------------------------------------")
print(f"Student Name: {student_details['name']}")
print(f"Age: {student_details['age']}")
print(f"Student ID: {student_details['student_id']}")
print(f"--------------------------------------------------------------------------------")
for score in scores_rituraj:
    print(f"{score}: {scores_rituraj[score]}")
print(f"--------------------------------------------------------------------------------")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Highest Score: {highest_subject} ({scores_rituraj[highest_subject]})")
print(f"Lowest Score: {lowest_subject} ({scores_rituraj[lowest_subject]})")
print(f"Grade: {grade}")
print(f"--------------------------------------------------------------------------------")