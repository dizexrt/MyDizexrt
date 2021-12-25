import discord
from discord.ext.commands import Bot
from discord.commands import ApplicationContext
from dizexrt import db

class AlertContext(ApplicationContext):

    async def alert(self, message):
        embed = discord.Embed()
        embed .title = "📢 Bot Alert"
        embed.description = message
        return await self.send(embed = embed)

class MyClient(Bot):

    async def get_context(self, message, *, cls=AlertContext):
        return await super().get_context(message, cls=cls)
    
    async def on_ready(self):
        print(f"Loged in as {self.user}")
        