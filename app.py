import discord
import os
from dotenv import load_dotenv

load_dotenv()

app = discord.Client() 

@app.event
async def on_ready():
  print("Bot esta online")

@app.event
async def on_message(message):
  if message.author == app.user:
    return
  
  # Check if message has an image
  if not len(message.attachments) > 0:
    return

  if message.channel.id == 1003185959405375498:
    await message.channel.send("Oi")

app.run(os.getenv('BOT_TOKEN'))