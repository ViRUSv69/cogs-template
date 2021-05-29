#----------------------------------------------HEADER-FILES<
import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')
#-----------------------------------------------MAINCODE<
#--------------------COGS-----------------------
'''ADD COGS HERE!!!!'''
cogs = ["cogs.blasty", "cogs.devCmd"] #             EACH FILE NAME OF THE COG IN THE FORMAT --> "FOLDER_NAME.FILE_NAME",

@bot.event
async def on_ready():
	print("The bot is ready!")                
	print("Loading cogs . . .")               
	for cog in cogs:                          
		try:                                  
			bot.load_extension(cog)           
			print(cog + " was loaded.")       
		except Exception as e:                
			print(e)
#-------------------------------------------devCommands<
#-----------------PING-----------------------------
#@bot.command(name="ping")
#async def ping(ctx: commands.Context):
#  await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")        
#---------------------------------------------RUNNER<
token = os.environ.get("TOKEN")
bot.run(token, reconnect = True, bot = True)