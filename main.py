import openai
import config
import sys

#APIキーセット
openai.api_key = config.API_KEY

args = sys.argv

if(len(args) <= 2):
    print("質問文を入力してください")
    quit()

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "日本語で返答してください。"
            },
        {
            
            "role": "user",
            "content": f"{args[1]}"
            },
        ],
    )
print(res["choices"][0]["message"]["content"])