import discord
from discord.ext import commands


class Roles(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_member_update')
  async def handle_update(self, before, after):
    """ Triggered every time a user is updated
        we only need to know to continue if
        a role is updated
    """
    return
  @commands.command(name="roles")
  async def print_roles(self, ctx):
    print (ctx.author.roles)
