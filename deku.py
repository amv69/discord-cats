import os
import discord
from dotenv import load_dotenv
import time

load_dotenv()
TOKEN = 'NzA5MTc3NTI4NzQ4NjA1NTEx.XriHWg.-TxQFiRBGaZUu9hB_f-vpkfyMxA'

client= discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} connected')

@client.event
async def on_message(message):
    if 'good deku' in message.content.lower():
        time.sleep(1)
        await message.channel.send('prrrrr')
    elif 'bad deku' in message.content.lower():
        time.sleep(1)
        await message.channel.send('hissss')
    elif 'deku' in message.content.lower():
        await message.channel.send('meow')

client.run(TOKEN)
