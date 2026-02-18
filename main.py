# a drinking game with mystery and adventure to enjoy with friends 

import os
import time

os.system('clear')  # will clear the screen or terminal first


def main():
    welcomeScreen()
    gameModeSelect()


# slow print for dramatic effect
def slow_print(text, delay=0.05):
    """Prints text character by character with a delay"""
    for char in text:  # Loop through each character
        print(char, end='', flush=True)  # Print without newline, show immediately
        time.sleep(delay)  # Pause for 'delay' seconds
    print()  # Add newline at the end


# welcome screen
def welcomeScreen():
    print("          ══════════════════════════════════════════")
    print("          ║                                        ║")
    print("          ║        🍻 LITTY ADVENTURE 🍻           ║")
    print("          ║                                        ║")
    print("          ║    Get lost in mystery and booze!!!    ║")
    print("          ║                                        ║")
    print("          ══════════════════════════════════════════")

    print("\n" * 2)

    print("              1. Solo adventure (Lone Wolf Mode) 🙃                    ")
    print()
    print("              2. GangBang adventure (Squad Goals) 🎉   ")

    print("\n" * 2)

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
    elif gameMode == '2':
        slow_print("\nWelcome to GangBang Mode! Let's get this party started! 🥳👯🍻")
    else:
        slow_print("\nGame Ended! Stay litty! 🍻✌️")
        quit()

# checking if we running main
if __name__ == "__main__":
    main()
