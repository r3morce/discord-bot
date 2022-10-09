# Import stuff
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()

# Read permission from another file .env
TOKEN = os.getenv('DISCORD_TOKEN')


# This will load the permissions the bot has been granted in the previous configuration
intents = discord.Intents.default()
intents.message_content = True


# Create custom discord.Client class
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.added = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.added:
            self.added = True
        print(f"Say hi to {self.user}!")


# Init custom client
client = aclient()


# Read messages and respond
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


# Add the token (permission) of your bot
client.run(TOKEN)
