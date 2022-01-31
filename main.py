
import discord
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config")



client = discord.Client()
client.run(os.getenv("TOKEN"))

@client.event
async def on_ready():
    print("Le bot est prêt !")

async def on_message(message):
    print(message.content)