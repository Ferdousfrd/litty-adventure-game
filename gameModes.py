# this file contains all the game modes related functions

import os, random
from datetime import datetime
import time
from ui import slow_print, wait_for_player


def gameModeSelect():
    """Select between solo and group modes"""
    gameMode = input(slow_print("Press 1 or 2 to start or Q to quit... ") or "")
    
    while gameMode not in ['1','2','q','Q']:
        print("\n" * 2)
        slow_print("Zeez!!! 🥴")
        print()
        slow_print("You not that drunk right!!🍺🤦")
        print()
        slow_print("How hard is it to pick a choice between 1, 2 and Q ?? 💀")
        print()
        gameMode = input(slow_print("Press 1 or 2 to start or Q to quit YOU DONUT!!! ❌🧠") or "")
        
    if gameMode == '1':
        soloMode()
    elif gameMode == '2':
        os.system('clear')
        slow_print("\nWelcome to GangBang Mode! Let's get this party started! 🥳👯🍻")
    else:
        slow_print("\nGame Ended! Stay litty! 🍻✌️")
        quit()


def soloMode():
    """Solo player adventure mode - main entry point"""
    show_intro()
    first_choice = forest_noise_scene()
    
    # track player items for ending
    has_key = False
    has_map = False
    
    if first_choice == 'a':
        has_key = investigate_bushes()
    else:
        has_map = find_cabin()
    
    # final treasure scene
    final_treasure_hunt(has_key, has_map)


def show_intro():
    """Show game intro with date/time and running animation"""
    now = datetime.now()
    currentTime = now.strftime("%I:%M %p")
    currentDate = now.strftime("%B %d, %Y")
    currentDay = now.strftime("%A")
    
    os.system('clear')
    print()
    slow_print(f"📅 {currentDay}, {currentDate}")
    slow_print(f"🕐 {currentTime}")
    print()
    time.sleep(1)
    
    slow_print("You looking through the window 🌃\nThe night air is thick with mystery...")
    time.sleep(0.8)
    
    slow_print("You decided to go for a late-night jog to clear your head.")
    print("🫩")
    slow_print("\nYou need to hydrate yourself before jog. TAKE 2 sips!!🍺🍺 ")
    wait_for_player()

    
    # animation of walking - Run left
    for i in range(15,0,-1):
        os.system('clear')
        print()
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        print()
        print(" " * i + "🏃💨")
        print()
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        time.sleep(0.45)
    
    os.system('clear')
    
    # Show scene
    print()
    print("🌙   ☁️  ☁️")
    print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
    print()
    slow_print("The moon hangs low in the sky, casting eerie shadows through the trees.")
    time.sleep(2)
    
    slow_print("Your breath creates small clouds in the cool air as you run 🌬️")
    time.sleep(2)
    
    os.system('clear')
    print()
    
    slow_print("The path ahead leads deeper into the forest...")
    print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
    print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲 🏃💨 ")
    print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
    time.sleep(2)
    
    slow_print("The trees seem to whisper secrets as you pass 🍃🍃")
    time.sleep(1)
    
    os.system('clear')
    print()
    slow_print("Then suddenly... You had to stop.")
    time.sleep(1.5)


def forest_noise_scene():
    """Player hears noise in forest - returns choice 'a' or 'b'"""
    os.system('clear')
    print()
    print("🌙   ☁️  ☁️")
    print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
    print()
    print(" " * 15 + "🧍‼️")
    time.sleep(1)
    print()
    
    slow_print("You hear a strange noise coming from the bushes! 🪾")
    time.sleep(1)
    print()
    slow_print("What do you do? \nA) Stop and investigate 🔍\nB) Keep running 🏃")
    
    userChoice = input("").lower()
    while userChoice not in ['a', 'b']:
        slow_print("Bruh! really?? you paying attention?")
        userChoice = input("Press A or B to select the options!! ").lower()
    
    return userChoice


def investigate_bushes():
    """Player investigates bushes - random outcome, returns True if got key"""
    os.system('clear')
    print()
    slow_print("You slowly approach the bushes... ")
    time.sleep(1)
    slow_print("Your heart pounds in your chest... 💓")
    time.sleep(1)
    slow_print("You reach out your hand...")
    time.sleep(1.5)
    print()
    slow_print("RUSTLE! RUSTLE! 🍃🍃")
    time.sleep(1.5)
    wait_for_player()
    
    # 2 scenarios randomly
    bushOutcome = random.choice(["lucky", "unlucky"])
    
    if bushOutcome == "lucky":
        dog_encounter()
        return True  # got the key
    else:
        bear_encounter()
        return False  # no key


def dog_encounter():
    """Lucky outcome - find dog with key"""
    os.system('clear')
    slow_print("! ! ! !")
    time.sleep(1)
    print()
    # ASCII art dog
    print("""
    
          / \\__
         (    @\\___
         /         O
        /   (_____/
       /_____/   U
    
    """)
    time.sleep(1)
    slow_print("WOOF! WOOF! 🐕")
    time.sleep(0.8)
    slow_print("It's a cute FLUFF ball! 🥰")
    time.sleep(0.8)
    slow_print("The dog charges at you with pure love! 💕")
    time.sleep(1)
    slow_print("*LICK* *LICK* *LICK* 👅")
    time.sleep(1)
    print()
    slow_print("While petting the good boy, you notice something shiny...")
    time.sleep(1)
    slow_print("His collar holds a MYSTERIOUS KEY! 🔑✨")
    time.sleep(1)
    slow_print("You take the key and put it in your pocket.")
    time.sleep(1)
    slow_print("While taking big breathes, you realise you feel thirsty!\nTake 2 sips to calm your nerves! 🍺🍺")
    time.sleep(1.5)
    print()
    wait_for_player()


def bear_encounter():
    """Unlucky outcome - bear attack"""
    os.system('clear')
    slow_print("! ! ! !")
    time.sleep(1)
    print()
    # ASCII art bear
    print("""
    
            ʕ •ᴥ•ʔ
          
          //|    |\\ 
            |    |
          //      \\
    
    """)
    time.sleep(0.5)
    slow_print("GRRROOOWWWLLL!!! 🐻")
    time.sleep(0.8)
    slow_print("A MASSIVE WILD BEAR jumps out! 😱")
    time.sleep(1)
    slow_print("Its eyes glow in the moonlight... 👀")
    time.sleep(1)
    print()
    slow_print("The bear LUNGES at you! 💥")
    time.sleep(1)
    slow_print("You DUCK just in time! 🤸")
    time.sleep(1)
    slow_print("Your legs find super-human speed! 🏃💨💨💨")
    time.sleep(1)
    slow_print("You crash through bushes and branches! 🌿💥🌿")
    time.sleep(1)
    wait_for_player()
    
    os.system('clear')
    print()
    slow_print("You escaped... but BARELY! 😰")
    time.sleep(1)
    slow_print("That was TOO close! Take 2 sips to calm your nerves! 🍺🍺")
    time.sleep(2)
    print()
    wait_for_player()


def find_cabin():
    """Player keeps running and finds cabin, returns True if got map"""
    os.system('clear')
    print()
    slow_print("Nah... probably just the wind. 🌬️")
    time.sleep(1)
    slow_print("You keep running... 🏃💨")
    time.sleep(1)
    print()
    
    # Show running animation
    for i in range(10, 0, -1):
        os.system('clear')
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        print()
        print(" " * i + "🏃💨")
        print()
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        time.sleep(0.35)
    
    os.system('clear')
    print()
    slow_print("The forest path opens up ahead... 🌳")
    time.sleep(1)
    slow_print("You see an OLD ABANDONED CABIN in the distance! 🏚️")
    time.sleep(1.5)
    print()
    
    # ASCII cabin
    print("""
    
        🌙
          ___________
         /          /|
        /          / |
       /__________/  |
       |  __  __  |  |
       | |  ||  | | /
       |_|__||__|_|/
    
    """)
    time.sleep(1.5)
    
    slow_print("The windows are dark... 🕯️")
    time.sleep(1)
    slow_print("But you notice a FAINT GLOW inside... ✨")
    time.sleep(1)
    print()

    
    # Cabin choice - returns True if got map
    cabin_choice = get_cabin_choice()
    
    if cabin_choice == 'a':
        return enter_cabin()
    else:
        peek_window()
        return False  # didn't get map from peeking


def get_cabin_choice():
    """Get player choice for cabin - returns 'a' or 'b'"""
    slow_print("Do you...")
    print()
    slow_print("A) Enter the cabin 🚪")
    slow_print("B) Circle around to peek through the window 👀")
    print()
    
    cabinChoice = input("Choose A or B: ").lower()
    
    while cabinChoice not in ['a', 'b']:
        slow_print("Focus! A or B! 🥴")
        cabinChoice = input("Choose A or B: ").lower()
    
    return cabinChoice


def enter_cabin():
    """Player enters cabin - random outcome, returns True if got map"""
    os.system('clear')
    print()
    slow_print("You push the creaky door open... CREEEAAK 🚪")
    time.sleep(1.5)
    slow_print("Inside, you find...")
    time.sleep(2)
    
    # Random outcome
    cabinOutcome = random.choice(["treasure", "trap"])
    
    if cabinOutcome == "treasure":
        find_treasure_map()
        return True  # got the map
    else:
        bat_attack()
        return False  # no map


def find_treasure_map():
    """Lucky cabin outcome - treasure map"""
    print()
    slow_print("A TREASURE MAP on the table! 🗺️✨")
    time.sleep(1)
    slow_print("X marks the spot... and it's CLOSE! 📍")
    time.sleep(1)
    slow_print("This could lead to RICHES! 💰💎👑")
    time.sleep(1)
    slow_print("You grab the map and fold it into your pocket.")
    time.sleep(1)
    print()
    slow_print("You're SO excited you need to celebrate!")
    slow_print("Take 1 sip of victory! 🍺")
    wait_for_player() 
    print()


def bat_attack():
    """Unlucky cabin outcome - bats"""
    print()
    slow_print("DOZENS OF BATS! 🦇🦇🦇")
    time.sleep(1)
    slow_print("They swarm around you! 😱")
    time.sleep(1)
    slow_print("You flail wildly and stumble backwards! 💫")
    time.sleep(1)
    slow_print("You crash through the door and fall on your butt! 💥")
    time.sleep(1)
    print()
    slow_print("Ow... that hurt your pride AND your body! 😣")
    slow_print("Take 3 sips for that disaster! 🍺🍺🍺")
    wait_for_player() 
    print()


def peek_window():
    """Player peeks through window - old man encounter"""
    os.system('clear')
    print()
    slow_print("You sneak around the cabin quietly... 🤫")
    time.sleep(1)
    slow_print("You peer through the dusty window... 👁️")
    time.sleep(1.5)
    print()
    slow_print("Inside you see...")
    time.sleep(2)
    slow_print("AN OLD MAN counting gold coins! 👴💰")
    time.sleep(1)
    slow_print("He looks friendly... or does he? 🤔")
    time.sleep(1)
    print()
    slow_print("Suddenly, he looks UP and makes EYE CONTACT with you! 😳")
    time.sleep(1.5)
    slow_print("He waves you inside... 👋")
    time.sleep(1)
    print()
    slow_print("This could be good... or a TRAP! 🎭")
    slow_print("But you're curious! Take 1 sip for bravery! 🍺")
    wait_for_player()  
    print()


def final_treasure_hunt(has_key, has_map):
    """Final scene - treasure hunt ending based on items collected"""
    os.system('clear')
    print()
    slow_print("You continue deeper into the forest...")
    time.sleep(1)
    slow_print("The path winds through ancient trees 🌲")
    time.sleep(1)
    
    # running animation toward treasure
    for i in range(8, 0, -1):
        os.system('clear')
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        print()
        print(" " * i + "🏃💨")
        print()
        print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
        time.sleep(0.3)
    
    os.system('clear')
    print()
    slow_print("You arrive at a clearing... 🌟")
    time.sleep(1)
    
    # treasure chest appears
    print()
    print("""
    
        _______________
       /  ___________  \\
      /  /           \  \\
     |  | 🔒        |  |
     |  |___________|  |
     \_________________/
    
    """)
    time.sleep(1.5)
    
    slow_print("A MYSTERIOUS TREASURE CHEST! 💎")
    time.sleep(1)
    print()
    
    # different endings based on items
    if has_key and has_map:
        # best ending - both items
        perfect_ending()
    elif has_key or has_map:
        # partial ending - one item
        partial_ending(has_key)
    else:
        # bad ending - no items
        bad_ending()


def perfect_ending():
    """Best ending - player has both key and map"""
    slow_print("You pull out the KEY from your pocket! 🔑")
    time.sleep(1)
    slow_print("AND the MAP that led you here! 🗺️")
    time.sleep(1)
    print()
    slow_print("You insert the key... *CLICK* ✨")
    time.sleep(1.5)
    slow_print("The chest opens with a GOLDEN GLOW! 💫")
    time.sleep(1.5)
    
    os.system('clear')
    print()
    print("""
    
        ✨💎💰👑💎✨
        💰  YOU  💰
        💎 FOUND 💎
        👑  THE  👑
        💰TREASURE💰
        ✨💎💰👑💎✨
    
    """)
    time.sleep(2)
    
    slow_print("GOLD! JEWELS! ANCIENT ARTIFACTS! 💰💎👑")
    time.sleep(1)
    slow_print("You're RICH beyond your wildest dreams! 🤑")
    time.sleep(1)
    print()
    slow_print("This calls for a CELEBRATION! 🎉")
    slow_print("Finish your drink! 🍺🍻")
    wait_for_player()
    
    show_victory_screen()


def partial_ending(has_key):
    """Partial ending - player has one item"""
    if has_key:
        slow_print("You have the KEY! 🔑")
        time.sleep(1)
        slow_print("But... you're not sure if this chest is THE treasure...")
        time.sleep(1)
    else:
        slow_print("You have the MAP that led you here! 🗺️")
        time.sleep(1)
        slow_print("But... the chest is LOCKED! 🔒")
        time.sleep(1)
    
    print()
    slow_print("You try to open it anyway...")
    time.sleep(1.5)
    
    # random outcome for partial ending
    outcome = random.choice(["success", "fail"])
    
    if outcome == "success":
        os.system('clear')
        print()
        slow_print("*CRACK* The lock breaks! 💥")
        time.sleep(1)
        slow_print("Inside you find... SOME treasure! 💰")
        time.sleep(1)
        slow_print("Not the FULL treasure, but still pretty good! 💎")
        time.sleep(1)
        print()
        slow_print("You're moderately rich! Take 2 celebratory sips! 🍺🍺")
        wait_for_player()
        show_victory_screen()
    else:
        slow_print("The chest won't budge... 😤")
        time.sleep(1)
        slow_print("You needed BOTH the key AND the map!")
        time.sleep(1)
        print()
        slow_print("Well... at least you tried! 🤷")
        slow_print("Take 2 consolation sips! 🍺🍺")
        wait_for_player()
        show_game_over()


def bad_ending():
    """Bad ending - player has no items"""
    slow_print("The chest is LOCKED! 🔒")
    time.sleep(1)
    slow_print("And you have no way to open it... 😔")
    time.sleep(1)
    print()
    slow_print("You try to force it open...")
    time.sleep(1)
    slow_print("*GRUNT* *PUSH* 💪")
    time.sleep(1)
    slow_print("Nothing... 😩")
    time.sleep(1.5)
    
    print()
    slow_print("You walk away empty-handed...")
    time.sleep(1)
    slow_print("Better luck next time! 🍀")
    time.sleep(1)
    print()
    slow_print("That sucks! Take 3 pity sips! 🍺🍺🍺")
    wait_for_player()
    show_game_over()


def show_victory_screen():
    """Display victory screen"""
    os.system('clear')
    print()
    print("""
    
    ╔═══════════════════════════════════╗
    ║                                   ║
    ║         🏆 VICTORY! 🏆            ║
    ║                                   ║
    ║     You completed the quest!      ║
    ║                                   ║
    ║         Stay Litty! 🍻            ║
    ║                                   ║
    ╚═══════════════════════════════════╝
    
    """)
    time.sleep(2)
    ask_play_again()


def show_game_over():
    """Display game over screen"""
    os.system('clear')
    print()
    print("""
    
    ╔═══════════════════════════════════╗
    ║                                   ║
    ║         GAME OVER 💀              ║
    ║                                   ║
    ║     Better luck next time!        ║
    ║                                   ║
    ║         Stay Litty! 🍻            ║
    ║                                   ║
    ╚═══════════════════════════════════╝
    
    """)
    time.sleep(2)
    ask_play_again()


def ask_play_again():
    """Ask if player wants to play again"""
    print()
    slow_print("Wanna go again? 🎮")
    choice = input("(Y/N): ").lower()
    
    if choice in ['y', 'yes']:
        soloMode()  # restart game
    else:
        os.system('clear')
        print()
        slow_print("Thanks for playing LITTY ADVENTURE! 🍻")
        slow_print("Stay litty out there! ✌️🔥")
        print()
        time.sleep(2)
        quit()