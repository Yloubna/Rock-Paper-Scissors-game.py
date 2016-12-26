# two-players Rock-Paper-Scissors game
# -*- coding: utf-8 -*-
import time

print "This is a Rock-Paper-Scissors game"
print "  "

joueur1 = raw_input("Player1 please enter your name: ")
joueur2 = raw_input("Player2 please enter your name: ")

print "  "
print "Choose one of those options :"
print " 1 for Rock"
print " 2 for Paper"
print " 3 for Scissors"
print "  "

player1wins = " Congratulations "+joueur1+", you win !"
player2wins = " Congratulations "+joueur2+", you win !"
egalite = " It's a tie !"
waitforit = "Wait For It..."
partie = 0
score1 = 0
score2 = 0

while partie < 6 :
    player1 = int(raw_input(" "+joueur1+" your turn: "))
    player2 = int(raw_input(" "+joueur2+" your turn: "))
    partie += 1
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
    print " "+joueur1+", you win this round with "+str(score1)+" points. Congrats !"
elif score1 < score2 :
    print " "+joueur2+", you win this round with "+str(score2)+" points. Congrats !"
else :
    print " it's a tie ! "
