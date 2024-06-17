import discord
import re
import instaloader
import os

async def reelh(message, bot):
    if 'https://www.instagram.com/reels/' in message.content or 'https://www.instagram.com/reel/' in message.content:
        L = instaloader.Instaloader()
        reel_url = message.content
        shortcode_match = re.search(r'/reels?/([^/?]+)', reel_url)
        if shortcode_match:
            shortcode = shortcode_match.group(1)
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            
            if post.is_video:
                L.download_post(post, target="directory")

                for filename in os.listdir("directory"):
                    if not filename.endswith(".mp4"):
                        os.remove(os.path.join("directory", filename))

                
                for filename in os.listdir("directory"):
                    if filename.endswith(".mp4"):
                        video_path = os.path.join("directory", filename)
                        video_file = discord.File(video_path)
                        await message.reply(file=video_file)

                        
                        os.remove(video_path)
