import discord
async def handle_kicks(message, bot):
    allowed_role_id = 1166811408357404824

    if "فوزي اطرد" in message.content and message.mentions:
        if message.author.guild_permissions.kick_members:

            member_to_kick = message.mentions[0]
            author = message.author
            allowed_role = discord.utils.get(author.roles, id=allowed_role_id)

            if allowed_role:
                await member_to_kick.kick()
                await message.channel.send(f"{member_to_kick.mention} تم طرده 🤭.")
            else:
                await message.reply("ليس لديك الإذن بطرد الأعضاء 😡.")
        else:
            await message.reply("ليس لديك الإذن بطرد الأعضاء 😡.")