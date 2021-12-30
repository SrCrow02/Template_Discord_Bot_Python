import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

TOKEN = 'SEU_TOKEN'

client = commands.Bot(command_prefix = '!')
slash = SlashCommand(client, sync_commands = True)

@slash.slash(
	name = "Hello",
	description = "legal",
	guild_ids = [923310790025551972]
)
async def _hello(ctx:SlashContext):
	await ctx.send('Olá')

client.run(TOKEN)