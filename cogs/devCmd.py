import discord
from discord.ext import commands

class DevCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="loadcogs")
  async def load(ctx, self, extension):
    self.bot.load_extension(f"cogs.{extension}")

  @commands.command(name="unload")
  async def unload(ctx, self, extension):
    self.bot.unload_extension(f"cogs.{extension}")
  
  @commands.command(name="reload")
  async def reload(ctx, self, extension):
    self.bot.unload_extension(f"cogs.{extension}")
    self.bot.load_extension(f"cogs.{extension}")

def setup(bot):                 #STETUP START
	bot.add_cog(DevCommands(bot))      #ADDING THE CLASS NAME "BLASTY" AS A COG