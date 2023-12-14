from .card import Card

class Base(Card):

    def __init__(self, name, faction, unique, hp,
        ability=None, description=None):
        super().__init__(name, description)
        self.faction = faction
        self.unique = unqiue
        self.card_type = 'base'
        self.hp = hp
        self.ability = ability # same as unit abilities