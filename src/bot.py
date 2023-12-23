import discord.ext


class Bot(discord.Bot):
    conversation_history = {}

    async def on_ready(self):  # override the on_ready event
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    # async def on_interaction(self, interaction):
    #     print(interaction)
