#Kollin Schalhamer
#CIS- 125
# Week 11 Assignment
#11-24-15

#Import info from BowlingGame.py 

from BowlingGame import Game


#Read File
newFile=open("testscores.txt", "r")
scoreList = []

#Analyze the file

for line in newFile:

    #Strip all lines and split numbers with comma
    line=line.strip()
    scoresList=line.split(",")
    scoresList=[int(e) for e in scoreList]
    totalScore=scoresList.pop()
    
    #Number of Pins
    #g is from BowlingGameTest.py
    g=Game()
    
    for pins in scoresList:
        g.roll(pins)
    score=g.score()
    
    #Give player scores
    print ("The score you recieved is {}, and the original is{}" .format(score, totalScore))
    
    if score == totalScore:
        print("YES! The scores match!")
    else:
        print("WRONG! The score should be", score)
        
    newFile.close()