
import time, os

rows = int(input("How many rows you want?"))
os.system('clear')

print("T"*rows) # to have trees on top at first

for i in range(0,rows):

    if i > 3:
        print("\n"+" "*i + "*")  # will go from 2nd line after i bigger than 3
    
    else:
        print(" "*i + "*")  # with loop i value it will print space and star
    time.sleep(1)   # pause the time ofr 1 sec so it doesnt print everything at once
    os.system('clear')  # clear terminal so slow motion affects
    print("T"*rows) # prints trees which will show on top again because screen will clear out in last line

os.system("clear")

# trying to use slow text concept
congrats = "Yeaaaaaaay"
for each in congrats:
    print(each, end="", flush=True)
    time.sleep(1.5)

# lol didnt work slow text. nothing apears may be looping in background. is it because we cant loop through a string ?