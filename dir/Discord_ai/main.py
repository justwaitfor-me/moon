from requests import post
import subprocess
import discord

token = 'MTExMTY0MTE2MjU1ODczODQ0Mg.G8A8dU.lWCVUfVVwMG1ItJKWcccod7qfYxD5lZu7SNR2Y'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
   print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.guild is not None and message.channel.name == 'Allgemein':
        subprocess.Popen(["python", "retro.py"])
        if 'hello' in message.content:
            await message.channel.send('Hello World!')
        elif 'hallo' in message.content:
            await message.channel.send('Hallo Welt!')
        elif '/mod.kill=bot' in message.content:
            await message.channel.send('Killing Bot...')
            import sys
            sys.exit()

client.run(token)
