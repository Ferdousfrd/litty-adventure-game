# a drinking game with mystery and adventure to enjoy with friends 

import os
import time

from ui import welcomeScreen
from gameModes import gameModeSelect

os.system('clear')  # will clear the screen or terminal first


def main():
    welcomeScreen()
    gameModeSelect()

    




# checking if we running main
if __name__ == "__main__":
    main()
