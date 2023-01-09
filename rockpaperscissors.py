import random

paper = "paper"
rock = "rock"
scissors = "scissors"

winning_combinations = {rock: scissors, paper: rock, scissors: paper}


def score(player, computer):
    if player == computer:
        return "Draw"
    if winning_combinations[player] == computer:
        return "Player wins"
    else:
        return "Computer wins"


def play():
    choices = [rock, paper, scissors]
    guess = raw_input("Rock, paper or scissors?")
    if guess not in choices:
        print "You can't use that, try again."
        return play()
    computer_guess = random.choice(choices)
    print "Computer has chosen " + computer_guess
    print score(guess, computer_guess)


play()
