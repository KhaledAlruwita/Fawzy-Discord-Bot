import discord

async def detect_explicit_words(message):
    explicit_words = [
    ]
    gif_url = ''
    sb_content = message.content
    for word in explicit_words:
        if word in sb_content:
            if message.author != message.guild.me: 
                response = f"ممنوع استخدام كلمة '{word}' هنا!"
                embed = discord.Embed()
                embed.set_image(url=gif_url)
                await message.reply(response, embed=embed)
            break
