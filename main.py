import os
from dotenv import load_dotenv
from dizexrt import MyClient
import discord

load_dotenv()
token = os.getenv("TOKEN")

client = MyClient(intents = discord.Intents.all())

@client.command()
async def test(ctx):
    await ctx.alert("hello")

@client.slash_command()
async def hello(ctx):
    await ctx.response("Hello world")

'''
for file in os.listdir('cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')
'''

client.run(token)