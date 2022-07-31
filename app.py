import discord
import os
from dotenv import load_dotenv

load_dotenv()

app = discord.Client() 

@app.event
async def on_ready():
  print("Bot esta online")

app.run(os.getenv('BOT_TOKEN'))