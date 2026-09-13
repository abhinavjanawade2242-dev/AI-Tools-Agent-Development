import ollama
question=input("Ask something:")
response=ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":f""""
You are a tool seection assistant.

Available Tools:

1. calculator
2 python
3 file_reader

Choose the most appropriate tool for the users request.format.format. 

user request:
{question}

Return only the tool name. 
"""
        }
    ]
)
print("Selected Tool:",response["message"]["content"])