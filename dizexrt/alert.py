import discord
from discord.ext import commands

class AlertContext(commands.Context):

    async def alert(self, message):
        embed = discord.Embed()
        embed .title = "📢 Bot Alert"
        embed.description = message
        return await self.send(embed = embed)

class MyClient(commands.Bot):

    async def get_context(self, message, *, cls=AlertContext):
        return await super().get_context(message, cls=cls)
    
    async def on_ready(self):
        print(f"Loged in as {self.user}")
        