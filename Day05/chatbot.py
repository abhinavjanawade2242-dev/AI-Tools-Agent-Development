import ollama
import json
import os
MEMORY_FILE = "memory.json"
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as file:
        messages = json.load(file)
else:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Remember the conversation and answer based on previous messages."
        }
    ]
print("Local AI Chatbot")
print("Type 'exit' to stop.")
print("Type 'clear' to delete memory.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    if user_input.lower() == "clear":
        messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Remember the conversation and answer based on previous messages."
            }
        ]
        with open(MEMORY_FILE, "w") as file:
            json.dump(messages, file, indent=4)
        print("Memory cleared.\n")
        continue
    messages.append({
        "role": "user",
        "content": user_input
    })
    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )
    ai_response = response["message"]["content"]
    print("AI:", ai_response)
    messages.append({
        "role": "assistant",
        "content": ai_response
    })
    with open(MEMORY_FILE, "w") as file:
        json.dump(messages, file, indent=4)