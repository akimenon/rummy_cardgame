#import required packages
import itertools
import random
from players import players

#create the deck of cards
deck=list(itertools.product((range(1,14)),['S','H','C','D']))

# Declare list for profiles
profile = []

#enter and store player details
def enterPlayerDetails(noOfPlayer):
    global profile
    for i in range (1,noOfPlayer+1):
        #Enter name
        p=input("Enter your name player %s : " %(i))
        #Enter Age
        a = input("Enter your age player %s : " % (i))
        #Enter Sex
        s = input("Enter your sex player %s : " % (i))

        #add the players object to the list
        profile.append(players(p,a,s))


#find out no of cards per player
def noOfCardsPerPlayer(noOfPlayer):
    if noOfPlayer > 2:
        return 7
    else:
        return 10

#get the running deck
def getDeck(deck,count):
        s= (str(deck[count][0])+deck[count][1])
        deck.pop(count)
        yield s

#distribute cards for profile
def distributecards(profile,cardsperplayer,deck):

    #loop through profile and start distribution
    for y in profile:
        openinghand = []
        for y1 in range(cardsperplayer):
            openinghand.append(next(getDeck(deck,y1)))

        #fill players deck
        y.openingHandDeck(openinghand)

#Enter game here
def initgame():

 while True:
    try:
      noofplayer=int(input("Enter No of players:"))
      break
    except:
      print('Try Again!')

 cardsperplayer=noOfCardsPerPlayer(noofplayer)

 print('No of cards per player is: %s' %(cardsperplayer))
 print('**lets setup the players***')
 enterPlayerDetails(noofplayer)
 print ('****start shuffling cards !***')
 random.shuffle(deck)

 print ('**** start distributing %s per player***' %(cardsperplayer))
 distributecards(profile,cardsperplayer,deck)
 print('after: %s' % (len(deck)))



#Let the game begin
initgame()


def startgame():
    while True:
        try:
            nxtcard = next(getDeck(deck, 1))
            print("1**Card on desk**:%s" % (nxtcard))
            profile[0].handchecker(nxtcard)


        except IndexError:
            print ("**game over!**")
            break

startgame()



