import os
import discord
from dotenv import load_dotenv
from Server import Server

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # Fill in this. This is the generated token for your bot from the Discord Developer Page

# Before that, You have to enable message intent for the bot from "Discord Dev Portal"
intent = discord.Intents.default()
intent.members = True
intent.message_content = True
client = discord.Client(intents = intent)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')     
   
   
@client.event
async def on_message(message):
    if message.author == client.user:
       return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
#Server()        
client.run(TOKEN)