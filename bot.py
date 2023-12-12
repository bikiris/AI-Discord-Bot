import discord.ext
from discord.ext import commands
from completion import chat_completion
import os
from dotenv import load_dotenv

load_dotenv()
client = commands.Bot()


@client.event
async def on_ready():
    print('Logged on as', client.user)


@client.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == client.user:
        return


@client.slash_command(name="gpt_query", description="Ask ChatGPT a question")
async def first_command(ctx, arg):
    chatgpt = chat_completion(arg)
    await ctx.respond(chatgpt)


client.run(os.environ['DISCORD_API'])
