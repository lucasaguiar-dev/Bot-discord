from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

load_dotenv()
key_discord = os.getenv("key_discord_lol")
key_lol = os.getenv("key_lol")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
    
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são:\n1 - Não falar sobre o clube da luta')
        elif message.content == '?nivel':
            await message.author.send('Nível 1')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)

client = MyClient(intents=intents)
client.run(f'{key_discord}')