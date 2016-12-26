# one player Rock-Paper-Scissors game
# -*- coding: utf-8 -*-
import time
import random

print "This is a Rock-Paper-Scissors game"
print "  "

joueur1 = raw_input("Hello ! Please enter your name: ")
joueur2 = "The computer"

print "  "
print "Choose one of those options :"
print " 1 for Rock"
print " 2 for Paper"
print " 3 for Scissors"
print "  "

player1wins = " Congratulations "+joueur1+", you win !"
player2wins = " "+joueur2+" wins !"
egalite = " It's a tie !"
waitforit = "Wait For It..."
partie = 0
score1 = 0
score2 = 0

while partie < 6 :
    player1 = int(raw_input(" "+joueur1+" your turn: "))
    player2 = random.randrange(1,4)
    partie += 1

    if player2 == 1 :
        print " The computer plays : Rock"
    elif player2 == 2 :
        print " The computer plays : Paper"
    else :
        print " The computer plays : Scissors"

    if player1 == 1 :
        if player2 == 1:
            print waitforit
            time.sleep(0.5)
            print egalite
        elif player2 == 2:
            print waitforit
            time.sleep(0.5)
            print player2wins
            score2 += 1
        elif player2 == 3:
            print waitforit
            time.sleep(0.5)
            print player1wins
            score1 += 1
    elif player2 == 1:
        if player1 == 2 :
            print waitforit
            time.sleep(0.5)
            print player1wins
            score1 += 1
        elif player1 == 3 :
            print waitforit
            time.sleep(0.5)
            print player2wins
            score2 += 1
    elif player1 == 2 :
        if player2 == 2:
            print waitforit
            time.sleep(0.5)
            print egalite
        elif player2 == 3:
            print waitforit
            time.sleep(0.5)
            print player2wins
            score2 += 1
    elif player2 == 2:
        if player1 == 3 :
            print waitforit
            time.sleep(0.5)
            print player1wins
            score1 += 1
    elif player1 == 3 :
        if player2 == 3:
            print waitforit
            time.sleep(0.5)
            print egalite
    else :
         print "Invalid Input. Please try again"
print " "
print " Game Over !"
print " "
if score1 > score2 :
    print " "+joueur1+" you win this round with "+str(score1)+" points"
elif score1 < score2 :
    print " The computer wins this round with "+str(score2)+" points"
else :
    print " it's a tie ! "
