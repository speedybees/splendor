#! /usr/bin/python

from enum import Enum
import random

class GemType(Enum):
    GOLD = 0
    DIAMOND = 1
    EMERALD = 2
    OPAL = 3
    RUBY = 4
    SAPPHIRE = 5

"""A place in the game cards can be.  Typically, the three decks, the purchasable rows, player tableaus, and player reserved cards
"""
class CardStorer(object):
    def __init__(self, cards=None):
        if cards == None:
            cards = set()
        self.cards = cards

    def add(self, card):
        self.cards.add(card)

    def remove(self, card):
        self.cards.remove(card)

class Card(object):
    def __init__(self, base_price, gem_value, point_value=0):
        self.base_price = base_price
        self.point_value = point_value
        self.gem_value = gem_value

    def get_point_value(self):
        return self.point_value

    def move(self, source, destination):
        source.remove(self)
        destination.add(self)

class GemValue(object):
    def __init__(self, gem_type_value_map):
        self.gem_type_value_map = gem_type_value_map

    def __getitem__(self, gem_type):
        if self.gem_type_value_map.has_key(gem_type):
            return self.gem_type_value_map[gem_type]
        else:
            return 0

    def __str__(self):
        return str(self.gem_type_value_map)

class CardRow(CardStorer):
    def __init__(self, deck, cards = None, card_count = 4):
        CardStorer.__init__(self, cards)
        self.card_count = 4
        self.deck = deck

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
        self.replenish()

    def replenish(self):
        while self.deck.has_cards() and len(self.cards) < self.card_count:
            self.deck.get_top_card().move(self.deck, self)

class Deck(CardStorer):
    def __init__(self, cards):
        CardStorer.__init__(self, cards)
        # Decks' cards are ordered
        self.cards = list(self.cards)

    def has_cards(self):
        return len(self.cards) > 0

    def get_top_card(self):
        return self.cards[0]

    def shuffle(self):
        random.shuffle(self.cards)

    @staticmethod
    def create_deck(level):
        cards = set()
        if level == 1:
            batch_type = GemType.SAPPHIRE
            for price in [
                {GemType.OPAL: 3},
                {GemType.OPAL: 2, GemType.DIAMOND: 1},
                {GemType.OPAL: 2, GemType.EMERALD: 2},
                {GemType.RUBY: 2, GemType.EMERALD: 2, GemType.DIAMOND: 1},
                {GemType.RUBY: 1, GemType.EMERALD: 3, GemType.SAPPHIRE: 1},
                {GemType.OPAL: 1, GemType.RUBY: 1, GemType.EMERALD: 1, GemType.DIAMOND: 1},
                {GemType.OPAL: 1, GemType.RUBY: 2, GemType.EMERALD: 1, GemType.DIAMOND: 1}
                ]:
                cards.add(Card(base_price=GemValue(price), gem_value=GemValue({batch_type: 1})))
            cards.add(Card(base_price=GemValue({GemType.RUBY: 4}), gem_value=GemValue({batch_type: 1}), point_value=1))


            batch_type = GemType.RUBY
            for price in [
                {GemType.DIAMOND: 3},
                {GemType.SAPPHIRE: 2, GemType.EMERALD: 1},
                {GemType.RUBY: 2, GemType.DIAMOND: 2},
                {GemType.OPAL: 2, GemType.EMERALD: 1, GemType.DIAMOND: 2},
                {GemType.OPAL: 3, GemType.RUBY: 1, GemType.DIAMOND: 1},
                {GemType.OPAL: 1, GemType.EMERALD: 1, GemType.SAPPHIRE: 1, GemType.DIAMOND: 1},
                {GemType.OPAL: 1, GemType.RUBY: 1, GemType.EMERALD: 1, GemType.DIAMOND: 2}
                ]:
                cards.add(Card(base_price=GemValue(price), gem_value=GemValue({batch_type: 1})))
            cards.add(Card(base_price=GemValue({GemType.DIAMOND: 4}), gem_value=GemValue({batch_type: 1}), point_value=1))


            batch_type = GemType.OPAL
            for price in [
                {GemType.EMERALD: 3},
                {GemType.EMERALD: 2, GemType.RUBY: 1},
                {GemType.EMERALD: 2, GemType.DIAMOND: 2},
                {GemType.RUBY: 1, GemType.SAPPHIRE: 2, GemType.DIAMOND: 2},
                {GemType.OPAL: 1, GemType.RUBY: 3, GemType.EMERALD: 1},
                {GemType.RUBY: 1, GemType.EMERALD: 1, GemType.SAPPHIRE: 1, GemType.DIAMOND: 1},
                {GemType.RUBY: 1, GemType.EMERALD: 1, GemType.SAPPHIRE: 2, GemType.DIAMOND: 1}
                ]:
                cards.add(Card(base_price=GemValue(price), gem_value=GemValue({batch_type: 1})))
            cards.add(Card(base_price=GemValue({GemType.SAPPHIRE: 4}), gem_value=GemValue({batch_type: 1}), point_value=1))


            batch_type = GemType.DIAMOND
            for price in [
                {GemType.SAPPHIRE: 3},
                {GemType.OPAL: 1, GemType.RUBY: 2},
                {GemType.OPAL: 2, GemType.SAPPHIRE: 2},
                {GemType.OPAL: 1, GemType.EMERALD: 2, GemType.SAPPHIRE: 2},
                {GemType.OPAL: 1, GemType.SAPPHIRE: 1, GemType.DIAMOND: 3},
                {GemType.OPAL: 1, GemType.RUBY: 1, GemType.EMERALD: 1, GemType.SAPPHIRE: 1},
                {GemType.OPAL: 1, GemType.RUBY: 1, GemType.EMERALD: 2, GemType.SAPPHIRE: 1}
                ]:
                cards.add(Card(base_price=GemValue(price), gem_value=GemValue({batch_type: 1})))
            cards.add(Card(base_price=GemValue({GemType.EMERALD: 4}), gem_value=GemValue({batch_type: 1}), point_value=1))


            batch_type = GemType.EMERALD
            for price in [
                {GemType.RUBY: 3},
                {GemType.SAPPHIRE: 1, GemType.DIAMOND: 2},
                {GemType.RUBY: 2, GemType.SAPPHIRE: 2},
                {GemType.OPAL: 2, GemType.RUBY: 2, GemType.SAPPHIRE: 1},
                {GemType.EMERALD: 1, GemType.SAPPHIRE: 3, GemType.DIAMOND: 1},
                {GemType.OPAL: 1, GemType.RUBY: 1, GemType.SAPPHIRE: 1, GemType.DIAMOND: 1},
                {GemType.OPAL: 2, GemType.RUBY: 1, GemType.SAPPHIRE: 1, GemType.DIAMOND: 1}
                ]:
                cards.add(Card(base_price=GemValue(price), gem_value=GemValue({batch_type: 1})))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 4}), gem_value=GemValue({batch_type: 1}), point_value=1))




        elif level == 2:
            batch_type = GemType.SAPPHIRE
            cards.add(Card(base_price=GemValue({GemType.RUBY: 3, GemType.EMERALD: 2, GemType.SAPPHIRE: 2}), gem_value=GemValue({batch_type: 1}), point_value=1))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 3, GemType.EMERALD: 3, GemType.SAPPHIRE: 2}), gem_value=GemValue({batch_type: 1}), point_value=1))

            cards.add(Card(base_price=GemValue({GemType.SAPPHIRE: 5}), gem_value=GemValue({batch_type: 1}), point_value=2))
            cards.add(Card(base_price=GemValue({GemType.SAPPHIRE: 3, GemType.DIAMOND: 5}), gem_value=GemValue({batch_type: 1}), point_value=2))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 4, GemType.RUBY: 1, GemType.DIAMOND: 2}), gem_value=GemValue({batch_type: 1}), point_value=2))

            cards.add(Card(base_price=GemValue({batch_type: 6}), gem_value=GemValue({batch_type: 1}), point_value=3))
            


            batch_type = GemType.RUBY
            cards.add(Card(base_price=GemValue({GemType.OPAL: 3, GemType.RUBY: 2, GemType.DIAMOND: 2}), gem_value=GemValue({batch_type: 1}), point_value=1))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 3, GemType.RUBY: 2, GemType.SAPPHIRE: 3}), gem_value=GemValue({batch_type: 1}), point_value=1))

            cards.add(Card(base_price=GemValue({GemType.OPAL: 5}), gem_value=GemValue({batch_type: 1}), point_value=2))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 5, GemType.DIAMOND: 3}), gem_value=GemValue({batch_type: 1}), point_value=2))
            cards.add(Card(base_price=GemValue({GemType.EMERALD: 2, GemType.SAPPHIRE: 4, GemType.DIAMOND: 1}), gem_value=GemValue({batch_type: 1}), point_value=2))

            cards.add(Card(base_price=GemValue({batch_type: 6}), gem_value=GemValue({batch_type: 1}), point_value=3))


            
            batch_type = GemType.OPAL
            cards.add(Card(base_price=GemValue({GemType.EMERALD: 2, GemType.SAPPHIRE: 2, GemType.DIAMOND: 3}), gem_value=GemValue({batch_type: 1}), point_value=1))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 2, GemType.EMERALD: 3, GemType.DIAMOND: 3}), gem_value=GemValue({batch_type: 1}), point_value=1))

            cards.add(Card(base_price=GemValue({GemType.DIAMOND: 5}), gem_value=GemValue({batch_type: 1}), point_value=2))
            cards.add(Card(base_price=GemValue({GemType.RUBY: 3, GemType.EMERALD: 5}), gem_value=GemValue({batch_type: 1}), point_value=2))
            cards.add(Card(base_price=GemValue({GemType.RUBY: 2, GemType.EMERALD: 4, GemType.SAPPHIRE: 1}), gem_value=GemValue({batch_type: 1}), point_value=2))

            cards.add(Card(base_price=GemValue({batch_type: 6}), gem_value=GemValue({batch_type: 1}), point_value=3))


            
            batch_type = GemType.DIAMOND
            cards.add(Card(base_price=GemValue({GemType.OPAL: 2, GemType.RUBY: 2, GemType.EMERALD: 3}), gem_value=GemValue({batch_type: 1}), point_value=1))
            cards.add(Card(base_price=GemValue({GemType.RUBY: 3, GemType.SAPPHIRE: 3, GemType.DIAMOND: 2}), gem_value=GemValue({batch_type: 1}), point_value=1))

            cards.add(Card(base_price=GemValue({GemType.RUBY: 5}), gem_value=GemValue({batch_type: 1}), point_value=2))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 3, GemType.RUBY: 5}), gem_value=GemValue({batch_type: 1}), point_value=2))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 2, GemType.RUBY: 4, GemType.EMERALD: 1}), gem_value=GemValue({batch_type: 1}), point_value=2))

            cards.add(Card(base_price=GemValue({batch_type: 6}), gem_value=GemValue({batch_type: 1}), point_value=3))


            batch_type = GemType.EMERALD
            cards.add(Card(base_price=GemValue({GemType.OPAL: 2, GemType.SAPPHIRE: 3, GemType.DIAMOND: 2}), gem_value=GemValue({batch_type: 1}), point_value=1))
            cards.add(Card(base_price=GemValue({GemType.RUBY: 3, GemType.EMERALD: 2, GemType.DIAMOND: 3}), gem_value=GemValue({batch_type: 1}), point_value=1))

            cards.add(Card(base_price=GemValue({GemType.EMERALD: 5}), gem_value=GemValue({batch_type: 1}), point_value=2))
            cards.add(Card(base_price=GemValue({GemType.EMERALD: 3, GemType.SAPPHIRE: 5}), gem_value=GemValue({batch_type: 1}), point_value=2))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 1, GemType.SAPPHIRE: 2, GemType.DIAMOND: 4}), gem_value=GemValue({batch_type: 1}), point_value=2))

            cards.add(Card(base_price=GemValue({batch_type: 6}), gem_value=GemValue({batch_type: 1}), point_value=3))


        elif level == 3:
            batch_type = GemType.SAPPHIRE
            cards.add(Card(base_price=GemValue({GemType.OPAL: 5, GemType.RUBY: 3, GemType.EMERALD: 3, GemType.DIAMOND: 3}), gem_value=GemValue({batch_type: 1}), point_value=3))

            cards.add(Card(base_price=GemValue({GemType.DIAMOND: 7}), gem_value=GemValue({batch_type: 1}), point_value=4))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 3, GemType.SAPPHIRE: 3, GemType.DIAMOND: 6}), gem_value=GemValue({batch_type: 1}), point_value=4))

            cards.add(Card(base_price=GemValue({GemType.SAPPHIRE: 3, GemType.DIAMOND: 7}), gem_value=GemValue({batch_type: 1}), point_value=5))


            batch_type = GemType.RUBY
            cards.add(Card(base_price=GemValue({GemType.OPAL: 3, GemType.EMERALD: 3, GemType.SAPPHIRE: 5, GemType.DIAMOND: 3}), gem_value=GemValue({batch_type: 1}), point_value=3))

            cards.add(Card(base_price=GemValue({GemType.EMERALD: 7}), gem_value=GemValue({batch_type: 1}), point_value=4))
            cards.add(Card(base_price=GemValue({GemType.RUBY: 3, GemType.EMERALD: 6, GemType.RUBY: 6, GemType.SAPPHIRE: 3}), gem_value=GemValue({batch_type: 1}), point_value=4))

            cards.add(Card(base_price=GemValue({GemType.RUBY: 3, GemType.EMERALD: 7}), gem_value=GemValue({batch_type: 1}), point_value=5))


            batch_type = GemType.OPAL
            cards.add(Card(base_price=GemValue({GemType.RUBY: 3, GemType.EMERALD: 5, GemType.SAPPHIRE: 3, GemType.DIAMOND: 3}), gem_value=GemValue({batch_type: 1}), point_value=3))

            cards.add(Card(base_price=GemValue({GemType.RUBY: 7}), gem_value=GemValue({batch_type: 1}), point_value=4))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 3, GemType.RUBY: 6, GemType.EMERALD: 3}), gem_value=GemValue({batch_type: 1}), point_value=4))

            cards.add(Card(base_price=GemValue({GemType.OPAL: 3, GemType.RUBY: 7}), gem_value=GemValue({batch_type: 1}), point_value=5))


            batch_type = GemType.DIAMOND
            cards.add(Card(base_price=GemValue({GemType.OPAL: 3, GemType.RUBY: 5, GemType.EMERALD: 3, GemType.SAPPHIRE: 3}), gem_value=GemValue({batch_type: 1}), point_value=3))

            cards.add(Card(base_price=GemValue({GemType.OPAL: 7}), gem_value=GemValue({batch_type: 1}), point_value=4))
            cards.add(Card(base_price=GemValue({GemType.OPAL: 6, GemType.RUBY: 3, GemType.DIAMOND: 3}), gem_value=GemValue({batch_type: 1}), point_value=4))

            cards.add(Card(base_price=GemValue({GemType.OPAL: 7, GemType.DIAMOND: 3}), gem_value=GemValue({batch_type: 1}), point_value=5))


            batch_type = GemType.EMERALD
            cards.add(Card(base_price=GemValue({GemType.OPAL: 3, GemType.RUBY: 3, GemType.SAPPHIRE: 3, GemType.DIAMOND: 5}), gem_value=GemValue({batch_type: 1}), point_value=3))

            cards.add(Card(base_price=GemValue({GemType.SAPPHIRE: 7}), gem_value=GemValue({batch_type: 1}), point_value=4))
            cards.add(Card(base_price=GemValue({GemType.EMERALD: 3, GemType.SAPPHIRE: 6, GemType.DIAMOND: 3}), gem_value=GemValue({batch_type: 1}), point_value=4))

            cards.add(Card(base_price=GemValue({GemType.EMERALD: 3, GemType.SAPPHIRE: 7}), gem_value=GemValue({batch_type: 1}), point_value=5))



        return Deck(cards)

class GemPool(object):
    def __init__(self, gems):
        self.gems = gems

    @staticmethod
    def gem_pool_factory(gem_count, gold_count):
        gems = {}
        for gem_type in GemType:
            gems[gem_type] = gem_count
        gems[GemType.GOLD] = gold_count
        return GemPool(gems)

class Gem(object):
    def __init__(self, gem_value):
        self.gem_value = gem_value

    def __str__(self):
        return str(self.gem_value)

class Noble(object):
    def __init__(self, point_value, gem_requirements):
        self.point_value = point_value
        self.gem_requirements = gem_requirements

class NoblePool(object):
    possible_nobles = set()
    usable_gem_types = [gem_type for gem_type in GemType if gem_type != GemType.GOLD]
    for c1 in usable_gem_types:
        for c2 in usable_gem_types:
            possible_nobles.add(Noble(3, GemValue({c1: 4, c2: 4})))
            if c1 != c2:
                for c3 in usable_gem_types:
                    if c1 != c3 and c2 != c3:
                        possible_nobles.add(Noble(3, GemValue({c1: 3, c2: 3, c3: 3})))

    @staticmethod
    def get_nobles(quantity):
        return random.sample(NoblePool.possible_nobles, quantity)

class Player(object):
    def __init__(self, gem_pool, nobles=None, reserved_cards=None, tableau=None, cards=None):
        if reserved_cards == None:
            reserved_cards = CardStorer()
        self.reserved_cards = reserved_cards
        if tableau == None:
            tableau = CardStorer()
        self.tableau = tableau
        if nobles == None:
            nobles = set()
        self.nobles = nobles
        self.gem_pool = gem_pool

    def get_points(self):
        return sum([card.point_value for card in self.cards], 
                   sum([noble.point_value for noble in self.nobles]))

    def get_price_for_card(self, card):
        to_return = dict(card.base_price)
        for gem_type, price in to_return.items():
            to_return[gem_type] = min(0, to_return[gem_type] - sum([card.gem_value[gem_type] for card in self.cards]))
        return to_return

    def buy_card(self, card, card_source, gem_bank):
        assert(SplendorGame.player_can_afford_card(self, card))
        for gem_type, cost in self.get_price_for_card(card):
            gold_cost = min(self.get_pool[gem_type] - cost, 0)
            cost = cost - gold_cost
            GemPool.move(gold_cost, GemType.GOLD, gem_bank)
            GemPool.move(cost, gem_type, gem_bank)
        card.move(card_source, self.tableau)

class SplendorGameFactory(object):
    @staticmethod
    def generate_game(players):
        card_rows = []
        decks = [Deck.create_deck(1), Deck.create_deck(2), Deck.create_deck(3)]
        for deck in decks:
            deck.shuffle()
            card_row = CardRow(deck, card_count=4)
            card_row.replenish()
            card_rows.append(card_row)
               
        nobles = NoblePool.get_nobles(len(players) + 1)
        if len(players) == 4:
            return SplendorGame(players, card_rows, decks, GemPool.gem_pool_factory(7, 5), nobles)
        else:
            raise Exception("Not implemented")

class SplendorGame(object):
    def __init__(self, players, card_rows, decks, gem_pool, nobles):
        self.available_nobles = nobles
        self.current_player = None
        self.players = players
        self.gem_pool = gem_pool

    @staticmethod
    def player_can_afford_card(player, card):
        for gem_type, gem_cost in player.get_price_for_card(card):
            if player.gem_pool[gem_type] < gem_cost:
                return False
        return True

    @staticmethod
    def player_can_take_noble(player, noble):
        for gem_requirement_gem_type, gem_requirement_quantity in noble.gem_requirements:
            if sum([gem.gem_value[gem_requirement_gem_type] for gem in player[gem_requirement_gem_type]])\
               < sum([card.gem_value[gem_requirement_gem_type] for card in player.cards]):
                return False
        return True

    def randomly_pick_starting_player(self):
        self.current_player = random.choice(self.players)
        return self.current_player

if __name__ == "__main__":
    players = [Player(GemPool.gem_pool_factory(0, 0)) for player in xrange(0, 4)]
    game = SplendorGameFactory.generate_game(players)
    game.randomly_pick_starting_player()
