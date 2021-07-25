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
        '<:sa_bau:868714371960958977>',
        '<:sa_cua:868715725576089610>',
        '<:sa_tom:868714377484857364>',
        '<:sa_ca:868714430563762186>',
        '<:sa_ga:868714484624150558>',
        '<:sa_nai:868714503171350578>',
    ]
    rd2 = [
        '<:sa_bau:868714371960958977>',
        '<:sa_cua:868715725576089610>',
        '<:sa_tom:868714377484857364>',
        '<:sa_ca:868714430563762186>',
        '<:sa_ga:868714484624150558>',
        '<:sa_nai:868714503171350578>',
    ]
    rd3 = [
        '<:sa_bau:868714371960958977>',
        '<:sa_cua:868715725576089610>',
        '<:sa_tom:868714377484857364>',
        '<:sa_ca:868714430563762186>',
        '<:sa_ga:868714484624150558>',
        '<:sa_nai:868714503171350578>',
    ]

    if message.content.startswith('sabc'):
        response1 = random.choice(rd1)
        response2 = random.choice(rd2)
        response3 = random.choice(rd3)
        ms = await message.channel.send('LOADING...')
        await asyncio.sleep(3)
        await ms.edit(content = response1 + ' ' + response2 + ' ' + response3)

client.run(os.environ['token'])