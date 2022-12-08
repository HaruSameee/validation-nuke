import random
from discord.ext import commands, tasks
import datetime
from datetime import datetime as dt
import os
from multicolorcaptcha import CaptchaGenerator
from dislash import InteractionClient, ActionRow, Button, ButtonStyle, Option, OptionType, SelectMenu, SelectOption, MessageInteraction
import random
import discord
from discord.ext import commands
from PIL import Image
from googletrans import Translator


intents = discord.Intents.all()
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='-', help_command=None, intents=intents)
inter_client = InteractionClient(bot)
translator = Translator()

@inter_client.slash_command(name = "captcha",
                description = "認証システムを配置します。",
                guild_ids=[948576902946377798])
async def captcha(ctx):
    user = ctx.author
    role = ctx.guild.get_role(975354748024791101)
    if role in user.roles:
        embed = discord.Embed(title='認証', description='以上の規約に同意できる方のみに認証へ進んでください。\n認証をすることでサーバに参加できます。', color=0x00e1ff)
        buttons = ActionRow(
            Button(
                style=ButtonStyle.green,
                label='認証',
                custom_id='verify'
            )
        )
        await ctx.send(embed=embed,components=[buttons])
    else:
        await ctx.send('権限がありません。', ephemeral=True) 

@inter_client.slash_command(name = 'nuke',
                description = 'チャンネルのログを削除します。',
                guild_ids=[948576902946377798]
                )
@commands.has_guild_permissions(manage_guild=True)
async def nuke(ctx):
    user = ctx.author
    role = ctx.guild.get_role(975354781168193616)
    if role in user.roles:
        pos = ctx.channel.position
        channel = await ctx.channel.clone()
        await ctx.channel.delete()
        await channel.edit(position=pos)
        embed = discord.Embed(description='チャンネルのログを削除しました✅',color=0x00e1ff, timestamp=dt.utcnow())
        await channel.send(embed=embed)
        ch = bot.get_channel(970171166515929140)
        await ch.send(f'`[{dt_now.strftime("%H:%M:%S")}]`🧹**{ctx.author.name}**{ctx.author.discriminator} nuked #{channel.name}\n[Criteria] {channel.id}\n[ Reason ] [no reason]')
    else:
        await ctx.send('権限がありません。', ephemeral=True)


@bot.event
async def on_button_click(ctx: MessageInteraction):
    custom_id = ctx.component.custom_id
    if custom_id == 'verify':
        user = ctx.author
        role = ctx.guild.get_role(975354748024791101)
        if  role in user.roles:
            await ctx.send('あなたは認証済みです。', ephemeral=True)

        else:
            a1 = random.randint(0,9)
            a2 = random.randint(0,9)
            global answer
            answer = a1*a2
            shiki = f'{a1}×{a2}'
            a = random.randint(0,81)
            b = random.randint(0,81)
            c = random.randint(0,81)
            d = random.randint(0,81)
            global h
            h = answer
            char = [a,b,c,d,h]
            result = random.sample(char, 5)
            r1 = str(result[0])
            r2 = str(result[1])
            r3 = str(result[2])
            r4 = str(result[3])
            r5 = str(result[4])
            button = ActionRow(
                    Button(
                        style=ButtonStyle.gray,
                        label = r1,
                        custom_id=r1
                    ),
                    Button(
                        style=ButtonStyle.gray,
                        label = r2,
                        custom_id=r2
                    ),
                    Button(
                        style=ButtonStyle.gray,
                        label = r3,
                        custom_id=r3
                    ),
                    Button(
                        style=ButtonStyle.gray,
                        label = r4,
                        custom_id=r4
                    ),
                    Button(
                        style=ButtonStyle.gray,
                        label = r5,
                        custom_id=r5
                    )
            )
            await ctx.reply(shiki, components=[button], ephemeral=True)
            answer = str(answer)

    elif custom_id == answer:
        verify_role = ctx.guild.get_role(975354748024791101)
        member = ctx.guild.get_member(ctx.author.id)
        await member.add_roles(verify_role)
        await ctx.send('認証完了しました。',ephemeral=True)

    else:
        print(custom_id)
        await ctx.send('認証失敗しました。',ephemeral=True)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.bot:
        return

    if message.content.startswith('-trans'):
        say = message.content
        say = say[7:]
        if say.find('-') == -1:
            str = say
            detact = translator.detect(str)
            befor_lang = detact.lang
            if befor_lang == 'ja':
                convert_string = translator.translate(str, src=befor_lang, dest='en')
                embed = discord.Embed(title='変換結果', color=0xff0000)
                embed.add_field(name='Befor', value=str)
                embed.add_field(name='After', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
            else:
                convert_string = translator.translate(str, src=befor_lang, dest='ja')
                embed = discord.Embed(title='変換結果', color=0xff0000)
                embed.add_field(name='Befor', value=str)
                embed.add_field(name='After', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
        else:
            trans, str = list(say.split('='))
            befor_lang, after_lang = list(trans.split('-'))
            convert_string = translator.translate(str, src=befor_lang, dest=after_lang)
            embed = discord.Embed(title='変換結果', color=0xff0000)
            embed.add_field(name='Befor', value=str)
            embed.add_field(name='After', value=convert_string.text, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith('!detect'):
        say = message.content
        s = say[8:]
        detect = translator.detect(s)
        m = 'この文字列の言語はたぶん ' + detect.lang + ' です。'
        await message.channel.send(m)

bot.run("")
