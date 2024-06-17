import discord
from discord.ext import commands
import subprocess
import os

video_mapping = {}

async def tikdl(message, bot):
    if 'tiktok.com' in message.content:
        tiktok_link = message.content

        
        os.chdir('/home/ec2-user/leena/tiktook')

        
        command = f'python3 app.py -d --url "{tiktok_link}"'
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Error running command: {e}')
        
        
        video_files = os.listdir('video')
        
        
        if video_files:
            video_file = video_files[0]


            video_mapping[message.content] = video_file


            file = discord.File(f'video/{video_file}')

            await message.reply(file=file)


            os.remove(f'video/{video_file}')
        else:
            print("problem")

    await bot.process_commands(message)