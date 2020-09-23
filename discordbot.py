# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzU3NTU4MTU0NjI3MzgzMzk3.X2iJAg.kmRXpKG5oxCfYZkts_bFxli0WTc'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    elif message.content == '/sutehage':
        await message.channel.send('おはようございやーーーーーーーーす^^')

    elif message.content == '/nagusamete':
        await message.channel.send('今日も頑張れ')

    elif message.content == '/studyrand':
        messages = ['微積', '線形代数', '数列', '常微分方程式', 'Toefl', 'atcoder', '途中のやつ実装しろ']
        message_ = random.choice(messages)
        if message_ != "途中のやつ実装しろ":
            counter = random.randint(1,6)
            await message.channel.send(message_ + str(counter) + "問")
        else:
            await message.channel.send(message_)
    
    elif message.content == "/!lang":
        messages = ['python3', 'C', 'C++', 'java', 'ruby', 'javaScript', 'Go']
        message_ = random.choice(messages)
        await message.channel.send("言語 : "+ message_)

    elif message.content == "やだ":
        await message.channel.send('頑張って。')

    elif message.content == "めんどくさい" or message.content == "面倒" or message.content == "面倒くさい":
        await message.channel.send('手を動かせ。')

    elif message.content == "おわった":
        await message.channel.send('お疲れ〜^^')

    elif message.content == "ma":
        await message.channel.send("mi")
    
    # else :
        # await message.channel.send('やれ')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
