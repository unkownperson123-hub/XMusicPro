# Copyright (C) 2021-2022 by TeamYukki@Github
# Modified for Heroku (Git functionality disabled)

# NOTE:
# Git features removed because Heroku environment does not support git runtime commands.
# This will NOT affect music bot functionality.

def install_req(cmd):
    # Disabled (not required on Heroku)
    return ("", "", 0, 0)


def git():
    # Disabled git updater (safe for Heroku)
    return
