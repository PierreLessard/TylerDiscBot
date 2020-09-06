import discord
from key import give_bot_key

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

    if message.content[0] != mb:
        return

    print(message.content)
    print(message.content[0])

    if message.content.startswith(mb+'help'):
        await message.channel.send('Commands:')
        await message.channel.send("'"+mb + "change new_classifier ----' This will change the the prefix on commands")
    
    if message.content.startswith(mb+'change'): 
        mbl[0] = message.content[len(message.content)-1]
        await message.channel.send("The command prefix has been changed to: " +  mbl[0])

client.run(key)