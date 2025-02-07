import discord
import random
import os
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
client = discord.Client(intents=intents)

processed_messages = set()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for @someone"))
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.id in processed_messages:
        return

    processed_messages.add(message.id)

    if "@someone" in message.content.lower():
        members = [m for m in message.guild.members if not m.bot]
        if members:
            random_member = random.choice(members)

            try:
                await message.reply(f"{random_member.mention}")

            except discord.errors.HTTPException as e:
                print(f"Rate limit error: {e}")
                await asyncio.sleep(10)
                return

client.run(TOKEN)