import openai 
import os

# openai.api_key = os.environ['GPT_KEY']
def gpt_response(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=50,
    )
    return print(response.choices[0].text)

def main():
    while True:
        print('GPT: Ask me a question\n')
        myQn = input()
        gpt_response(myQn)

main()