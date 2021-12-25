import discord
from discord.ext.commands.flags import F
from gtts import gTTS

__all__ = (
    'TTS_Source',
    'Voice',
)

class Voice:

    def __init__(self, client) -> None:
        self.client = client

    async def join(self, ctx):

        if ctx.author.voice is None:
            await ctx.alert('You have to join voice channel first!')
            return False
        
        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()
            await ctx.alert(f'{self.client.user.name} has joined voice channel {ctx.voice_client.channel.mention} now')
            return True
        
        if ctx.voice_client.channel == ctx.author.voice.channel:
            return True
        
        if len(ctx.voice_client.channel.members) > 1:
            await ctx.alert(f'{self.client.user.name} has already joined voice channel with others')
            return False
        
        if len(ctx.voice_client.channel.members) == 1:
            await ctx.voice_client.move_to(ctx.author.voice.channel)
            ctx.alert(f'{self.client.user.name} is moved to voice channel {ctx.voice_client.channel.mention}')
            return True
    
class TTS_Source(discord.FFmpegPCMAudio):

    def __init__(self, text:str):
        self.path = 'dizexrt/voice/source/tts.mp3'
        self.extract(text)
        super().__init__(self.path)

    def extract(self, text:str):
        tts = gTTS(text, lang = 'th')
        tts.save(self.path)