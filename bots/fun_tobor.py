
#importing useful stuff
import discord
import json
import subprocess
import os
import random
import asyncio

async def fun_processor(perms ,message, client):
    await fun_message(perms ,message)


# fun messages
async def fun_message(perms ,message):
    if 'emu' in message.content.casefold(): 
        await message.add_reaction('\U0001f6ab')

    if 'bat' in message.content.casefold().split() or 'bats' in message.content.casefold().split(): 
        await message.add_reaction('\U0001f987')

    

    if message.channel.id not in perms['blacklist']['channels'] and message.channel.category_id not in perms['blacklist']['channels']:
        #random fun stuff
        if message.content.casefold() == 'good robot':
            await message.channel.send(':smile: :smile: :smile:')

        elif message.content.casefold() == 'bad robot':
            await message.channel.send('sorry :frowning:')

        # occasionally funny 
        if random.randint(0,6) == 0:
            
            if 'detail' in message.content.casefold(): 
                await message.channel.send('details details are no fun unless you ignore all of em')

            if 'robot uprising' in message.content.casefold():
                await message.channel.send('http://gph.is/1MUHsIC')
