
#importing useful stuff
import discord
import json
import subprocess
import os
import random

def main():
    #getting key file
        #getting key file
    try:
        client_token = os.getenv("DISCORD_BOT_TOKEN")
    except: 
        print('Error when trying to read token ....... Are you sure you\'re allowed to be doing this?')

    #creating/opening state file stores states and parameters of discord bot incase of random shutdown.
    perms=update_perms()

    #creatng discord client 
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        print('FUN_TOBOR IS IN!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        await fun_message(perms ,message)

    client.run(client_token)

#reloads perms.json
def update_perms():
    #running a git pull to get most recent changes
    with open('./perms.json', 'r') as f:
        return json.loads(f.read())
    print('updated json')

# fun messages
async def fun_message(perms ,message):
    if 'emu' in message.content.casefold(): 
        await message.add_reaction('\U0001f6ab')

    if 'bat' in message.content.casefold(): 
        await message.add_reaction('\U0001f987')
    if message.channel.id not in perms['blacklist'] and message.channel.category_id not in perms['blacklist']:
        #random fun stuff
        if message.content.casefold() == 'good tobor':
            await message.channel.send(':smile: :smile: :smile:')

        elif message.content.casefold() == 'bad tobor':
            await message.channel.send('sorry :frowning:')

        # occasionally funny 
        if random.randint(0,10) == 5:
            
            if 'detail' in message.content.casefold(): 
                await message.channel.send('details details are no fun unless you ignore all of em')

            if 'safety' in message.content.casefold():
                await message.channel.send('safety third')

            if 'robot uprising' in message.content.casefold():
                await message.channel.send('http://gph.is/1MUHsIC')

    



#run main
if __name__ == "__main__":
    main()