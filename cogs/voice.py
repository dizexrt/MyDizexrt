from discord import voice_client
from discord.ext import commands
from dizexrt.voices import TTS_Source

class MusicCommand(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases = ['say', 'speak', 'talk', 'tts'])
    async def gtts(self, ctx, text:str):
        join = await ctx.bot.voice.join(ctx)
        if not join:return

        source = TTS_Source(text)
        voice_client.play(source)
    
    @commands.command(aliases = ['p', 'play', 'search'])
    async def music_search(self, ctx, query:str):
        await ctx.alert(query)

def setup(client):
    client.add_cog(MusicCommand(client))