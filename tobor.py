#importing useful stuff
import discord
import json
import subprocess

#running a git pull to get most recent changes
subprocess.call(["git", "pull"])

#getting key file
def main():
    try:
        with open(".discord.key", "r") as key_file:
            client_token=key_file.read()
            print('found .discord.key loaded')
            if not client_token:
                raise Exception
    except: 
        print('Error when trying to read .discord.key, make sure you have the key file present in the same directory as this code ....... Are you sure you\'re allowed to be doing this?')

    #creating/opening state file stores states and parameters of discord bot incase of random shutdown.
    try:
        with open("state.json", "r") as state_file:
            state=json.loads(state_file.read())  
            print('state.json found loading last saved state') 
            print(state)      
    except: 
            print('state file error creating blank state')
            state={
                'super' : {
                            'channels' : [740613670933102655]
                            },
                'command_key' : 't!',
                'whitelist': {
                            'channels' : [] 
                }

            }
            save(state)


    #creatng discord client 
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        print('TOBOR IS READY!')

    @client.event
    async def on_message(message):
        
        #prevent bot from reading own commands
        if message.author == client.user:
            return


        #these are admin commands
        if message.content.startswith(state["command_key"]):
            message.content= message.content[len(state["command_key"]):]
            if message.channel.id in state['super']['channels']:
                arg = message.content.split()

                #modifying super perms (aka where can admin commands be run)
                if arg[0] == 'super': 
                    del arg[0]

                    if arg[0] == 'channel':
                        del arg[0]
                        
                        if arg[0] == 'add':
                            del arg[0]

                            #check that arg[0] a channel
                            if arg[0].isnumeric():
                                state['super']['channels'].append(int(arg[0]))
                                await message.channel.send(f'Successfully addded channel:{arg[0]} to list of super channels')

                        elif arg[0] == 'del':
                            del arg[0]
                            try:
                                state['super']['channels'].remove(int(arg[0]))
                                await message.channel.send(f'Successfully removed channel: {arg[0]} from list of super channels')
                            except ValueError:
                                await message.channel.send(f'Channel: {arg[0]} is not a super channel')
                        else:
                            await message.channel.send(f'{state["command_key"]}super channel {arg[0]} is not a command')
                    else:
                        await message.channel.send(f'{state["command_key"]}super {arg[0]} is not a command')
                

                #whitlelist channels (aka bot does fun things only in approved channels)
                elif arg[0] == 'whitelist': 
                    del arg[0]

                    if arg[0] == 'channel':
                        del arg[0]
                        
                        if arg[0] == 'add':
                            del arg[0]

                            #check that arg[0] a channel
                            if arg[0].isnumeric():
                                state['whitelist']['channels'].append(int(arg[0]))
                                await message.channel.send(f'Successfully addded whitelist:{arg[0]} to list of whitelisted channels')

                        elif arg[0] == 'del':
                            del arg[0]
                            try:
                                state['whitelist']['channels'].remove(int(arg[0]))
                                await message.channel.send(f'Successfully removed channel: {arg[0]} from list of whitelisted channels')
                            except ValueError:
                                await message.channel.send(f'Channel: {arg[0]} is not a super channel')
                        else:
                            await message.channel.send(f'{state["command_key"]}whitelist channel {arg[0]} is not a command')
                    else:
                        await message.channel.send(f'{state["command_key"]}super {arg[0]} is not a command')

                #git commands
                elif arg[0] == 'git': 
                    del arg[0]

                    if arg[0] == 'pull':
                        del arg[0]
                        subprocess.call(["git", "pull"], shell=True)
                        await message.channel.send('I pulled')

                    else:
                        await message.channel.send(f'{state["command_key"]}git {arg[0]} is not a command')

                else:
                        await message.channel.send(f'{arg[0]} is not a command')


                save(state)
        #everybody section
        elif message.channel.id in state['whitelist']['channels'] or message.channel.id in state['super']['channels']:
            if message.content.casefold() == 'good robot':
                await message.channel.send(':smile: :smile: :smile:')

            elif message.content.casefold() == 'bad robot':
                await message.channel.send('sorry :frowning:')

            elif 'bat' in message.content.casefold(): 
                await message.add_reaction('\U0001f987')

    client.run(client_token)


#helpful functions 
def save(json_val, file='state.json'):
    #write and save file
    f = open(file, "w+")
    cur_state=f.read()
    new_state=json.dumps(json_val)
    if (cur_state != new_state):
        f.write(new_state)
        f.close()

        #git add commit and push
        subprocess.call(["git", "add", file])
        subprocess.call(["git", "commit", "-m", "tobor state update"])  
        subprocess.call(["git", "push"])  
    else:
        f.close()



#running main
main()