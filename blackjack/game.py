from .deck import Deck
from .dealer import Dealer
from .player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.round_ended = 0
        name_ = input("What is your name? ").title()
        self.player = Player(name_)
    
    def start_game(self):
        print("Welcome to Blackjack!")
        while self.player.score > 0:
            self.begin_round()
            print(f"Current score: {self.player.score}")
            if self.player.score <= 0:
                print("Game over! You have 0 points left.")
                break
            continue_game = input("Do you still want to play another round? (yes/no)").strip().lower()
            if continue_game == 'no':
                print(f"Game ended. Your final score: {self.player.score}")
                break
            elif continue_game == 'yes':
                self.round_ended = 0 # reset the whole round
                continue
            else:
                print("Invalid choice. Please try again!")


    def begin_round(self):
        self.deck.shuffle()
        self.initial_cards_setup()
        self.output_blackjack()  # Check for blackjack after initial cards setup
        
        if not self.round_ended:
            self.player_move()
            player_points = self.player.calculate_points()
            #handle black jack case
            if player_points > 21:
                self.player.display_hand()
                print("You bursts! Dealer wins.")
                self.player.score -= 10
                self.round_ended = 1
        if not self.round_ended:
            self.dealer_move()
            self.output_round_winner()
            self.round_ended = 1


    def initial_cards_setup(self):
        # Clear the hands for a new round
        self.player.hand = []
        self.dealer.hand = []
        for _ in range(2):
            self.player.add_card_to_hand(self.deck.deal_card())
            self.dealer.add_card_to_hand(self.deck.deal_card())
    
    def player_move(self): #this player move will be based on the user
        while self.player.calculate_points() <= 21:
            self.player.display_hand()
            self.dealer.display_hand()
            option_ = input("Do you want to Hit or Stay? (hit/stay): ").strip().lower()
            if option_ == "hit":
                self.player.add_card_to_hand(self.deck.deal_card())
            elif option_ == "stay":
                break
            else:
                print("Invalid choice. Please try again!")
    
    def dealer_move(self):
        while self.dealer.calculate_points() <= 16:
            self.dealer.add_card_to_hand(self.deck.deal_card())

    def output_blackjack(self):
        if self.dealer.calculate_points() == 21: #doesn't matter if player get blackjack
            self.player.display_hand()
            self.dealer.display_hand(reveal_full_hand = True)
            print("Dealer got Blackjack! You lose.")
            self.player.score -= 10
            self.round_ended = 1
        
        elif self.player.calculate_points() == 21:
            self.player.display_hand()
            self.dealer.display_hand(reveal_full_hand = True)
            print(f"{self.player.name} got Blackjack! Congratulations!")
            self.player.score += 15
            self.round_ended = 1
        

    def output_round_winner(self):
        player_points = self.player.calculate_points()
        dealer_points = self.dealer.calculate_points()
        self.player.display_hand()
        self.dealer.display_hand(reveal_full_hand = True)
        # print(f"{self.player.name}'s points: {player_points} vs Dealer's ppoints: {dealer_points}")
        if dealer_points > 21 or dealer_points < player_points:
            print("You win!")
            self.player.score +=10
        elif dealer_points <= 21 and dealer_points > player_points:
            print("Dealer wins!")
            self.player.score -= 10
        elif dealer_points == player_points:
            print("Push! No points for this round.")
