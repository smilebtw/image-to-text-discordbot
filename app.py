import discord
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = discord.Client() 

@app.event
async def on_ready():
  print("Bot esta online")

@app.event
async def on_message(message):
  if message.channel.id == 1003185959405375498:
    if message.author == app.user:
      return
    
    # Check if message has an image
    if not len(message.attachments) > 0:
      return

    try:
      image = requests.get(message.attachments[0].url).content
      with open('discord_image.png', 'wb') as handler:
        handler.write(image)
    except:
        return await message.channel.send('Houve um erro ao tentar baixar a imagem')
        
    emote = '✅'
    await message.add_reaction(emote)
    
app.run(os.getenv('BOT_TOKEN'))