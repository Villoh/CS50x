import discord, logging, aiohttp
from discord.ext import commands
from discord import app_commands

class Weather(commands.Cog):
    def __init__(self, discord_client: commands.Bot):
        self.client = discord_client

        @self.client.hybrid_command(name="weather", description="Sends an interactive calculator")
        @app_commands.describe(location="Specific location where you want to get the information from.")
        @app_commands.describe(language="Language . Eg. es, fr, en...")
        async def weather(ctx: commands.Context, location: str, language: str):
            languages = [
                'am', 'ar', 'af', 'be', 'bn', 'ca', 'da', 'de', 'el', 'et', 'fr',
                'fa', 'gl', 'hi', 'hu', 'ia', 'id', 'it', 'lt', 'mg', 'nb', 'nl',
                'oc', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'ta', 'tr', 'th', 'uk', 'vi',
                'zh-cn', 'zh-tw', 'az', 'bg', 'bs', 'cy', 'cs', 'eo', 'es', 'eu',
                'fi', 'ga', 'hi', 'hr', 'hy', 'is', 'ja', 'jv', 'ka', 'kk', 'ko',
                'ky', 'lv', 'mk', 'ml', 'mr', 'nl', 'fy', 'nn', 'pt', 'pt-br', 'sk',
                'sl', 'sr', 'sr-lat', 'sv', 'sw', 'te', 'uz', 'zh', 'zu', 'he'
            ]

            if language.lower() not in languages:
                await ctx.send("The entered language is not available. Sorry :( )")
                return

            embed = discord.Embed(title=f'Weather in {location.lower()}', color=0xFFFF00)
            # Set the user's profile picture as the thumbnail of the embed
            embed.set_image(url = f'https://wttr.in/{location}.png?lang={language}&m')
            # Send the embed message
            await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Weather(bot))