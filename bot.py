import discord
import logging
from completion import chat_completion
import os
from dotenv import load_dotenv
load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('/'):
            print(message.content[1:])
            chatgpt = chat_completion(message.content[1:])
            await message.channel.send(chatgpt)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run(os.environ['DISCORD_API'],log_handler=handler)

