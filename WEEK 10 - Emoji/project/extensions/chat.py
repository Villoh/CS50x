import discord, logging
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class Chat(commands.Cog):
    def __init__(self, discord_client: commands.Bot):
        self.client = discord_client

        @self.client.hybrid_command(name="purge", description="Deletes specified number of messages")
        @app_commands.describe(amount="Number of message(s) to delete")
        @app_commands.describe(before="Delete message(s) before this date. Format: dd-mm-YYYY")
        @app_commands.describe(after="Delete message(s) after this date. Format: dd-mm-YYYY")
        @commands.has_permissions(manage_messages = True)
        async def purge(ctx: commands.Context, amount: int, before = None, after = None):

            try:
                msg_count = 0
                async for message in ctx.channel.history(limit=None):
                    msg_count += 1
                if not ctx.channel.permissions_for(ctx.guild.me).manage_messages:
                    await ctx.send("You don't have enough permissions.", ephemeral=True)
                    return
                elif amount < 1 or amount > 100:
                    await ctx.send("You need to enter a value between 1 and 100.", ephemeral=True)
                    return
                elif amount > msg_count:
                    await ctx.send("You are trying to delete more messages than there are in the chat.", ephemeral=True)
                    return

                before_date = datetime.strptime(before, "%d-%m-%Y") if before else None
                after_date = datetime.strptime(after, "%d-%m-%Y") if after else None

                await ctx.defer()
                deleted = await ctx.channel.purge(limit = amount + 1, before=before_date, after=after_date)

                if len(deleted) == 0:
                    # If no messages were deleted, create an embed message with a custom color and text
                    embed = discord.Embed(title='Purge completed  🧹', color=0xFFFF00)
                    embed.description = 'No messages were deleted. \n Purge made by {ctx.author}'
                    # Set the user's profile picture as the thumbnail of the embed
                    embed.set_thumbnail(url=ctx.author.avatar.url)
                    # Send the embed message
                    await ctx.channel.send(embed=embed)
                else:
                    # Create an embed message with a custom color and text
                    embed = discord.Embed(title='Purge completed  🧹', color=0xFFFF00)
                    # If more than one message was deleted, use plural text
                    embed.description = f'{len(deleted)-1} message(s) were deleted. \n Purge made by {ctx.author}'
                    # Set the user's profile picture as the thumbnail of the embed
                    embed.set_thumbnail(url=ctx.author.avatar.url)
                    # Send the embed message
                    await ctx.channel.send(embed=embed)
            except discord.errors.NotFound as nf:
                logging.error(f"Message mnot found. Error: {nf}")
                await ctx.send(f"Message mnot found. Error: {nf}", ephemeral=True)
            except discord.errors.Forbidden as f:
                logging.error(f"You don't have enough permissions for this. Error: {f}")
                await ctx.send(f"You don't have enough permissions for this. Error: {f}", ephemeral=True)
            except Exception as e:
                logging.error(f"Error while parsing dates. Error: {e}")

        # @self.client.tree.command(name="delete_message_id", description="Deletes a message by the id")
        # @app_commands.describe(message_id="Id off the message to delete")
        # async def delete(interaction: discord.Interaction, message_id: str):



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Chat(bot))
