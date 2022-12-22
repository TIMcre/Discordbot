import discord
import youtube_dl
import os
import ffmpeg


# Create the Client object with the intents parameter
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)
token = open('token.txt').read()

@client.event
async def on_ready():
    print("Logged in as", client.user)

@client.event
async def on_message(message):
    global voice_client

    if message.content.startswith("!join"):
        # Join the voice channel
        channel = message.author.voice.channel
        await channel.connect()
    
    elif message.content.startswith("!play"):                      
        # Split the command and its arguments
        command, *args = message.content.split()
        print(command, *args)
        try:
            # Get the first argument (the audio source)
            audio_source = args[0]
        except:
            await message.channel.send("couldnt find a audio source")      
        
        # Use FFmpeg to play the audio file
        voice_client = client.voice_clients[0]
        voice_client.pause()
        voice_client.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=audio_source))
        await message.channel.send("Playing song...")

    elif message.content.startswith("!pause" or "!p"):
        try:
            voice_client.pause()
            await message.channel.send("pausing")
        except:
            await message.channel.send("Unabel to pause")

    elif message.content.startswith("!resume" or "!r"):
        try:
            voice_client.resume()
            await message.channel.send("resuming")
        except:
            await message.channel.send("Unabel to resume")

    elif message.content.startswith("!leave"):
        
        await voice_client.disconnect()
        await message.channel.send("left")
        



client.run(token)