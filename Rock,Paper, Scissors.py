import random
import time

rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}


player_score = 0
computer_score = 0  # it will help to keep the winning scores

def game():
    player = move()
    computer = random.randint(1,3)
    result(player, computer)
    return (play_again())
def move():
    while True:
        player = input("Rock=1, paper = 2, scissors = 3.MAKE A MOVE")
        player = int(player)
        try:
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("please enter 1,2 or 3")

def result(player, computer):
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("computer moved {0}".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("there's a tie")
    else:
        if rules[player] == computer:
            print("you won")
            player_score += 1
        else:
            print("the computer wins")
            computer_score += 1
def play_again():
    answer = input("want to play again yes / no")
    if answer in ('yes'):
        return answer
    else:
        print("it was nice playing with you")
        quit()
def start():
    while game():
        pass
    scores()

if __name__ == '__main__':
    start()

