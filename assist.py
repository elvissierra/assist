import environ
import os
import wandb
from openai import OpenAI
client = OpenAI()

gpt_assistant_prompt = "You're a " + input ("Who am I in this scenario?")
gpt_user_prompt = input ("What prompt am I to do?")
gpt_prompt = gpt_assistant_prompt, gpt_user_prompt
print(gpt_prompt)

message= [{"role": "assistant", "content": gpt_assistant_prompt}, {"role": "user", "content" : gpt_user_prompt}]
temperature = 0.2
max_tokens = 256
frequency_penalty = 0.0

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=message,
    temperature=temperature,
    max_tokens=max_tokens,
    frequency_penalty=frequency_penalty
)
print(response.choices[0].message)
