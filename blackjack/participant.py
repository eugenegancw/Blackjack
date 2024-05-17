class Participant:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card_to_hand(self, card):
        self.hand.append(card)
    
    def calculate_score(self):
        total_score = sum(self.card_value(card) for card in self.hand)
        num_aces = len([card for card in self.hand if card.rank == "A"])
        while total_score > 21 and num_aces >0:
            total_score -= 10
            num_aces -= 1
        return total_score


    def card_value(self, card):
        if card.rank.isdigit():
            return int(card.get_rank())
        elif card.rank in ['J', 'Q', 'K']:
            return 10
        elif card.rank == 'A':
            return 11
        return 0
    
    def display_hand(self):
        print("-" * 20)
        print(f"{self.name}'s hand")
        for card in self.hand:
            display_txt = card.display()
            print(display_txt)
        print(f"Total points for {self.name}: {self.calculate_score()}")
        print("=" * 20)
