import deepl, os
import discord
import logging
from discord.ext import commands
from discord import app_commands

# Token config
if 'DEEPL_TOKEN' in os.environ:
   deepl_token = os.environ['BOT_TOKEN']
else:
  with open('extensions/deepl_token', 'r') as file:
    deepl_token = file.read().strip()

TEST_GUILD_ID=1

class Translator(commands.Cog):
    def __init__(self, discord_client: commands.Bot):
        self.client = discord_client
        self.translator = deepl.Translator(deepl_token)

        @self.client.hybrid_command(name = "translate", description= "Translate a text to another language! ;)")
        @app_commands.describe(text="Text that you want to translate")
        @app_commands.describe(dest="Target language of the translation")
        async def translate(ctx: commands.Context, text: str, dest: str):
            try:
                result = self.translator.translate_text(text, target_lang=dest)
                await ctx.send(result.text)
            except deepl.DeepLException as e:
                logging.error(f"Translate error: {e}")
                await ctx.send(f"Oops, translation failed! {e}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Translator(bot))






