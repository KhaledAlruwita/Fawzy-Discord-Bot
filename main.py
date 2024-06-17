import discord
from discord.ext import commands
#from daily_task import send_koo
from message_responses import handle_message
#from explicit_words import detect_explicit_words
from kicks import handle_kicks
import asyncio
#from points import register_member
#from points import add_points
#from points import remove_points
#from points import top_points
#from points import retrieve_points
from tiktook.tk import tikdl
#from relo import reelh

TOKEN = ""
def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)


    voice_clients = {}

    @bot.event
    async def on_ready():
        print("________________________________________")
        print(bot.user)

    @bot.event
    async def on_message(message):
        await handle_message(message, bot)
        #await detect_explicit_words(message)
        await handle_kicks(message, bot)
       # await register_member(message, bot)
       # await add_points(message, bot)
       # await remove_points(message, bot)
       # await retrieve_points(message, bot)
        #await top_points(message, bot)
        await tikdl(message, bot)
        #await reelh(message, bot)
        
        
    
    
    
    bot.run(TOKEN)

if __name__ == "__main__":
    run()
