"""
main.py
Twilight Struggle card tracker

Idea: offload the task of counting cards.

Functional organization: 

App maintains a list of cards that are still in the pack / opponent's hand. 

User inputs each card as it is played, and app removes it from the list. (Auto-completing card name would be nice.)

App models deck management rules from the game -- reshuffles, adding Mid- and Late-war cards, etc.(?). 
"""

import readline
import itertools

def getCards(filename):
    
    # Read early war cards from file into list, stripping newlines
    with open(filename,'r') as f: 
        cards = [l.replace("\n","") for l in f.readlines()]
    
    return cards
    

class DeckHandler(object):
    
    def __init__(self,cards): 
        self.cards = sorted(cards)
        self.discard = []
        self.removed = []
    
    def complete(self,text,state):
        response = None
        
        if state == 0:
            if text:
                self.matches = [s for s in self.cards if s and s.startswith(text)]
            else: 
                self.matches = self.cards
        
        try: 
            response = self.matches[state]
        except IndexError: 
            response = None
        
        return response

    def doInput(self, input): 
        pass

    def discardCard(self, card):

        self.cards.remove(card)

        self.discard.append(card)
        self.discard.sort()

    def removeCard(self,card):
        self.cards.remove(card)
        self.removed.append(card)
        self.removed.sort()
        


    def listCards(self):

        return ['In deck\n'] + self.cards

    def listDiscards(self):

        return ['In discard\n'] + self.discard

    def listRemoved(self):

        return ['Removed from game\n'] + self.removed

    def reshuffle(self):

        self.cards = sorted(self.cards + self.discard)
        self.discard = []

    def addMidWar(self):

        with open("mid-war.txt",'r') as f: 
            midwar = [l.replace("\n","") for l in f.readlines()]
            self.cards = sorted(self.cards + midwar)

    def addLateWar(self):

        with open("late-war.txt",'r') as f: 
            midwar = [l.replace("\n","") for l in f.readlines()]
            self.cards = sorted(self.cards + midwar)
        

def input_loop(dh):
    line = ''
    while True: 
        print "\n\n\n"
        for (a,b,c) in itertools.izip_longest(dh.listCards(),dh.listDiscards(),dh.listRemoved(),fillvalue=" "): 
            # print '{0}\t\t\t\t{1}\t\t\t\t{2}'.format(a,b,c)
            print '%-40s %-40s %s' % (a, b, c)
        line = raw_input('>') 
        if line.startswith("discard"):
            pre, card = line.split(" ",1)
            dh.discardCard(card)
        if line.startswith("remove"):
            pre, card = line.split(" ",1)
            dh.removeCard(card)
        if line.startswith("reshuffle"):
            dh.reshuffle()
        if line.startswith("midwar"):
            dh.addMidWar()
        if line.startswith("latewar"):
            dh.addLateWar()



cards = getCards("early-war.txt")
dh=DeckHandler(cards)

readline.set_completer(dh.complete)

readline.parse_and_bind('tab: complete') 

input_loop(dh)
        
        
    
    