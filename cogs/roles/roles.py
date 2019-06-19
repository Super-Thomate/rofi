import discord
from discord.ext import commands
import rolesconfig

class Roles(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    # self.roles = rolesconfig.roles
    self.roles = rolesconfig.roles_dev

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

    if (     not has_role (before, self.roles["work_team"])
         and not has_role (after, self.roles["work_team"])
         and (    has_role (after, self.roles["suf_work_team"])
               or has_role (after, self.roles["star_work_team"])
               or has_role (after, self.roles["ar_work_team"])
             )
       ):
      """ Must add role work_team
      """
      print ("MUST ADD work_team")
      role_to_add = after.guild.get_role(self.roles["work_team"])
      try:
        await after.add_roles(role_to_add)
      except Exception as e:
        print (f"ERROR: {type(e).__name__} - {e}")

    if (      has_role (before, self.roles["work_team"])
         and  has_role (after, self.roles["work_team"])
         and not (    has_role (after, self.roles["suf_work_team"])
                   or has_role (after, self.roles["star_work_team"])
                   or has_role (after, self.roles["ar_work_team"])
                 )
       ):
      """ Must remvove role work_team
      """
      print ("MUST REMOVE work_team")
      role_to_remove = after.guild.get_role(self.roles["work_team"])
      try:
        await after.remove_roles(role_to_remove)
      except Exception as e:
        print (f"ERROR: {type(e).__name__} - {e}")
  @commands.command(name="roles")
  async def print_roles(self, ctx, *, member: discord.Member = None):
    member = member or ctx.author
    for role in member.roles:
      if role.id == 494812563016777729:
        print (f"{member.name} as role everyone")
  