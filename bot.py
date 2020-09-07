import discord
from key import give_bot_key
import re

key = give_bot_key()
client = discord.Client()
mbl = ["&"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    mb = mbl[0] #the beginning of a message

    if message.author == client.user:
        return

    if message.content.startswith(mb) == False:
        return


    if message.content.startswith(mb+'help'):
        await message.channel.send('Commands:')
        await message.channel.send("{}change new_prefix ----- This will change how I register commands".format(mb))
    
    if message.content.startswith(mb+'change'):
        txt = message.content
        command = re.compile(r'.*change\s*')
        mbl[0] = command.sub('',txt)
        await message.channel.send("The command prefix has been changed to: {}".format(mbl[0]))

    if message.content.startswith(mb+'reassure me'):
        await message.channel.send("Ok {}, It's all going good. Trust me, I am a robot".format(message.author.display_name))

client.run(key)