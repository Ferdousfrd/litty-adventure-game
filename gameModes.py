# this file contains all the game modes related functions

import os

#import slow_print
from ui import slow_print

# game mode selection
def gameModeSelect():

    # ask user for game mode
    gameMode = input(slow_print("Press 1 or 2 to start or Q to quit... ") or "")
    

    while gameMode not in ['1','2','q','Q']:
        print("\n" * 2)
        # dramatic taunt for invalid input
        slow_print("Zeez!!! 🥴")
        print()
        slow_print("You not that drunk right!!🍺🤦")
        print()
        slow_print("How hard is it to pick a choice between 1, 2 and Q ?? 💀")
        print()
        gameMode = input(slow_print("Press 1 or 2 to start or Q to quit YOU DONUT!!! ❌🧠") or "")
        

    if gameMode == '1':
        slow_print("\nWelcome to Solo Mode, Lone Wolf! 🐺")
        time.sleep(2)
        print("\n" * 2)
        soloMode()

    elif gameMode == '2':
        slow_print("\nWelcome to GangBang Mode! Let's get this party started! 🥳👯🍻")
    else:
        slow_print("\nGame Ended! Stay litty! 🍻✌️")
        quit()


# solo game play mode
from datetime import datetime
import time

def soloMode():
    """Solo player adventure mode"""

    # get current date and time
    now = datetime.now()

    # string formetting current date and time however we want
    currentTime = now.strftime("%I:%M %p")
    currentDate = now.strftime("%B %d, %Y")
    currentDay = now.strftime("%A")

    # clear the screen
    os.system('clear')

    print("\n" * 2)

    # intro story
    slow_print(f"📅 {currentDay}, {currentDate}")
    slow_print(f"🕐 {currentTime}")

    print()
    time.sleep(1)

    slow_print("You looking through the window 🌃\nThe night air is thick with mystery...")
    time.sleep(0.8)
    
    slow_print("You decided to go for a late-night jog to clear your head.")
    print("🫩")
    time.sleep(0.8)


    # animation of walking
    

    # Run left
    for i in range(15,0,-1):
        os.system('clear')
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        print()
        print(" " * i + "🏃💨")
        print()
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        time.sleep(0.15)  # Speed of animation
    
    os.system('clear')

    # Show scene
    print("\n🌙   ☁️  ☁️")
    print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
    
    print()
    slow_print("The moon hangs low in the sky, casting eerie shadows through the trees.")
    time.sleep(2)
    
    slow_print("Your breath creates small clouds in the cool air as you run 🌬️")
    time.sleep(2)

    os.system('clear')
    
    slow_print("The path ahead leads deeper into the forest...")
    print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
    print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲 🏃💨 ")
    print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
    time.sleep(1)
    
    slow_print("The trees seem to whisper secrets as you pass 🍃🍃")
    time.sleep(1)
    
    print("\n")
    slow_print("Suddenly...")
    time.sleep(1.5)
    
    slow_print("You hear a strange noise coming from the bushes! ")
    time.sleep(1)
    
    print("\n" * 2)


