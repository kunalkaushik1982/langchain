import ollama
topic='india'
#response = ollama.chat(model="llama3", messages=[{"role": "user", "content": "Your message"}])
response=ollama.chat(model="llama3", messages=[{"role": "user", "content": f"Write a poem about {topic} for a 5-year-old child."}])
print(response.message.content)


