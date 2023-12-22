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


@bot.slash_command(name="gpt_query", description="Ask ChatGPT a question")
async def chat(ctx, arg):
    chatgpt = chat_completion(arg)
    await ctx.respond(chatgpt)


@bot.slash_command(name="image_generation", description="Ask AI for an image")
async def image(ctx, arg):
    url = image_generation(arg)
    embed = discord.Embed(
        title="Image"
    )
    embed.set_image(url=url)
    await ctx.send(embed=embed, reference=ctx.message)


@bot.slash_command(name="gpt_vision", description="Generate a meme caption")
async def image_chat(ctx, arg1: str, arg2: discord.Attachment):
    print(arg1)
    print(arg2)
    await ctx.respond("ok attachment received")

bot.run(os.environ['DISCORD_API'])
