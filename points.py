import mysql.connector
import discord
import pandas as pd
import requests
from io import BytesIO
import io
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
allowed_role_id = 1132572147781476362
async def register_member(message, bot):
    if message.author == bot.user:
        return

    if message.content.lower() == "فوزي سجلني في الرابطة":
        conn = mysql.connector.connect(
            host="",
            port="",
            user="",
            password="",
            database="",
        )
        cursor = conn.cursor()
        user_id = message.author.id
        username = message.author.name
        print(user_id)
        cursor.execute("INSERT INTO *** (id, name, ps_points) VALUES (%s, %s, %s);", (user_id, username, 0))
        conn.commit()
        cursor.close()
        conn.close()
    
        await message.reply(" تم!")

async def add_points(message, bot):
    if "فوزي اضف" in message.content and message.author.roles and 1132572147781476362 in [role.id for role in message.author.roles]:
        user_to_add_points = message.mentions[0] if message.mentions else None

        if user_to_add_points:
            conn = mysql.connector.connect(
                host="",
                port="",
                user="",
                password="",
                database="",
            )
            cursor = conn.cursor()

            user_id = user_to_add_points.id
            points_to_add = 5
            
            cursor.execute("UPDATE *** SET ps_points = ps_points + %s WHERE id = %s;", (points_to_add, user_id))
            conn.commit()
            cursor.close()
            conn.close()

            
            image_url = ""
            response = requests.get(image_url)
            image_data = BytesIO(response.content)
            await message.reply(f"تمت إضافة {points_to_add} نقطة لـ {user_to_add_points.mention}.", file=discord.File(image_data, "anime-girl.gif"))


        else:
            await message.reply(" لمين ؟")



async def remove_points(message, bot):
    if "فوزي اخصم" in message.content and message.author.roles and 1132572147781476362 in [role.id for role in message.author.roles]:
        user_to_add_points = message.mentions[0] if message.mentions else None

        if user_to_add_points:
            conn = mysql.connector.connect(
                host="",
                port="",
                user="",
             password="",
                database="",
            )
            cursor = conn.cursor()

            user_id = user_to_add_points.id
            points_to_add = -5
            
            cursor.execute("UPDATE *** SET ps_points = ps_points + %s WHERE id = %s;", (points_to_add, user_id))
            conn.commit()
            cursor.close()
            conn.close()

            image_url = ""
            response = requests.get(image_url)
            image_data = BytesIO(response.content)
            await message.reply(f"تم خصم {points_to_add} نقطة لـ {user_to_add_points.mention}.", file=discord.File(image_data, "anime-girl.gif"))
        else:
            await message.reply(" لمين ؟")


async def retrieve_points(message, bot):
    if message.content.lower() == "فوزي كم نقاطي":
        user_id = message.author.id
        result = None
        conn = mysql.connector.connect(
                host="",
                port="3306",
                user="",
                password="",
                database="",
            )
        cursor = conn.cursor()
        cursor.execute("SELECT ps_points FROM RMRA WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result is not None:
            ps_points = result[0]  
            response = f" نقاطك هي {ps_points} نقطة بلاتينية"
        else:
            response = "😕ليس لديك نقاط بعد."

 
        await message.reply(response)



async def top_points(message, bot):
    if message.content.lower() == "فوزي ارسلي ترتيب النقاط":
        conn = mysql.connector.connect(
            host="",
            port="",
            user="",
            password="",
            database="",
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM X")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        
        df = pd.DataFrame(data, columns=['id', 'name', 'ps_points'])
        colors = plt.cm.viridis(range(len(df)))
        xlbl = get_display(arabic_reshaper.reshape('يوزر الدسكورد'))
        ylbl = get_display(arabic_reshaper.reshape('النقاط '))
        title = get_display(arabic_reshaper.reshape('ترتيب النقاط '))

        plt.bar(df['name'], df['ps_points'], color=colors)
        plt.xlabel(xlbl)
        plt.ylabel(ylbl)
        plt.title(title)


        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        await message.channel.send(" هو ترتيب نقاط الرابطة:", file=discord.File(buffer, 'points.png'))



    











