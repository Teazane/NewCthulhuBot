import discord, random, time
from src.reactions import Reactions

class Bot(discord.Client):
    # Explication du mécanisme asynchrone Python : https://stackabuse.com/python-async-await-tutorial/

    async def on_ready(self):
        """
            Log un message quand le bot est prêt.
        """
        print("Cthulhu bot is now ready as " + str(self.user))
    
    async def on_connect(self):
        """
            Log un message quand le bot est connecté.
        """
        print("Cthulhu bot is now connected as " + str(self.user))
        print("Cthulhu has access to the following servers:")
        for guild in self.guilds:
            print("> " + str(guild.name) + "(" + str(guild.id) +  ") containing channels: ")
            for chan in guild.text_channels:
                print("\t - " + chan.name)

    async def on_message(self, message):
        """
            Traite un message quand le bot en reçoit un.
        """
        # Si l'auteur est un bot, on ne répond pas
        if message.author.bot:
            return
        else:
            print("The bot has received a message from " + message.author.name + ": " + message.content)
            reactions = Reactions()
            you_are_taunt = random.randint(0,50)
            if you_are_taunt == 0:
                await message.channel.send(reactions.toi_meme_repeat(message.content))
            else:
                response_msg = reactions.search_key_word(message.content)
                if response_msg is not None:
                    await message.channel.send(reactions.search_key_word(message.content))
                else:
                    pass

    async def on_disconnect(self):
        """
            Log un message quand le bot se déconnecte.
        """
        print("Cthulhu bot has been disconnected")