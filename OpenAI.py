import openai
openai.api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages = [
                {"role": "system", "content" : "Complete the following code."},
                {"role": "user", "content" : "def fibonacci(num):"}
             ]
)

print(completion)
