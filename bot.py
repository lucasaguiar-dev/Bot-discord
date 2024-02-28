import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

load_dotenv()
key = os.getenv("key")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))
    
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são:\n1 - Não falar sobre o clube da luta')

client = MyClient(intents=intents)
client.run(f'{key}')