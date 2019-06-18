from .invitation import Invitation

def setup(bot):
  bot.add_cog(Invitation(bot))