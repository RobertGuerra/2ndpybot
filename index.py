# index.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_read():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        
    
    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.anem}(id: {guild.id})'
    )

client.run(TOKEN)
