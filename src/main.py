import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents().all()
intents.members = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents
)

bot.author_id = 892824832243269692  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author.name)


@bot.command()
async def count(ctx):
    online = 0
    offline = 0
    idle = 0
    dnd = 0
    for member in ctx.guild.members:
        if str(member.status) == 'online':
            online+= 1
        elif str(member.status) == 'offline':
            offline+= 1
        elif str(member.status) == 'idle':
            idle+= 1    
        elif str(member.status) == 'dnd':
            dnd+= 1
    await ctx.send("{} are online, {} are offline, {} are idle and {} don't want to be disturbed!".format(online, offline, idle, dnd))


@bot.command()
async def admin(ctx, arg):
    listMembers = ctx.guild.members
    for member in listMembers:
        if str(member.name) == arg:
            role = ""
            found = False
            for role_i in ctx.guild.roles:
                if role_i.name == "admin":
                    role = role_i
                    found = True
                    break
            if not found:
                role = await ctx.guild.create_role(name="admin", permissions=discord.Permissions(8))
                await member.add_roles(role)
            else:
                await member.add_roles(role)
            return 


@bot.command()
async def xkcd(ctx):
    rd = random.randint(1, 2500)
    path = 'https://xkcd.com/{}/'.format(rd)
    await ctx.send(path)

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot.run(token)  # Starts the bot