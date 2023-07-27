import os
import discord
import deepl
import logging
from discord.ext import commands
from discord import app_commands
from colorama import Fore


# Token config
if 'BOT_TOKEN' in os.environ:
   token = os.environ['BOT_TOKEN']
else:
  with open('token', 'r') as file:
    token = file.read().strip()

# Intents config
INTENTS = discord.Intents.all()
INTENTS.message_content = True
INTENTS.guild_messages = True
INTENTS.dm_messages = True
INTENTS.members = True

# Logger config
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class Client(commands.Bot):
  def __init__(self):
    super().__init__(command_prefix="!", intents=INTENTS)


  async def setup_hook(self) -> None:
    extensions_dir = "extensions"

    for filename in os.listdir(extensions_dir):
      if filename.endswith('.py'):
        await client.load_extension(f'{extensions_dir}.{filename[:-3]}')
        print(f"Extension " +  Fore.RED + filename + Fore.RESET + " was loaded")

  async def on_ready(self):

    # Welcome message in the logger
    print(""""
 _       __     __                             __           ____        __  _ ____      __
| |     / /__  / /________  ____ ___  ___     / /_____     / __ )____  / /_(_) / /___  / /_
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \   / __  / __ \/ __/ / / / __ \/ __ \\
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /  / /_/ / /_/ / /_/ / / / /_/ / / / /
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   \__/\____/  /_____/\____/\__/_/_/_/\____/_/ /_/  developed by Villoh
""")

    print("Logged in as " + Fore.RED + str(self.user) + Fore.RESET)
    # synced = await self.tree.sync()
    # print(" Slash CMDs Synced " + Fore.RED + str(len(synced)) + " Commands" + Fore.RESET)

  async def on_message(self, message):
    # do some extra stuff here
    print(str(message) + "\n")
    await client.process_commands(message)

client = Client()

@client.hybrid_command(name = "ping", description = "Pings the discord server to see the bot status.")
async def ping(ctx: commands.Context):
    try:
      await ctx.send(f"``Pong! {round(client.latency * 1000)}ms``  📡")
    except discord.errors.HTTPException or discord.errors.Forbidden as e:
      print("Exception: ", e)


@client.hybrid_command(name = "sync", description = "Synchronize all the commands with the discord client server.")
@commands.has_permissions(administrator = True)
async def sync(ctx: commands.Context):
    try:
      synced = await client.tree.sync()
      print("Slash CMDs Synced " + Fore.RED + str(len(synced)) + " Commands" + Fore.RESET)
      await ctx.send("Slash CMDs Synced " + str(len(synced)) + " Commands", ephemeral=True)
    except discord.errors.HTTPException or discord.errors.Forbidden as e:
      print("Exception: ", e)


client.run(token)