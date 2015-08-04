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

    def removeCard(self, card):

        self.cards.remove(card)
        self.discard.append(card)
        self.discard.sort()

    def listCards(self):

        return self.cards

def input_loop(dh):
    line = ''
    while True: 
        print dh.listCards()
        line = raw_input('Prompt') 
        dh.removeCard(line)



cards = getCards("early-war.txt")
dh=DeckHandler(cards)

readline.set_completer(dh.complete)

readline.parse_and_bind('tab: complete') 

input_loop(dh)
        
        
    
    