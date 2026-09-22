import json

# Read the student's private data
with open("../data/student_data.json", "r") as file:
    data = json.load(file)

subjects = data["subjects"]

print("=== Rule-Based Workflow ===")
print()

# Predefined rule
for subject in subjects:
    if subject["due_days"] == 0:
        print("Study first:", subject["name"])
        print("Assignment:", subject["assignment"])
        break
