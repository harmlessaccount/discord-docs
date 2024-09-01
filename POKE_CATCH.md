# Poké Catcher submitted by [@StrawberryChemical95](https://github.com/StrawberryChemical95)

This will teach you how to check for message edits, send slash commands and applying button pressing. Use this with caution as you may be banned on the target bot. [Bot invite](https://discord.com/oauth2/authorize?client_id=707333868713410682&permissions=2147863616&scope=bot%20applications.commands).

# Automation Script

```
import discord
from discord.ext import commands
import asyncio
import random
import schedule
import datetime
import time
import threading

# Assign your Discord User token
Token = "TOKEN"

# Assign the channel you'd like to run the bot in.
channel_id = 123456789012345678

# Command IDs
pokemon_id = 1067810369541779589
pokestop_id = 1067810369541779590


# Simple function to add variance to your asyncio.sleeps
async def sleeper(base, variation) -> None:
    await asyncio.sleep(base + random.uniform(.25, variation))
    return


class Client(discord.Client):
    def __init__(self, client, catches):
        super().__init__()
        self.messagechannel = None
        self.client = None
        self.catchable = catches

    async def on_ready(self):
        # Fetch the channel run commands in
        self.messagechannel = await self.client.fetch_channel(channel_id)

        # Get the commands to run
        self.commands = await self.messagechannel.application_commands()
        self.pokemon = [i for i in self.commands if i.id == pokemon_id]
        self.pokestop = [i for i in self.commands if i.id == pokestop_id]
        print('Logged on')

        # Check if the hour is a multiple of 3, if it is, run /pokestop
        current_hour = datetime.datetime.now().hour
        if current_hour % 3 == 0:
            await self.pokestops()

        await asyncio.sleep(10)

        # Send the first /pokemon command, which will trigger the loop.
        # Only 10 pokemon can be spawned per hour.
        await self.pokemon[0].__call__(channel=channel_id)

    # Run the command /pokestop to get free pokeballs (once every 3 hours)
    async def pokestops(self):
        await asyncio.sleep(3)
        await self.pokestop[0].__call__(channel=channel_id)

    async def on_message_edit(self, before, after):
        if before or after:
            if after.channel.id == channel_id:
                # Catch a Spawned Pokemon
                for i in after.components:
                    for j in i.children:
                        if j.label == 'Catch':
                            await sleeper(2.5, 5.5)
                            await j.click()
                            self.catchable -= 1

                        # When number of spawns/catches reaches 0, stop the bot.
                        if self.catchable == 0:
                            await self.client.close()

                        # Roll Again
                        if j.label == 'Roll Again':
                            if self.catchable > 0:
                                await sleeper(2.5, 5.5)
                                await j.click()
                                if self.catchable == 0:
                                    await self.client.close()


def initialize_and_run_task():
    # Add a random delay when running the script, (number of spawns resets at XX:00, so we can run it anytime within the hour)
    seconds_delay = random.randint(1, 35) * random.randint(50, 60)
    print(f"{seconds_delay}s until code executes")
    time.sleep(seconds_delay)

    client = Client(client=None, catches=10)  # Only 10 pokemon can be spawned per hour
    client.client = client  # Assigning the client instance to itself

    # Run the bot within a thread, so it doesn't interfere with the scheduler
    print("Running Catcher!")
    bot_thread = threading.Thread(target=client.run, args=(Token,))
    bot_thread.start()
    print("Thread over")


# Schedule the bot to run every hour.
def schedule_task():
    current_hour = datetime.datetime.now().hour
    if 7 <= current_hour < 23:  # Only run the bot between 7AM and 11PM (07:00 -> 23:00)
        initialize_and_run_task()


# Schedule the job every hour at minute 5
schedule.every().hour.at(":05").do(schedule_task)

print("Task has been Scheduled!")
print(f"Current Time: {datetime.datetime.now()}")

# Loop to rerun the bot every hour
while True:
    schedule.run_pending()
    time.sleep(5)
```

The bot should take a while to start due to how it handles cooldowns. If this worked, your bot should run `/pokemon` ten times every hour, and also run `/pokestop` every three hours. Thanks again [@StrawberryChemical95](https://github.com/StrawberryChemical95) for the submission.
