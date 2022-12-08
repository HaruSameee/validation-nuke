import discord
import datetime
import asyncio
from discord.ext import tasks

bot = discord.Client()

@tasks.loop(seconds=60)
async def loop():
    now = datetime.datetime.now().strftime('%H:%M')
    if now == '00:00':
        guild = bot.get_guild(948576902946377798)
        notice = bot.get_channel(975355576789901332)
        await notice.send('全てのチャンネルのログを削除します...')
        for channel in guild.channels:
            if str(channel.type) == 'news' and channel.topic == 'nuke':
                pos = channel.position
                await channel.delete()
                new_ch = await channel.clone()
                await new_ch.edit(position=pos)

        for channel in guild.channels:
            if str(channel.type) == 'text' and channel.topic == 'nuke':
                pos = channel.position
                await channel.delete()
                new_ch = await channel.clone()
                await new_ch.edit(position=pos)
                await asyncio.sleep(1)
    
    elif now == '06:00':
        guild = bot.get_guild(948576902946377798)
        notice = bot.get_channel(975355576789901332)
        await notice.send('全てのチャンネルのログを削除します...')
        for channel in guild.channels:
            if str(channel.type) == 'news' and channel.topic == 'nuke':
                pos = channel.position
                await channel.delete()
                new_ch = await channel.clone()
                await new_ch.edit(position=pos)

        for channel in guild.channels:
            if str(channel.type) == 'text' and channel.topic == 'nuke':
                pos = channel.position
                await channel.delete()
                new_ch = await channel.clone()
                await new_ch.edit(position=pos)
                await asyncio.sleep(1)
    
    elif now == '12:00':
        guild = bot.get_guild(948576902946377798)
        notice = bot.get_channel(975355576789901332)
        await notice.send('全てのチャンネルのログを削除します...')
        for channel in guild.channels:
            if str(channel.type) == 'news' and channel.topic == 'nuke':
                pos = channel.position
                await channel.delete()
                new_ch = await channel.clone()
                await new_ch.edit(position=pos)

        for channel in guild.channels:
            if str(channel.type) == 'text' and channel.topic == 'nuke':
                pos = channel.position
                await channel.delete()
                new_ch = await channel.clone()
                await new_ch.edit(position=pos)
                await asyncio.sleep(1)
    
    elif now == '18:00':
        guild = bot.get_guild(948576902946377798)
        notice = bot.get_channel(975355576789901332)
        await notice.send('全てのチャンネルのログを削除します...')
        for channel in guild.channels:
            if str(channel.type) == 'news' and channel.topic == 'nuke':
                pos = channel.position
                await channel.delete()
                new_ch = await channel.clone()
                await new_ch.edit(position=pos)

        for channel in guild.channels:
            if str(channel.type) == 'text' and channel.topic == 'nuke':
                pos = channel.position
                await channel.delete()
                new_ch = await channel.clone()
                await new_ch.edit(position=pos)
                await asyncio.sleep(1)
@bot.event
async def on_ready():
    await loop()

bot.run('')
