import discord
import random
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if "@someone" in message.content.lower():
        members = [m for m in message.guild.members if not m.bot]
        if members:
            random_member = random.choice(members)

            thread = await message.create_thread(
                name=f"@{random_member.name} was pinged by this bot.",
                auto_archive_duration=60,
                reason="Pinged a random user"
            )

            await thread.send(f"You were pinged randomly in the message by {message.author.mention}!")

            await message.reply(f"{random_member.mention}")

client.run(TOKEN)
