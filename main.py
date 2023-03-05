import openai
import config
import sys

#APIキーセット
openai.api_key = config.API_KEY

args = sys.argv

global question
global messageHistory

if(len(args) < 2):
    print("System > 質問文を入力してください")
    quit()

# 引数で引き受けた質問文をセット
question = args[1]

# インタラクション保存変数
messageHistory=[
    
    # ChatGPTの前提条件セット
    {
        "role": "system",
        "content": "日本語で返答してください。"
    }
]

while True:
    if(question == ""):
        question = input("Me > ")

    # 質問をインタラクション変数に追加
    messageHistory.append({"role": "user", "content": question})
    
    chatInfos = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messageHistory,
        )
    answer = chatInfos["choices"][0]["message"]["content"]
    question = ""

    # 回答をインタラクション変数に追加
    messageHistory.append({"role": "assistant", "content": answer})

    #トークン数を確認し会話情報の削除の有無を実施
    token = chatInfos["usage"]["total_tokens"]
    if(token > 2000):
        messageHistory.pop(1)
        messageHistory.pop(1)
        
    print(f"ChatGPT > {answer}")
    print("\n")
