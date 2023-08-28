import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "rewrite the sentence 'They said we should go to church'"}
  ]
)

print(completion.choices[0].message)
