# logic for Rock-Paper-Scissor game

def rock_logic(player_choice, opponent_choice, your_score, opponent_score, sym_list):
    if player_choice == "rock" and opponent_choice == sym_list[0]:
        print(f"Your score : {your_score} \t\t Opponent\'s score : {opponent_score}")
        print("\t\t\tIt\'s a tie")
    elif player_choice == "rock" and opponent_choice == sym_list[1]:
        opponent_score += 1
        print(f"Your score : {your_score} \t\t Opponent\'s score : {opponent_score}")
        print("\t\t\tSorry, You lose!")
    else:
        your_score += 1
        print(f"Your score : {your_score} \t\t Opponent\'s score : {opponent_score}")
        print("\t\t\tCongrats, You win!")


def paper_logic(player_choice, opponent_choice, your_score, opponent_score, sym_list):
    if player_choice == "paper" and opponent_choice == sym_list[1]:
        print(f"Your score : {your_score} \t\t Opponent\'s score : {opponent_score}")
        print("\t\t\tIt\'s a tie")
    elif player_choice == "paper" and opponent_choice == sym_list[2]:
        opponent_score += 1
        print(f"Your score : {your_score} \t\t Opponent\'s score : {opponent_score}")
        print("\t\t\tSorry, You lose!")
    else:
        your_score += 1
        print(f"Your score : {your_score} \t\t Opponent\'s score : {opponent_score}")
        print("\t\t\tCongrats, You win!")


def scissor_logic(player_choice, opponent_choice, your_score, opponent_score, sym_list):
    if player_choice == "scissor" and opponent_choice == sym_list[2]:
        print(f"Your score : {your_score} \t\t Opponent\'s score : {opponent_score}")
        print("\t\t\tIt\'s a tie")
    elif player_choice == "scissor" and opponent_choice == sym_list[0]:
        opponent_score += 1
        print(f"Your score : {your_score} \t\t Opponent\'s score : {opponent_score}")
        print("\t\t\tSorry, You lose!")
    else:
        your_score += 1
        print(f"Your score : {your_score} \t\t Opponent\'s score : {opponent_score}")
        print("\t\t\tCongrats, You win!")
