import discord
from discord.ext import commands
import asyncio
import os
import sys

# Check if a token was provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python audiobladebot.py <Your_Bot_Token>")
    sys.exit(1)

bot_token = sys.argv[1]  # The first command-line argument after the script name

# Define the intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Instantiate the bot with the defined intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def playmidi(ctx):
    # Check if there is an attachment in the message
    if not ctx.message.attachments:
        await ctx.send("Please attach a MIDI file.")
        return

    # Download the MIDI file
    midi_file = ctx.message.attachments[0]
    file_name, file_extension = os.path.splitext(midi_file.filename)
    if file_extension.lower() != '.mid':
        await ctx.send("Please attach a MIDI file (.mid).")
        return
    await midi_file.save(midi_file.filename)

    # Convert MIDI to MP3
    output_file = file_name + '.mp3'
    conversion_command = f'timidity {midi_file.filename} -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k {output_file}'
    os.system(conversion_command)

    # Send the converted MP3 file
    with open(output_file, 'rb') as mp3:
        await ctx.send(file=discord.File(mp3, filename=output_file))

    # Cleanup
    os.remove(midi_file.filename)  # Delete the original MIDI file
    os.remove(output_file)  # Delete the converted MP3 file

# Run the bot
bot.run(bot_token)

