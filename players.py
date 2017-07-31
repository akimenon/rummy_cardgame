from collections import defaultdict


def sequencecheck(cardtype,card,step,profile):

    #conver list to int list
    l =list(map(int,cardtype[card[-1]]))
    c =int(card[:-1])
    matchcard =[]
    #sort it for sequencing
    l.append(c)
    l.sort()

    seqcheck=0

    #check range from 1st element to step size

    for k in range(l[0],l[0]+step):
        if (l.count(k)):
            seqcheck+=1
            matchcard.append(k)


    if (seqcheck>=step):
        profile.currentmatchdecks={card[-1]:matchcard}

    return (seqcheck>=step)


class players(object):

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def openingHandDeck (self,openingHandDeck):
        self.openingHandDeck=openingHandDeck

        print ('opendeck:%s' %(self.openingHandDeck))


    def handchecker(self,card):

        #remove any matcheddeck so that it doenst duplicate
        self
        #conver my hand to type dict
        cardtype=cardtypedic(self.openingHandDeck)

        #check sequence card exists
        if(sequencecheck(cardtype,card,4,self)):
            print ('##Got a sequence#cardType: %s : card : %s :' %(cardtype,card))
            self.openingHandDeck.append(card)
            print('##new opening hand: %s' % (self.openingHandDeck))
            print ('match deck: %s' %(self.currentmatchdecks))


    def trashcard(self):
        pass

def cardtypedic(cards):

    cardtypdic=defaultdict(list)
    for i in cards:
        cardtypdic[i[-1]].append(i[:-1])

    return cardtypdic

def cardnodic(cards):
    cardnodic = defaultdict(list)
    for i in cards:
        cardnodic[i[-1]].append(i[:-1])

    return cardnodic

def incrementer(lnum,step):


    return str(int(lnum[:-1])+step)


def decrementer(lnum, step):

    return str(int(lnum[:-1])-step)


