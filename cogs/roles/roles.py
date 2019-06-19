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
    def has_role (member, role_id):
      for role in member.roles:
        if role.id == role_id:
          return True
      return False
    
    return
  @commands.command(name="roles")
  async def print_roles(self, ctx, *, member: discord.Member = None):
    member = member or ctx.author
    for role in member.roles:
      if role.id == 494812563016777729:
        print (f"{member.name} as role everyone")
  