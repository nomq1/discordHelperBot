import discord
import escapeString
from discord.ext import commands
import subprocess

bot = commands.Bot(description="preform commands on local computer", command_prefix=(";"))
programs = {'teamviewer':"C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe"}

@bot.event
async def on_ready():
    print("I'm ready!")
@bot.command()
async def hello():
    """greet my master"""
    await bot.say("Hello master Dros")
@bot.command()
async def say(something):
    await bot.say("I hope the next generation of Waynes wont inherit an empty wine cellar. Not that there's likely to be a next generation.")

@bot.command()
async def open(programName="a"):
    """open teamviewer"""
    programName = escapeString.escape_argument(programName)
    if programName in programs:
        await bot.say("Right away sir")
        programPath = programs[programName]
        subprocess.call([programPath])
    else:
        await bot.say("hmm.. sir im afraid that I cant do that , Remember the last time we used unauthorized software ?")
@bot.command()
async def lsopen():
    """openable programs"""
    programsstring = "the authorized softwares are : \n"
    for name in programs :
        programsstring =  programsstring +"  " + name + "\n"
    await bot.say(programsstring)

bot.run("NDI5NzE4MzI4ODExMTkyMzIw.DaFuGw.t07joxBMc29tbf6-vq35D1lLNNc")