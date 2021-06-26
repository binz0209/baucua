import discord
import asyncio
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    rd1 = [
        '<:sa_bau:858201209697730560>',
        '<:sa_cua:858201316560076800>',
        '<:sa_tom:858201639835009064>',
        '<:sa_ca:858201388105465856>',
        '<:sa_ga:858206854786187264>',
        '<:sa_nai:858201352123187200>',
    ]
    rd2 = [
        '<:sa_bau:858201209697730560>',
        '<:sa_cua:858201316560076800>',
        '<:sa_tom:858201639835009064>',
        '<:sa_ca:858201388105465856>',
        '<:sa_ga:858206854786187264>',
        '<:sa_nai:858201352123187200>',
    ]
    rd3 = [
        '<:sa_bau:858201209697730560>',
        '<:sa_cua:858201316560076800>',
        '<:sa_tom:858201639835009064>',
        '<:sa_ca:858201388105465856>',
        '<:sa_ga:858206854786187264>',
        '<:sa_nai:858201352123187200>',
    ]

    if message.content.startswith('sabc'):
        response1 = random.choice(rd1)
        response2 = random.choice(rd2)
        response3 = random.choice(rd3)
        ms = await message.channel.send('LOADING...')
        await asyncio.sleep(3)
        await ms.edit(content = response1 + ' ' + response2 + ' ' + response3)

client.run(os.environ['token'])