import discord
import botconfig
from discord.ext import commands

class Invitation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='invite')
  async def hello(self, ctx, member: discord.Member = None):
    """Send the invitation's link in a DM"""
    member = member or ctx.author
    try:
      await member.send (botconfig.config['invite_bot'])
    except:
      await ctx.send ('Oups je ne peux pas envoyer de DM !')
  
  @commands.Cog.listener('on_message')
  async def invitation(self, message):
    """ Send the invitation's link in a DM
        if the word 'invitation' is found
    """
    if "invitation" in message.content.lower():
      member = message.author
      try:
        await member.send (botconfig.config['invite_bot'])
      except:
        await message.channel.send ('Oups je ne peux pas envoyer de DM !')
    