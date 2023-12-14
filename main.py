from cards.unit import Unit
from cards.base import Base
from cards.capital_ship import Capital_Ship
from cards.cards import Cards

def main():
    print("SW-DBG")
    cards = Cards()
    deck = []
    deck = deck + cards.create_cards('/home/bhsb/Documents/SW-DBG/cards/units')

    print(deck)
    for card in deck:
        print(card.name, card.cost)



if __name__ == '__main__':
    main()