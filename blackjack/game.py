from .deck import Deck
from .dealer import Dealer
from .player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.round_ended = 0
        self.round_number = 1
        name_ = input("What is your name? ").title()
        self.player = Player(name_)

    def start_game(self):
        print("Welcome to Blackjack!")
        while self.player.points > 0:
            self.begin_round()
            print(f"Round {self.round_number} ended. Current points: {self.player.points}")
            if self.player.points <= 0:
                print("Game over! You have 0 points left.")
                break
            if not self.continue_game():
                break

    def continue_game(self):
        while True:
            continue_game = input("Do you still want to play another round? (yes/no): ").strip().lower()
            if continue_game == 'no':
                print(f"Game ended. Your final points: {self.player.points}")
                return False
            elif continue_game == 'yes':
                self.round_ended = False  # reset the whole round
                self.round_number += 1
                return True
            else:
                print("Invalid choice. Please try again!")

    def begin_round(self):
        print(f"\nStarting Round {self.round_number}")
        self.deck.shuffle()
        self.initial_cards_setup()
        self.check_blackjack()  # Check for blackjack after initial cards setup

        if not self.round_ended:
            self.player_move()
            player_score = self.player.calculate_score()
            if player_score > 21:
                self.all_display_hands(True)
                print("You bursts! Dealer wins.")
                self.player.points -= 10
                self.round_ended = 1

        if not self.round_ended:
            self.dealer_move()
            self.output_round_winner()
            self.round_ended = 1

    def initial_cards_setup(self):
        # Clear the hands for a new round
        self.player.hand, self.dealer.hand = [], []
        for _ in range(2):
            self.player.add_card_to_hand(self.deck.deal_card())
            self.dealer.add_card_to_hand(self.deck.deal_card())

    def player_move(self):
        while self.player.calculate_score() <= 21:
            self.all_display_hands()
            option_ = input("Do you want to Hit or Stay? (hit/stay): ").strip().lower()
            if option_ == "hit":
                self.player.add_card_to_hand(self.deck.deal_card())
            elif option_ == "stay":
                break
            else:
                print("Invalid choice. Please try again!")

    def dealer_move(self):
        while self.dealer.calculate_score() <= 16:
            self.dealer.add_card_to_hand(self.deck.deal_card())

    def check_blackjack(self):
        if self.dealer.calculate_score() == 21:  # Dealer's advantage
            self.all_display_hands(True)
            print("Dealer got Blackjack! You lose.")
            self.player.points -= 10
            self.round_ended = 1

        elif self.player.calculate_score() == 21:
            self.all_display_hands(True)
            print(f"{self.player.name} got Blackjack! Congratulations!")
            self.player.points += 15
            self.round_ended = 1

    def output_round_winner(self):
        player_score = self.player.calculate_score()
        dealer_score = self.dealer.calculate_score()
        self.all_display_hands(True)
        if dealer_score > 21 or dealer_score < player_score:
            print("You win!")
            self.player.points += 10
        elif dealer_score <= 21 and dealer_score > player_score:
            print("Dealer wins!")
            self.player.points -= 10
        elif dealer_score == player_score:
            print("Push! No points for this round.")

    def all_display_hands(self, reveal_dealer=False):
        self.player.display_hand()
        self.dealer.display_hand(reveal_full_hand=reveal_dealer)
