from src.bot import Bot
import discord.ext
from openai_functions import (
    chat_completion,
    image_generation
)
import os
from dotenv import load_dotenv

load_dotenv()
bot = Bot()


@bot.slash_command(name="test", description="Check if the bot is up")
async def ping(ctx):
    await ctx.respond("pong")


@bot.slash_command(name="gpt_query", description="Ask ChatGPT a question")
async def chat(ctx, arg):
    message = []
    if ctx.author.id in bot.conversation_history:
        message = bot.conversation_history[ctx.author.id]
        if len(message) > 9:
            message = message[2:]
        message.append(
            {"role": "user", "content": arg},
        )
    else:
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": arg},
        ]
    completion = chat_completion(message)
    message.append(
        {"role": "system", "content": completion},
    )
    bot.conversation_history[ctx.author.id] = message
    print(bot.conversation_history[ctx.author.id])
    await ctx.respond(completion)


@bot.slash_command(name="image_generation", description="Ask AI for an image")
async def image(ctx, arg):
    url = image_generation(arg)
    embed = discord.Embed(
        title="Image"
    )
    file = discord.File("./AI.png")
    embed.set_image(url="attachment://AI.png")
    await ctx.respond(file=file, embed=embed)


@bot.slash_command(name="gpt_vision", description="Generate a meme caption")
async def image_chat(ctx, arg1: str, arg2: discord.Attachment):
    print(arg1)
    print(arg2)
    await ctx.respond("ok attachment received")

bot.run(os.environ['DISCORD_API'])
