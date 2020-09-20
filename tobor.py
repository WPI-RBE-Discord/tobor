#importing useful stuff
import discord
import json
import subprocess


def main():
    #getting key file
    try:
        with open(".discord.key", "r") as key_file:
            client_token=key_file.read()
            print('found .discord.key loaded')
            if not client_token:
                raise Exception
    except: 
        print('Error when trying to read .discord.key, make sure you have the key file present in the same directory as this code ....... Are you sure you\'re allowed to be doing this?')

    #creating/opening state file stores states and parameters of discord bot incase of random shutdown.
    perms=update_perms()
    


    #creatng discord client 
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        print('TOBOR IS READY!')

    @client.event
    async def on_message(message):
        print(message)
        if message.content.startswith(perms['command_key']):
            #remove command key
            message.content= message.content[len(state["command_key"]):]
            #splitting message into arguments
            args = message.content.split()
            #if message.channel.id not in perms['super']['channels']:
                #super_message(message, args, perms)



        await fun_message(message)



    client.run(client_token)

#reloads perms.json
def update_perms():
    #running a git pull to get most recent changes
    subprocess.call(["git", "pull"])
    with open('perms.json', 'r') as f:
        return json.loads(f.read())
    print('updated json')


#admin related messages
#super_message(message, args, perms):



# fun messages
async def fun_message(message):
    #random fun stuff
    if message.content.casefold() == 'good robot':
        await message.channel.send(':smile: :smile: :smile:')

    elif message.content.casefold() == 'bad robot':
        await message.channel.send('sorry :frowning:')

    elif 'bat' in message.content.casefold(): 
        await message.add_reaction('\U0001f987')



#run main
main()