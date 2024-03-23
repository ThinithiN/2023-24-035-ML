import openai

# Set your OpenAI API key
openai.api_key = "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"

messages = [ {"role": "system", "content":"You are a intelligent assistant."} ]

def ask_from_gpt(user_msg):

    message = user_msg
    if message:
        messages.append({"role": "user", "content": message},)

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)


    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    return reply

