#importing useful stuff
import discord
import json
import subprocess



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
        elif message.content.startswith(perms['command_key']) and message.channel.id in perms['super']['channels']:
            message = pop_command_key(message, perms)

            args = message.content.split()

            await command_handler( message, args)

            


    client.run(client_token)

#msg_commands
async def post(message, args):
    
    try:
        #get channel id 
        channel_id = int(args.pop(0))

        #post message
        message_content = ' '.join(args)

        channel = client.get_channel(channel_id)

        if channel: 
            sent_msg = await channel.send(message_content)
            await message.channel.send(f'I do the post, message id: {sent_msg.id}')
        else:
            await message.channel.send(f'No channel with ID: {channel_id}')


    except (ValueError, IndexError):
        await message.channel.send(f't! msg post <channel_id> <msg content>')

async def edit(message, args):
    #get channel id 
    try:
        channel_id = int(args.pop(0))
        message_id = int(args.pop(0))
        
        #post message
        message_content = ' '.join(args)

        channel = client.get_channel(channel_id)
        

        if channel:
            msg = await channel.fetch_message(message_id)
            if msg: 
                await msg.edit(content=message_content)
                await message.channel.send(f'I did edit, message id: {msg.id}')
            else:
                await message.channel.send(f'No message with ID: {message_id} in channel {channel_id}')
        else:
            await message.channel.send(f'No channel with ID: {channel_id}')

    except (ValueError, IndexError):
        await message.channel.send(f't! msg edit <channel_id> <message_id> content')

async def delete(message, args):
    #get channel id 
    try:
        channel_id = int(args.pop(0))
        message_id = int(args.pop(0))
        

        channel = client.get_channel(channel_id)
        

        if channel:
            msg = await channel.fetch_message(message_id)
            if msg: 
                await msg.delete()
                await message.channel.send(f'It is gone now')
            else:
                await message.channel.send(f'No message with ID: {message_id} in channel {channel_id}')
        else:
            await message.channel.send(f'No channel with ID: {channel_id}')

    except (ValueError, IndexError):
        await message.channel.send(f't! msg delete <channel_id> <message_id>')

   



#command handler
async def command_handler(message, args):

    msg_commands= {
        'post'   : post,
        'edit'   : edit,
        'delete' : delete
    }


    if args[0] == 'msg':
        del args[0]
        if args[0] in msg_commands.keys():
            cmd = args.pop(0)
            await msg_commands[cmd](message, args)
        else: 
            await message.channel.send(f'No command {args[0]} in msg command')







#purge message command_key
def pop_command_key(message,perms):
    message.content = message.content[len(perms['command_key']):]
    return message

#reloads perms.json
def update_perms():
    #running a git pull to get most recent changes
    subprocess.call(["git", "pull"])
    with open('../perms.json', 'r') as f:
        return json.loads(f.read())
    print('updated json')



#run main
main()