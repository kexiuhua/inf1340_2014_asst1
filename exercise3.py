#!/usr/bin/env python3

def decide_rps(player1, player2):
    #write something here
    #abc123
    scores = {("Rock", "Rock"): 0,
              ("Rock", "Paper"): 2,
              ("Rock", "Scissors"): 1,
              ("Paper", "Rock"): 1,
              ("Paper", "Paper"): 0,
              ("Paper", "Scissors"): 2,
              ("Scissors", "Rock"): 2,
              ("Scissors", "Paper"): 1,
              ("Scissors", "Scissors"): 0}

    index = (player1, player2)

    return scores[index]

print(decide_rps("Scissors", "Rock"))
print(decide_rps("Scissors", "asdf"))