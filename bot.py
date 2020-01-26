import discord

class Bot(discord.Client):

    async def on_ready(self):
        print("Cthulhu bot is now logged as " + str(self.user))

    async def on_message(self, message):
        # Si l'auteur est un bot, on ne répond pas
        if message.author.bot:
            return
        pass

    async def on_disconnect(self):
        print("Cthulhu bot has been disconnected")