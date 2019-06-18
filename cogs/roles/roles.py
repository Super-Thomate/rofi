import discord
from discord.ext import commands


class Roles(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_member_update')
  async def handle_update(self, before, after):
    """ Triggered every time a user is updated
    """

