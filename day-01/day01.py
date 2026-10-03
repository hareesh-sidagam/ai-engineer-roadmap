# Day 1 - AI Engineer Roadmap
# Topics: AI vs ML vs GenAI vs LLM + Python Basics

# 1. Variables
name = "Harish"
role = "AI Engineer"
experience = 6

print("Name:", name)
print("Target Role:", role)
print("Experience:", experience, "years")


# 2. List
skills = [
    "Python",
    "Node.js",
    "Angular",
    "AWS",
    "GenAI"
]

print("\nMy skills:")
for skill in skills:
    print("-", skill)


# 3. Dictionary
ai_concepts = {
    "AI": "Machines performing tasks that require human intelligence",
    "ML": "Systems that learn patterns from data",
    "GenAI": "AI that generates new content",
    "LLM": "Large language models for understanding and generating language"
}

print("\nAI Concepts:")
for concept, meaning in ai_concepts.items():
    print(f"{concept}: {meaning}")


# 4. Function
def introduce(name, role):
    return f"{name} is preparing for an {role} role."


message = introduce(name, role)
print("\n" + message)


# 5. Simple condition
learning_hours = 1

if learning_hours >= 1:
    print("🔥 Day 1 learning goal completed!")
else:
    print("Keep learning!")