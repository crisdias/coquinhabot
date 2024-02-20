import random
import datetime
import discord

from dotenv import load_dotenv
import os

from amazon import get_asin_from_link, extract_amazon_url, amazon_tagger, add_affiliate_tag_to_product, get_item
from bitly  import bitly_shorten
from utils  import pp

load_dotenv()
TOKEN     = os.getenv("TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")


# read config/frases.txt into array
with open('data/frases.txt', 'r') as f:
    frases = f.readlines()

if len(frases) == 0:
    frases = [""]

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.reactions = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    # exit if message is from bot
    if message.author == client.user:
        return 1

    if message.author.name.startswith('crisdias'):
        return 1

    amznurl = extract_amazon_url(message.content)
    if amznurl:
        asin = get_asin_from_link(amznurl)
        if asin:
            url = add_affiliate_tag_to_product(asin)
        else:
            url = amazon_tagger(amznurl)

        shorturl = bitly_shorten(url)


        pp(f'amznurl: {amznurl}')
        pp(f'url: {url}')
        pp(f'shorturl: {shorturl}')
        print('\n\n')

        frase = frases[random.randint(0, len(frases)-1)]

        await message.channel.send(frase + "\n" + shorturl)

        await message.edit(suppress=True)

    return 1









print(f'https://discordapp.com/api/oauth2/authorize?client_id={CLIENT_ID}&permissions=10304&scope=bot')

@client.event
async def on_ready():
    print(f'\n\n\n\n\n\n\nWe have logged in as {client.user}')
    print(datetime.datetime.now())
    print('\n\n\n\n\n\n\n')

client.run(TOKEN)

