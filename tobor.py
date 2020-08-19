#importing useful stuff
import discord

#getting key file
try:
    with open(".discord.key", "r") as key_file:
        client_token=key_file.read()
        if not client_token:
            raise Exception
except: 
    print('Error when trying to read .discord.key, make sure you have the key file present in the same directory as this code ....... Are you sure you\'re allowed to be doing this?')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
     
    if message.author == client.user:
        return

    # mod only section
    if message.channel.id == 740613670933102655:
        print('only mods can use this')
        






    #everybody section
    if message.content.casefold() == 'good robot':
        await message.channel.send(':smile: :smile: :smile:')

    if message.content.casefold() == 'bad robot':
        await message.channel.send('sorry :frowning:')

    if 'bat' in message.content.casefold(): 
        await message.add_reaction('\U0001f987')

client.run(client_token)