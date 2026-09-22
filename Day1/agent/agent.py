import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# TOOL 1: Read private student data
def read_student_data():
    with open("../data/student_data.json", "r") as file:
        return json.load(file)


# TOOL 2: Find the most urgent assignment
def find_urgent_assignment():
    data = read_student_data()

    urgent = min(
        data["subjects"],
        key=lambda subject: subject["due_days"]
    )

    return urgent


# Tool definitions given to the LLM
tools = [
    {
        "type": "function",
        "function": {
            "name": "read_student_data",
            "description": "Read the student's private subject, mark, assignment and deadline data.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_urgent_assignment",
            "description": "Find the student's assignment with the nearest deadline.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]


messages = [
    {
        "role": "system",
        "content": """
You are a student study assistant.

You have access to tools that can read the student's private
study data.

Use the tools when the user's question requires private data.
Give a clear final answer after getting the required information.
"""
    },
    {
        "role": "user",
        "content": "What should I study first?"
    }
]


print("=== AI AGENT ===")
print()

# AGENT LOOP
while True:

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools
    )

    message = response.choices[0].message

    # If the LLM wants to use a tool
    if message.tool_calls:

        messages.append(message)

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            print("Agent selected tool:", tool_name)

            if tool_name == "read_student_data":
                result = read_student_data()

            elif tool_name == "find_urgent_assignment":
                result = find_urgent_assignment()

            else:
                result = "Unknown tool"

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                }
            )

    else:
        # LLM has finished the task
        print()
        print("Final Answer:")
        print(message.content)
        break
