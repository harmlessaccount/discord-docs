# Automating Tasks on UnbelievaBot

This will teach you how to fetch embeds
## Automation Script

Create a file named `unbelieva.py`:

```
# unbelieva.py
import discord
from discord.ext import commands, tasks
import re
import asyncio

bot = commands.Bot(command_prefix='>', self_bot=True)
token = "TOKEN INSIDE HERE"  # Paste your account token here
channelId = 123  # Paste the channel ID here
botId = 123  # Target the bot ID so we don't fetch messages from other bot's embeds.

# Constants
totalGained = 0
workLoopTask = None  # Keeping track of the work loop task.

# Background task to send !work message every 30 seconds
async def workLoop():
    global workLoopTask
    await bot.wait_until_ready()
    channel = bot.get_channel(channelId)
    if channel is None:
        print("Channel not found!")
        return
    while not bot.is_closed():
        await channel.send('!work')
        await asyncio.sleep(30)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def start(ctx):
    global workLoopTask
    if workLoopTask and not workLoopTask.done():
        await ctx.send('The task is already running.')
        return

    workLoopTask = bot.loop.create_task(workLoop())
    await ctx.send('Started sending !work messages every 30 seconds.')

@bot.listen('on_message')
async def on_message(message):
    if message.author.id != botId or message.channel.id != channelId:
        return

    try:
        fetchedMessage = await message.channel.fetch_message(message.id)

        if not fetchedMessage.embeds:
            print('Embed without description.')
            return

        for embed in fetchedMessage.embeds:
            # Checks if Unbelieva is mentioning the bot or some other user
            if bot.user.name in embed.author.name:
                description = embed.description
                if description:
                    numbers = re.findall(r'\d+', description)
                    for number in numbers:
                        amount = int(number)
                        if len(number) != 18:  # Ignore emoji IDs, bandage.
                            global totalGained
                            totalGained += amount
                            print(f'Amount gained: {amount}')
                            print(f'Total gained so far: {totalGained}')
            else:
                print("Other user's gains.")

    except Exception as e:
        print(f'Error: {e}')

    await bot.process_commands(message)

@bot.command()
async def total(ctx):
    await ctx.send(f'Total gained so far: {totalGained}')

bot.run(token)

```

a
