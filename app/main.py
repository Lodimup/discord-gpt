import os
import discord
from discord import app_commands
from services.discord_client import CustomDiscordClient
from services.chatbot import ChatBot
from services.chunk_message import chunk_message
from services.env_man import ENVS

ALLOWED_GUILDS = [ENVS['GUILD_ID']]  # one guild one bot for now
DEFAULT_SYSTEM_MESSAGE = ENVS['DEFAULT_SYSTEM_MESSAGE']
OPENAI_API_KEY = ENVS['OPENAI_API_KEY']

chatbot = ChatBot(api_key=OPENAI_API_KEY)
intents = discord.Intents.default()
intents.message_content = True
client = CustomDiscordClient(intents=intents)


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

    if os.getenv('PREPEND_USERNAME') is True:
        discord_message = f'{message.author.name}: {message.content}'
    else:
        discord_message = message.content

    content = chatbot.chat(discord_message)

    chunked_content = chunk_message(content, 2000)
    for chunk in chunked_content:
        await message.channel.send(chunk)


client.run(ENVS['DISCORD_TOKEN'])
