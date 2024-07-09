import pyshorteners
import discord
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)
class GenUrl:
    def __init__(self, original_url):
        self.original_url = original_url
        self.type_tiny = pyshorteners.Shortener()
        self.new_url = self.type_tiny.tinyurl.short(self.original_url)
    def generate_new_url(self):
        return self.new_url
@client.event
async def on_ready():
    print(f"bot is ready as {client.user}")
@client.command()
async def generate(ctx, original_url: str):
    try:
        gen_url_instance = GenUrl(original_url)
        new_url = gen_url_instance.generate_new_url()
        await ctx.send(f"New url is: {new_url}")
    except Exception as e:
        await ctx.send(f"Use this format: .generate your_url\nerror is {e}")
client.run("your_token_goes_here")