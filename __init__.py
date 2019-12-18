import discord
import website
import replit
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

website.start()
time.sleep(2)
replit.clear()

@client.event
async def on_ready():
    channels = [653711820439420928, 591815679594856570]
    for x in channels:
       channel = client.get_channel(x)
       await channel.send('Bob is back online!')
    print('Logged in as ' + client.user.name + ' (' + str(client.user.id) + ')')


client.run('NjUzNzEwODAyNTQ4Njg2ODY5.Xe74tg.q966ITgprLBBaSgpT44PH3A9Gw0')
