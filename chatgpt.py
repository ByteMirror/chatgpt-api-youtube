from openai import OpenAI

client = OpenAI(api_key="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")


completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "I want you to only write down 3 random Pokemon names in markdown format. Print only the names, one in each line. No fat text, and nothing else. Each name should have a - in front so that it is a bullet list"}])
print(completion)#.choices[0].message.content




# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
#         "role": "assistant"
#       },
#       "logprobs": null
#     }
#   ],
#   "created": 1677664795,
#   "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
#   "model": "gpt-3.5-turbo-0613",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 17,
#     "prompt_tokens": 57,
#     "total_tokens": 74
#   }
# }