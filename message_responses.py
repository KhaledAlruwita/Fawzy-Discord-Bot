import asyncio
import random
import socket
Loveimages = [
    'example1.gif',
    'example2.gif',
    'example3.gif',
    'example4.gif',
    'example5.gif'
]




Hateimages = [
    'example1.gif',
    'example2.gif',
    'example3.gif',
    'example4.gif',
    'example5.gif'
]

async def handle_message(message, bot):
    if message.author == bot.user:
        return

    if message.content.lower() == "فوزي ا" or message.content.lower() == "fz a":
        host_name = socket.gethostname()
        
        await message.reply(f"فوزي 1.00 | | على {host_name}")
    if message.content.lower() == "فوزي خلصت مذاكرة":
        await asyncio.sleep(5)
        await message.reply("شطوور")
    if message.content.lower() == "فوزي":
            await asyncio.sleep(3)
            await message.reply("هلا")

    




    if message.content.startswith("فوزي قول لي"):
        content = message.content[12:] 
        await message.reply(content)
    boost_role_id = 1045185777597939803
    if any(role.id == boost_role_id for role in message.author.roles) and message.content.startswith("فوزي قوليي "):
        content = message.content[11:]
        await message.delete()
        await message.channel.send(content)
    if message.content.lower() == "فوزي اكرهك":
            await asyncio.sleep(10)
            Hateimage = random.choice(Hateimages)
            await message.reply(Hateimage)

    if message.content.lower() == "فوزي احبك":
            Loveimage = random.choice(Loveimages)
            await asyncio.sleep(10)
            await message.reply(Loveimage)

    elif message.content.lower() == "صباح الخير":
            await asyncio.sleep(4)
            await message.reply("صباح النووور")
    elif message.content.lower() == "فوزي كيف حالك":
            await asyncio.sleep(7)
            await message.reply.send("أنا بخير، شكرًا!")
