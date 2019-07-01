import discord
from discord.ext import commands
import rolesconfig

class Roles(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.roles = rolesconfig.roles
    # self.roles = rolesconfig.roles_dev

  @commands.Cog.listener('on_member_update')
  async def handle_update(self, before, after):
    """ Triggered every time a user is updated
        we only need to do something if
        roles are updated
    """
    def has_role (member, role_id):
      for role in member.roles:
        if role.id == role_id:
          return True
      return False
    def get_new_nick (member):
      new_nick = member.display_name.replace('🔥','').replace('⭐','').replace('💖','').replace ('🚋', '')
      if has_role (member, self.roles["ar"]):
        new_nick += " 🔥"
      if has_role (member, self.roles["suf"]):
        new_nick += " ⭐"
      if has_role (member, self.roles["star"]):
        new_nick += " 💖"
      if has_role (member, self.roles["train"]):
        new_nick += " 🚋"
      return new_nick
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

    if (    (not has_role (before, self.roles["ar"])   and has_role (after, self.roles["ar"]))
         or (not has_role (before, self.roles["suf"])  and has_role (after, self.roles["suf"])) 
         or (not has_role (before, self.roles["star"]) and has_role (after, self.roles["star"]))
         or (not has_role (before, self.roles["train"]) and has_role (after, self.roles["train"]))
         or (has_role (before, self.roles["ar"])   and not has_role (after, self.roles["ar"]))
         or (has_role (before, self.roles["suf"])  and not has_role (after, self.roles["suf"]))
         or (has_role (before, self.roles["star"]) and not has_role (after, self.roles["star"]))
         or (has_role (before, self.roles["train"]) and not has_role (after, self.roles["train"]))
       ):
      """ add/remove emoji
      """
      print ("add/remove emoji")
      try:
        await after.edit(nick= get_new_nick (after))
      except Exception as e:
        print (f"ERROR: {type(e).__name__} - {e}")
  """
  @commands.command(name="roles")
  async def print_roles(self, ctx, *, member: discord.Member = None):
    member = member or ctx.author
    for role in member.roles:
      if role.id == 494812563016777729:
        print (f"{member.name} as role everyone")
  """