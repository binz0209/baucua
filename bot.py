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
        '<:sa_bau:874564299203436544>',
        '<:sa_cua:874564374457634826>',
        '<:sa_tom:874564456988954634>',
        '<:sa_ca:874564511057739796>',
        '<:sa_ga:874564337883295785>',
        '<:sa_nai:874564413577891870>',
    ]
    rd2 = [
        '<:sa_bau:874564299203436544>',
        '<:sa_cua:874564374457634826>',
        '<:sa_tom:874564456988954634>',
        '<:sa_ca:874564511057739796>',
        '<:sa_ga:874564337883295785>',
        '<:sa_nai:874564413577891870>',
    ]
    rd3 = [
        '<:sa_bau:874564299203436544>',
        '<:sa_cua:874564374457634826>',
        '<:sa_tom:874564456988954634>',
        '<:sa_ca:874564511057739796>',
        '<:sa_ga:874564337883295785>',
        '<:sa_nai:874564413577891870>',
    ]

    if message.content.startswith('sabc'):
        response1 = random.choice(rd1)
        response2 = random.choice(rd2)
        response3 = random.choice(rd3)
        ms = await message.channel.send('LOADING...')
        await asyncio.sleep(3)
        await ms.edit(content = response1 + ' ' + response2 + ' ' + response3)

client.run(os.environ['token'])
