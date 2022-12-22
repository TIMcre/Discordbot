import discord
import requests
import ast  
import random 

url = "https://goquotes-api.herokuapp.com/api/v1/random?count=1"

ourwords = ["our", "we", "everybody", "everyone", "all of us", "every person", "each and every one", "each one", "each person", "every last one", "one and all", "all and sundry", "the whole world"]

token = open('token.txt').read()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_text():
    response = requests.request("GET", url)
    response = ast.literal_eval(response.text)
    response = response["quotes"]
    response = ast.literal_eval(str(response[0]))
    text = response["text"]
    author = response["author"]
    author = f"-{author}"
    return text, author

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ("!quote"):
        text = get_text()
        await message.channel.send(text[0])
        await message.channel.send(text[1])

    if any(word in message.content.lower() for word in ourwords):
        await message.channel.send("https://tenor.com/view/meme-our-now-gif-21036569")


    #if message.content.lower() == ("haare") or ("bold") or ("hair"):
    #    await message.channel.send("https://tenor.com/view/jim-carey-hai-hi-hello-bald-gif-4763908")
  

client.run(token)