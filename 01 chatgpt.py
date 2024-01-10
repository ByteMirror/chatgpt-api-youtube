from openai import OpenAI

client = OpenAI(api_key="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")


completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "I want you to only write down 3 random Pokemon names in markdown format. Print only the names, one in each line. No fat text, and nothing else. Each name should have a - in front so that it is a bullet list"}])
print(completion.choices[0].message.content)