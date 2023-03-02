import Player
from Deck import Deck
import random
from const import MESSAGES


class Game:
    max_pl_count = 4

    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        # self.dealler = None
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def _launching(self):
        while True:
            bots_count = int(input('Hello write bots count '))
            if bots_count <= self.max_pl_count - 1:
                break
        self.all_players_count = bots_count + 1
        for _ in range(bots_count):
            b = Player.Bot()
            self.players.append(b)
            print(b, ' is created')
        self.player = Player.Player()
        self.player_pos = random.randint(0, self.all_players_count)
        print('Your position is: ', self.player_pos)
        self.players.insert(self.player_pos, self.player)

    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

    def first_descr(self):
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)

    def ask_card(self):
        for player in self.players:
            while player.ask_card():
                card = self.deck.get_card()
                player.take_card(card)
                if isinstance(player, Player.Player):
                    print('Your last cards: ')
                    self.player.print_cards()

    def start_game(self):
        message = MESSAGES.get('ask_start')
        # todo: max player count?
        if not self._ask_starting(message=message):
            exit(1)

        # generating for starting
        self._launching()
        # ask about bet
        self.ask_bet()
        # give first cards to the players
        self.first_descr()
        # print card first deck
        self.player.print_cards()
        # ask player about cards
        self.ask_card()