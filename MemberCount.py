import discord
from discord.ext import commands
import configparser
import os

version = 0.1
print('##########################')
print('# Discord MemberCount    #')
print(f'# Version {version}            #')
print('##########################')
print('\n')

CONFIG_DIR = "config"
CONFIG_FILE = "config/config.ini"
config = configparser.ConfigParser()

##### CONFIG HANDELING #####
if not os.path.exists(CONFIG_DIR):
    print("Creating CONFIG_DIR\n")
    os.system(f"mkdir {CONFIG_DIR}")
if not os.path.exists(CONFIG_FILE):
    print("Creating CONFIG_FILE \n")
    config.add_section("Settings")
    config.set("Settings", "TOKEN", "")
    config.set("Settings", "BOT_PREFIX", "!")
    config.set("Settings", "OWNER_ID", "")
    config.set("Settings", "CHANNEL", "")
    config.set("Settings", "STATUS", "Counting members... 🔄")
    config.add_section("Messages")
    config.set("Messages", "# Available placeholders: {0} user-ammount | {1} servername", "")
    config.set("Messages", "Join", "「⏫」 {0} Members on {1}")
    config.set("Messages", "Leave", "「⏬」 {0} Members {1}")
    file = open(CONFIG_FILE, 'w')
    config.write(file)
    file.close()
else:
    print("All Direcories and Files in place!\nContinuing")

config.read(CONFIG_FILE)
BOT_PREFIX = config.get('Settings', 'BOT_PREFIX')
TOKEN = config.get('Settings', 'TOKEN')
if TOKEN == "" or TOKEN == None:
    print("##### Please edit the settings-file and fill in a Bot-Token #####")
    exit()
else:
    TOKEN = config.get("Settings", "TOKEN")
    BOT_PREFIX = config.get("Settings", "BOT_PREFIX")
    OWNER_ID = config.get("Settings", "OWNER_ID")
    CHANNEL = config.get("Settings", "Channel")
    STATUS = config.get("Settings", "Status")
    JOIN = config.get("Messages", "Join")
    LEAVE = config.get("Messages", "Leave")


if __name__ == '__main__':
    client = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all(), case_insensitive=True,
                          owner_id=OWNER_ID)


    @client.event
    async def on_ready():
        print("Erfolgreich als {0.user} angemeldet".format(client))
        print(f"Discord.python version: {discord.__version__}")
        print(f"Name: {client.user.name}")
        print(f"ID: {client.user.id}")
        print(f"Prefix: {BOT_PREFIX}")
        print(
            f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=261993005047&scope=bot%20applications.commands")
        print("--------------------------------------------------")
        game = discord.Game(STATUS)
        await client.change_presence(status=discord.Status.dnd, activity=game)


    @client.event
    async def on_member_join(ctx):
        member = len(ctx.guild.members)
        servername = ctx.guild.name
        count_channel = client.get_channel(int(CHANNEL))
        plus = JOIN.format(member, servername)
        await count_channel.edit(name=plus)


    @client.event
    async def on_member_remove(ctx):
        member = len(ctx.guild.members)
        servername = ctx.guild.name
        count_channel = client.get_channel(int(CHANNEL))
        minus = LEAVE.format(member, servername)
        await count_channel.edit(name=minus)

    client.run(TOKEN)
