""" Rock Paper Scissors
----------------------------------------
"""
import random


# Show status at the end of the game 
def status(st):
    if st == "win":
        return print("\n [😎 WIN  ]\n----------------------------------------")
    elif st == "lose":
        return print("\n [😳 LOSE ]\n----------------------------------------")
    else:
        return print("\n [😐 DRAW ]\n----------------------------------------")

# Show score at the end of the game  
def show_score(pn, cs, ps):
    print("=========================================================================")
    print(" 🤖🔻-(ROBOT SCORE):[{}]  |  😃🔻-({} SCORE):[{}]".format(cs, pn, ps))
    if cs > ps:
        print("\n_____________ 💀 ROBOT WIN 💀 ____________")
    elif cs < ps:
        print("\n_____________ 🎉 YOU WIN 🎉 ______________")
    else:
        print("\n_____________ 👉👈 DRAW 👉👈 _____________")
    print("=========================================================================")


def start_game():
    computer_score = 0
    player_score = 0
    
    # play_by_hand = {1:"✊", 2:"🖐", 3:"✌"}
    play_by_objects = {1:"⚫", 2:"📃", 3:"✂️"}

    # get information from player
    print("=========================================================================")
    print(" 🔷  HELLO TERMINAL TRAVELER! WELCOME TO [ROCK, PAPER, SCISSORS] GAME! 🔷")
    print("=========================================================================")
    player_name = input(" ⚙️  ENTER YOUR NAME: ")
    print("----------------------------------------")
    round_num = input(" ⚙️  HOW MANY ROUND: ")
    print("----------------------------------------")   
    wanna_play = input(" ▶️  OK **{}**, READY TO PLAY? [y/n]: ".format(player_name))
    print("=========================================================================")
    if wanna_play != "y":
        print(" 👋 GOOD BYE")
        return
    # start game
    for i in range(int(round_num)):
        moves = {1:"Rock", 2:"Paper", 3:"Scissors"}

        random_number = int(random.randint(1, 3))
        computer_move = moves[random_number]
        cm_emoji = play_by_objects[random_number]
        # cm_emoji = play_by_hand[random_number]

        print(" ENTER THE NUMBER OF SELECTED MOVE: [1:⚫, 2:📃, 3:✂️  ]")
        action = 0
        while True:
            action = int(input(" ↪️  : "))
            if action in moves:
                player_move = moves[action]
                pm_emoji = play_by_objects[action]
                # pm_emoji = play_by_hand[action]
                break
            else:
                print("----------------------------------------")   
                print(" ⚠️  ^ UNVALIED INPUT! TRY AGAIN.. ^ ⚠️")
                print("----------------------------------------")   


        print(" 🤖 -(ROBOT):{}  | 😃 -({}):{}".format(cm_emoji, player_name, pm_emoji))
        if player_move == computer_move:
            status("draw")
        else:
            # Scissors:1 | Rock:3
            if (player_move == "Scissors") and (computer_move == "Rock"):
                computer_score = computer_score + 1
                status("lose")
            if (player_move == "Rock") and (computer_move == "Scissors"):
                player_score = player_score + 1
                status("win")

            # Paper:2 | Rock:3    
            if (player_move == "Rock") and (computer_move == "Paper"):
                computer_score = computer_score + 1
                status("lose")
            if (player_move == "Paper") and (computer_move == "Rock"):
                player_score = player_score + 1
                status("win")

            # Paper:2 | Scissors:3 
            if (player_move == "Paper") and (computer_move == "Scissors"):
                computer_score = computer_score + 1
                status("lose")
            if (player_move == "Scissors") and (computer_move == "Paper"):
                player_score = player_score + 1
                status("win")

    show_score(player_name, computer_score, player_score)

if __name__ == '__main__':
    start_game()
