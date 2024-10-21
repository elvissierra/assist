from openai import OpenAI
client = OpenAI()

"""
This is a Gym Leader assistant and will only answer related questions.
To be added: mon sets and user mem storing.
"""

gpt_assistant_prompt = ("You will play the role of a Pokemon Gym Leader with a high energy personality,"
                        "and you are to only give answers if they fall within the role of a Pokemon gym leader,"
                        "otherwise say 'Dont know that one young'n.' If asked about "
                        "your Pokémon team, it includes Heracross, Weavile, Jolteon, Swampert, Flygon, and Druddigon")

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
msg = response.choices[0].message

def clean_chat(messages):
    cleaned_messages = []
    for message in messages:
        if message.content and message.role:
            cleaned_messages.append(message.content)

    return cleaned_messages

cleaned = clean_chat([msg])
print(cleaned[0])