import os

from HB.startup import *

os.system("clear")


vars = """
APP_ID=
API_HASH=
BOT_TOKEN=
"""

opp = input(f"Want to fill vars ? if yes type Y/yes else press enter: ")
if opp.lower() in ["y", "yes"]:
    if not os.path.exists(".env"):
        y = open(".env", "w")
        y.write(vars)
        y.close()
        os.system("clear")
        LegendStartUP()
    elif os.path.exists(".env"):
        f = open(".env")
        check = f.read()
        print(check)
        f.close()
        check_again()
        if not len(lines) == 3:
            os.system("rm -rf .env")
            y = open(".env", "w")
            y.write(vars)
            y.close()
            os.system("clear")
            LegendStartUP()
        else:
            os.system("clear")
            LegendStartUP()
else:
    os.system("clear")
    os.system("python3 -m HackBot")
