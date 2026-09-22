# Day 1 - Analysis

## Scenario

The selected scenario is a Student Personal Study Assistant.

The system uses student data containing subjects, marks, assignments and
assignment deadlines.

## 1. Plain Chatbot

The plain chatbot gives a predefined conversational response.

It does not directly access the student's private JSON data and does not
use external tools.

It is suitable for simple conversational responses.

## 2. Rule-Based Workflow

The rule-based workflow reads the student data and follows a predefined rule.

If an assignment has 0 days remaining, the workflow selects that assignment
as the priority.

It is predictable and works well for fixed tasks.

## 3. AI Agent

The AI agent demonstrates the basic agent architecture:

Decision-making + Tools + Loop

The agent selects a tool called `find_urgent_assignment`.

The tool reads the private student data and finds the assignment with the
nearest deadline.

The agent then uses the tool result to produce a final answer.

This implementation is a local simulation because an external LLM API key
was not available during development.

## Comparison

| Feature | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Uses predefined rules | No | Yes | Partly |
| Uses private data | No | Yes | Yes |
| Tool usage | No | Fixed operations | Tool selection |
| Flexibility | Medium | Low | High |
| Multi-step tasks | Limited | Predefined | Can support multiple steps |
| Predictability | Medium | High | Medium |
| External LLM required | No | No | Real deployment: Yes |

## Suitability

### Plain Chatbot

Useful for general conversation and simple questions.

### Rule-Based Workflow

Useful when the task has clear and fixed conditions.

### AI Agent

Useful for flexible tasks where the system needs to select tools,
access information and perform multiple steps.

## Conclusion

A plain chatbot mainly generates responses.

A rule-based workflow follows predefined conditions.

An AI agent combines decision-making with tools and an execution loop.

The three approaches are useful for different types of problems.