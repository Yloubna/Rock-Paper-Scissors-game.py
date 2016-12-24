# one player Rock-Paper-Scissors game
# -*- coding: utf-8 -*-
import time
import random

print "This is a Rock-Paper-Scissors game"
print "  "

joueur1 = raw_input("Hello ! Please enter your name: ")
joueur2 = "The computer"

print "  "
print "Choose one of those options : Rock / Paper / Scissors "
print "  "

player1wins = " Congratulations "+joueur1+", you win !"
player2wins = " "+joueur2+" wins !"
egalite = " It's a tie !"
waitforit = "Wait For It..."

while True:

    player2 = random.randrange(1,4)
    if player2 == 1 :
        print " The computer plays : Rock"
    elif player2 == 2 :
        print " The computer plays : Paper"
    else :
        print " The computer plays : Scissors"

    player1 = raw_input(" "+joueur1+" your turn: ")

    if player1 == "Rock":
        if player2 == 1:
            print waitforit
            time.sleep(2)
            print egalite
        elif player2 == 2:
            print waitforit
            time.sleep(2)
            print player1wins
        elif player2 == 3:
            print waitforit
            time.sleep(2)
            print player1wins
    elif player2 == 1:
        if player1 == "Rock":
            print waitforit
            time.sleep(2)
            print egalite
        elif player1 == "Paper":
            print waitforit
            time.sleep(2)
            print player2wins
        elif player1 == "Scissors":
            print waitforit
            time.sleep(2)
            print player2wins
    elif player1 == "Paper":
        if player2 == 2:
            print waitforit
            time.sleep(2)
            print egalite
        elif player2 == 3:
            print waitforit
            time.sleep(2)
            print player2wins
    elif player2 == 2:
        if player1 == "Scissors":
            print waitforit
            time.sleep(2)
            print player1wins
    elif player1 == "Scissors":
        if player2 == 3:
            print waitforit
            time.sleep(2)
            print egalite
    else :
         print "Invalid Input. Please try again"
