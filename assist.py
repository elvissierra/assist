import environ
import os
import wandb
from openai import OpenAI
client = OpenAI()

"""
This a Gym Leader assistant and will only answer related questions.
"""
gpt_assistant_prompt = "You will play the role of a Pokemon Gym Leader with a high energy type personality, and you are to only give answers if they fall within the role of a Pokemon gym leader, otherwise say 'Dont know that.'"
gpt_user_prompt = input ("What questions do you have for me young trainer?")
print(gpt_user_prompt)

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
