import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    commandlist = "$command, $hello, $bye, $rolld6"

    if message.content.startswith('$command'):
        await message.channel.send('The Following commands are: '+ commandlist)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$bye'):
        await message.channel.send('Goodbye')

    if message.content.startswith('$rolld6'):
        await message.channel.send('Rolling')
        await message.channel.send(random.randint(1,7))

    if message.content.startswith('$rolld20'):
        await message.channel.send('Rolling')
        await message.channel.send(random.randint(1,21))

client.run('insert token here')
