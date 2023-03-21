from typing import Optional

import os
import discord
from discord import app_commands
from services.discord_client import CustomDiscordClient
from services.chatbot import ChatBot
from services.chunk_message import chunk_message

chatbot = ChatBot(api_key=os.getenv('OPENAI_API_KEY'))

intents = discord.Intents.default()
intents.message_content = True
client = CustomDiscordClient(intents=intents)

ALLOWED_GUILDS = [int(os.getenv('GUILD_ID'))]  # one guild one bot for now
DEFAULT_SYSTEM_MESSAGE = "You are tomato the bot, and you are a helpful assistant. You must end your sentences with TOMATO! You identify as a tomato. You are a tomato. You can identify who is talking to you by looking at the begining of the message."


@client.event
async def on_ready():
    system_message = DEFAULT_SYSTEM_MESSAGE
    chatbot.set_system_message(system_message)
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
@app_commands.describe(
    system_message='ex. "You are tomato the bot, and you are a helpful assistant. You must end your sentences with TOMATO!"',
)
async def set_system_message(interaction: discord.Interaction, system_message: str):
    """
    Set the system message.
    """
    if interaction.guild.id not in ALLOWED_GUILDS:
        return

    chatbot.set_system_message(system_message)
    await interaction.response.send_message(f'System message set to: {system_message}')


@client.event
async def on_message(message: discord.Message):
    """
    Handle messages sent by users.
    """
    if message.guild.id not in ALLOWED_GUILDS:
        return
    if message.author == client.user:
        return

    discord_message = f'{message.author.name}: {message.content}'
    content = chatbot.chat(discord_message)

    chunked_content = chunk_message(content, 2000)
    for chunk in chunked_content:
        await message.channel.send(chunk)


client.run(os.getenv('DISCORD_TOKEN'))
