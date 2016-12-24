# two-players Rock-Paper-Scissors game
# -*- coding: utf-8 -*-
import time

print "This is a Rock-Paper-Scissors game"
print "  "

joueur1 = raw_input("Player1 please enter your name: ")
joueur2 = raw_input("Player2 please enter your name: ")

print "  "
print "Choose one of those options : Rock / Paper / Scissors "
print "  "

player1wins = " Congratulations "+joueur1+", you win !"
player2wins = " Congratulations "+joueur2+", you win !"
egalite = " It's a tie !"
waitforit = "Wait For It..."

while True:
    player1 = raw_input(" "+joueur1+" your turn: ")
    player2 = raw_input(" "+joueur2+" your turn: ")

    if player1 == "Rock":
        if player2 == "Rock":
            print waitforit
            time.sleep(1)
            print egalite
        elif player2 == "Paper":
            print waitforit
            time.sleep(1)
            print player1wins
        elif player2 == "Scissors":
            print waitforit
            time.sleep(1)
            print player1wins
    elif player2 == "Rock":
        if player1 == "Rock":
            print waitforit
            time.sleep(1)
            print egalite
        elif player1 == "Paper":
            print waitforit
            time.sleep(1)
            print player2wins
        elif player1 == "Scissors":
            print waitforit
            time.sleep(1)
            print player2wins
    elif player1 == "Paper":
        if player2 == "Paper":
            print waitforit
            time.sleep(1)
            print egalite
        elif player2 == "Scissors":
            print waitforit
            time.sleep(1)
            print player2wins
    elif player2 == "Paper":
        if player1 == "Scissors":
            print waitforit
            time.sleep(1)
            print player1wins
    elif player1 == "Scissors":
        if player2 == "Scissors":
            print waitforit
            time.sleep(1)
            print egalite
    else :
        print " Invalid input! You have not entered Rock, Paper or Scissors, try again."
