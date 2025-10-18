import discord
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def get_random_meme_from_meme_api():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
    
  async def on_message(self, message):
    if message.author == self.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')
    
    if message.content.startswith('$meme'):
        await message.channel.send(get_random_meme_from_meme_api())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(f'{os.getenv('DISCORD_TOKEN')}')