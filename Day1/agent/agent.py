import json


# TOOL: Read private student data
def read_student_data():
   with open("Day1/data/student_data.json", "r") as file:
        return json.load(file)


# TOOL: Find the most urgent assignment
def find_urgent_assignment():
    data = read_student_data()

    urgent = min(
        data["subjects"],
        key=lambda subject: subject["due_days"]
    )

    return urgent


print("=== AI AGENT (LOCAL SIMULATION) ===")
print()

user_question = "What should I study first?"

print("User:", user_question)
print()

# AGENT LOOP
print("Agent: I need to check the student's private data.")
print()

# Agent selects a tool
tool_name = "find_urgent_assignment"

print("Agent selected tool:", tool_name)
print()

# Tool is executed
if tool_name == "find_urgent_assignment":
    result = find_urgent_assignment()

# Agent receives the tool result
print("Tool result:")
print(result)
print()

# Agent gives final answer
print("Final Answer:")
print(
    "You should study",
    result["name"],
    "first because the assignment",
    result["assignment"],
    "is due in",
    result["due_days"],
    "day(s)."
)