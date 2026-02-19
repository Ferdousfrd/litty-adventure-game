# this file contains all the ui related functions

import time

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