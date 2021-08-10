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
        '<:sa_bau:868698651894095943>',
        '<:sa_t6cua:868729524303593483>',
        '<:sa_tom:868698601482752010>',
        '<:sa_ca:868698726372360212>',
        '<:sa_ga:868695242650570792>',
        '<:sa_nai:874558023920660480>',
    ]
    rd2 = [
        '<:sa_bau:868698651894095943>',
        '<:sa_t6cua:868729524303593483>',
        '<:sa_tom:868698601482752010>',
        '<:sa_ca:868698726372360212>',
        '<:sa_ga:868695242650570792>',
        '<:sa_nai:874558023920660480>',
    ]
    rd3 = [
        '<:sa_bau:868698651894095943>',
        '<:sa_t6cua:868729524303593483>',
        '<:sa_tom:868698601482752010>',
        '<:sa_ca:868698726372360212>',
        '<:sa_ga:868695242650570792>',
        '<:sa_nai:874558023920660480>',
    ]

    if message.content.startswith('sabc'):
        response1 = random.choice(rd1)
        response2 = random.choice(rd2)
        response3 = random.choice(rd3)
        ms = await message.channel.send('LOADING...')
        await asyncio.sleep(3)
        await ms.edit(content = response1 + ' ' + response2 + ' ' + response3)

client.run(os.environ['token'])
