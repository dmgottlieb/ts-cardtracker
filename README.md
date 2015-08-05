# ts-cardtracker

Simple command-line card tracker for Twilight Struggle. 
Invoke using:

> python main.py

You are presented with an interactive prompt showing all cards remaining in the deck (or players' hands), all cards that have been discarded, and all cards that have been removed from the game. 

To discard a card, type "discard" followed by the card name: 

> discard Defectors

You can use tab-autocomplete for card names. 

Other commands: 

* `remove [cardname]`: removes it from the game
* `midwar`: add midwar cards 
* `latewar`: add latewar cards
* `reshuffle`: add discarded cards back to the deck.
