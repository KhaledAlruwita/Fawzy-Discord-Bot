import discord
from discord.ext import commands
import asyncio
TOKEN = ""
def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    voice_clients = {}

    @bot.event
    async def on_ready():
        print("Bot is ready!")
        print(bot.user)

    @bot.event
    async def on_message(message):
        if message.content == "فوزي فويس":
            channel = bot.get_channel(1232576889831424101)
            if channel:
                voice_client = await channel.connect()
                voice_clients[channel.guild.id] = voice_client
                await message.channel.send(f"تمت انا ب {channel.name}")
        

    bot.run(TOKEN)

if __name__ == "__main__":
    run()
