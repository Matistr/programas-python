import openai
import config

openai.api_key=config.api_key

content=input("¿Sobre qué quieres hablar?\n")


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=1,
    messages=[{"role":"user",
              "content":content}])

print(response)