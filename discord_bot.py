from datetime import datetime
import discord
from discord.ext import commands
import security
from roll_char import rollCharCommand

TOKEN = security.api_key.get(security.DISCORD_KEY)
bot = commands.Bot(command_prefix='!')


@commands.command()
async def test(ctx, arg):
    await ctx.send(f'@{ctx.author._user.display_name}#{ctx.author._user.discriminator} прислал {arg}')


@commands.command()
async def clear(ctx, amount):
    await ctx.channel.purge(limit=int(amount))


@commands.command()
async def roll_char(ctx):
    message = rollCharCommand()
    msg_c = message.get('text')
    msg_p = message.get('pic')
    await ctx.send(msg_c)
    await ctx.send(file=discord.File(msg_p))

bot.add_command(clear)
bot.add_command(test)
bot.add_command(roll_char)


try:
    print(f'[{datetime.now()}]: BOT is started!')
    bot.run(TOKEN)
except Exception:
    print(f'[{datetime.now()}]: BOT starting falled...')
