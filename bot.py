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
        '<:sa_bau:874560822108622878>',
        '<:sa_cua:874560348072607744>',
        '<:sa_tom:874560189016186951>',
        '<:sa_ca:874560654873362472>',
        '<:sa_ga:874560001350451312>',
        '<:sa_nai:874559850863005756>',
    ]
    rd2 = [
        '<:sa_bau:874560822108622878>',
        '<:sa_cua:874560348072607744>',
        '<:sa_tom:874560189016186951>',
        '<:sa_ca:874560654873362472>',
        '<:sa_ga:874560001350451312>',
        '<:sa_nai:874559850863005756>',
    ]
    rd3 = [
        '<:sa_bau:874560822108622878>',
        '<:sa_cua:874560348072607744>',
        '<:sa_tom:874560189016186951>',
        '<:sa_ca:874560654873362472>',
        '<:sa_ga:874560001350451312>',
        '<:sa_nai:874559850863005756>',
    ]

    if message.content.startswith('sabc'):
        response1 = random.choice(rd1)
        response2 = random.choice(rd2)
        response3 = random.choice(rd3)
        ms = await message.channel.send('LOADING...')
        await asyncio.sleep(3)
        await ms.edit(content = response1 + ' ' + response2 + ' ' + response3)

client.run(os.environ['token'])
