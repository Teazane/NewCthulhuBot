import discord, random, time
from reactions import Reactions

class Bot(discord.Client):
    # Explication du mécanisme asynchrone Python : https://stackabuse.com/python-async-await-tutorial/

    # Initialisation du client avec création des réactions (chargement des listes, ...)
    def __init__(self):
        self.reactions = Reactions()

    async def on_ready(self):
        print("Cthulhu bot is now ready as " + str(self.user))
    
    async def on_connect(self):
        print("Cthulhu bot is now connected as " + str(self.user))
        for chan in self.guilds[0].channels:
            if chan.name == "general":
                await chan.send("Salut les p'tits potes !")

    async def on_message(self, message):
        # Si l'auteur est un bot, on ne répond pas
        if message.author.bot:
            return
        else:
            you_are_taunt = random.randint(0,50)
            if you_are_taunt == 0:
                await message.channel.send(self.reactions.toi_meme_repeat(message.content))
            else:
                await message.channel.send(self.reactions.search_key_word(message.content))

    async def on_disconnect(self):
        print("Cthulhu bot has been disconnected")

    def muted_for_15_minutes(self):
        time.sleep(900)
        self.reactions.muted_state = False