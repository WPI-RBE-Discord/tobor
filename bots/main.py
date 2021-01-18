#importing useful stuff
import discord
import json
import subprocess
import os
import asyncio
from fun_tobor import fun_processor
from msg_tobor import msg_processor 

def main():
    #getting key file
    try:
        client_token = os.getenv("DISCORD_BOT_TOKEN")
    except: 
        print('Error when trying to read token ....... Are you sure you\'re allowed to be doing this?')

    
    #creating/opening state file stores states and parameters of discord bot incase of random shutdown.
    global perms 
    perms = update_perms()

    #creatng discord client 
    global client 
    client= discord.Client()
    
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        print('TOBOR IS IN!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        # function to process messages 
        await fun_processor(perms, message, client)
        await msg_processor(perms, message, client)

    client.run(client_token)

#reloads perms.json
def update_perms():
    #running a git pull to get most recent changes
    with open('./perms.json', 'r') as f:
        return json.loads(f.read())
    print('updated json')

#run main
if __name__ == "__main__":
    main()