# # R-P-S GAME V-1

# import random
# import time

# options = ("rock", "paper", "sissors")

# # presentation
# ## first group words
# for word in ["welcome", "to", "-ROCK-", "-PAPER-", "-SISSORS-", "**GAME**"][0:2]:
#     print(word)
#     time.sleep(1)
# ## second group words
# for word in ["welcome", "to", "-ROCK-", "-PAPER-", "-SISSORS-", "**GAME**"][2:]:
#     print(word)
#     time.sleep(0.5)
# time.sleep(1)


# # mechanics
# def round():
#     is_running = True
#     computer_score = 0
#     player_score = 0
#     while is_running:
#         computer = random.choice(options)
#         for choice in ["ROCK.", "PAPER..", "SISSORS..."]:
#             print(choice)
#             time.sleep(0.3)

#         player = input("*> ")
#         if player in options:
#             if player == computer:
#                 print("TIE!!")
#             elif player == "rock" and computer == "paper":
#                 print("1 to computer")
#                 computer_score += 1
#             elif player == "paper" and computer == "sissors":
#                 print("1 to computer")
#                 computer_score += 1
#             elif player == "sissors" and computer == "paper":
#                 print("1 to computer")
#                 computer_score += 1
#             else:
#                 print("1 to player")
#                 player_score += 1
#         else:
#             print("this option is invalid")
        
#         time.sleep(0.5)
#         print()

#         if player_score == 3 and computer_score < 3:
#             is_running = False
#             print(f"**********\n***PLAYER WIN***\nwith {player_score} to {computer_score}")
#         elif computer_score == 3 and player_score < 3:
#             is_running = False
#             print(f"**********\n***COMPUTER WIN***\nwith {computer_score} to {player_score}")
        

# # press to start
# press_button = input("-PRESS TO START-")
# if press_button == str(press_button):
#     time.sleep(1)
#     print()
#     round()


# R-P-S GAME V-2

# **********
# add matchs, show computer choice, do some graphics improvements
# **********

import random
import time

options = ("rock", "paper", "scissors")

# presentation
## first group words
for word in ["welcome", "to", "-ROCK-", "-PAPER-", "-SCISSORS-", "**GAME**"][0:2]:
    print(word)
    time.sleep(1)
## second group words
for word in ["welcome", "to", "-ROCK-", "-PAPER-", "-SCISSORS-", "**GAME**"][2:]:
    print(word)
    time.sleep(0.5)
time.sleep(1)


# mechanics
def round():
    is_running = True
    computer_score = 0
    player_score = 0
    while is_running:
        computer = random.choice(options)
        for choice in ["ROCK.", "PAPER..", "SCISSORS..."]:
            print(choice)
            time.sleep(0.3)

        player = input("--> ")
        if player in options:
            if player == computer:
                print("TIE!!")
                time.sleep(.5)
            elif player == "rock" and computer == "paper":
                computer_score += 1
                print(f"* {computer_score} to computer *")
                print(f"computer choice: {computer}")
                
                time.sleep(.5)
                
            elif player == "paper" and computer == "scissors":
                computer_score += 1
                print(f"* {computer_score} to computer *")
                print(f"computer choice: {computer}")
                
                time.sleep(.5)
                
            elif player == "scissors" and computer == "paper":
                computer_score += 1
                print(f"* {computer_score} to computer *")
                print(f"computer choice: {computer}")
                
                time.sleep(.5)
            else:
                player_score += 1
                print(f"* {player_score} to player *")
                print(f"computer choice: {computer}")
                
                time.sleep(.5)
        else:
            print("this option is invalid")
        
        time.sleep(0.5)
        print()

        if player_score == 3 and computer_score < 3:
            is_running = False
            print(f"""****************\n***PLAYER WIN***\n***** {player_score}:{computer_score} ******""")
            
        elif computer_score == 3 and player_score < 3:
            is_running = False
            print(f"""******************\n***COMPUTER WIN***\n****** {computer_score}:{player_score} ******""")
        

# press to start
press_button = input("-PRESS TO START-")
if press_button == str(press_button):
    time.sleep(1)
    print()
    round()
