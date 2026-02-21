# this file contains all the ui related functions

import time, pygame


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

# make sure player has the game pacing
def wait_for_player():
    """Pause and wait for player to press any key"""
    input("\n[Press Enter to continue...]")


# initialize music system
pygame.mixer.init()


def play_background_music():
    """Start playing background music on loop"""
    try:
        pygame.mixer.music.load('spooky.mp3')
        pygame.mixer.music.set_volume(0.3)  # 30% volume (not too loud)
        pygame.mixer.music.play(-1)  # -1 means loop forever
    except:
        pass  # if music file not found, game still works


def stop_music():
    """Stop the background music"""
    try:
        pygame.mixer.music.stop()
    except:
        pass
