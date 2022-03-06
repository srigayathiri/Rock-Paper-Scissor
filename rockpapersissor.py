# program to play a game Rock-Paper-Scissor

import random
import logic

sym_list = [
    """
          * * * * * *
        *             *
       *    R O C K    *
        *             *
          * * * * * *
    """,
    """
        * * * * * * * *
        *             *
        *  P A P E R  *
        *             *
        * * * * * * * *
    """,
    """
         * S C I S S O R *
          *            *
            *       *
              *   *
              * * *
           *        *
         *   *    *   *
           *        *
              
     """]


def rps_instruction():
    print("."*42)
    print("Instructions for Rock-Paper-Scissor game")
    print("."*42)
    print("Rock crushes Scissor")
    print("Scissor cuts paper")
    print("Paper covers rock")
    print("."*42)


your_score = 0
opponent_score = 0

ask = input("Do you wanna play the game ?\nYes/No : ").upper()
if ask == "YES":
    print("Lets play the game...!")
    rps_instruction()

    while True:
        def input_choice():
            opponent_choice = random.choice(sym_list)
            player_choice = input("Enter rock, paper or scissor : ").lower()
            print("Your\'s choice is :")
            if player_choice == "rock":
                print(sym_list[0])
            elif player_choice == "paper":
                print(sym_list[1])
            elif player_choice == "scissor":
                print(sym_list[2])
            else:
                quit()
            print("Opponent\'s choice is :\n", opponent_choice)

            if player_choice == "rock":
                logic.rock_logic(player_choice, opponent_choice, your_score, opponent_score, sym_list)
            elif player_choice == "paper":
                logic.paper_logic(player_choice, opponent_choice, your_score, opponent_score, sym_list)
            else:
                logic.scissor_logic(player_choice, opponent_choice, your_score, opponent_score, sym_list)

            ask1 = input("Do you wanna play again...? Yes/No : ").lower()
            if ask1 != "yes":
                print("Thanks for playing")
                quit()
        input_choice()
else:
    print("Give a try...")
