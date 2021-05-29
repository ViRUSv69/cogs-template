from discord.ext import commands

class Blasty(commands.Cog):
	def __init__(self, bot):      #INITAILIZING
		self.bot = bot              

	@commands.command(name="bot")
	async def name(self, ctx):
		bot_name = self.bot.user.name
		await ctx.send(f"My name is {bot_name}") 

def setup(bot):                 #STETUP START
	bot.add_cog(Blasty(bot))      #ADDING THE CLASS NAME "BLASTY" AS A COG