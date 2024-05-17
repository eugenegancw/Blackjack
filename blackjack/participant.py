class Participant:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def get_score(self):
        return self.score

    def add_card_to_hand(self, card):
        self.hand.append(card)
    
    def calculate_points(self):
        total_points = sum(self.card_value(card) for card in self.hand)
        num_aces = len([card for card in self.hand if card.rank == "A"])
        while total_points > 21 and num_aces >0:
            total_points -= 10
            num_aces -= 1
        return total_points


    def card_value(self, card):
        if card.rank.isdigit():
            return int(card.get_rank())
        elif card.rank in ['J', 'Q', 'K']:
            return 10
        elif card.rank == 'A':
            return 11
        return 0
    
    def display_hand(self):
        print(f"{self.name}'s hand")
        for card in self.hand:
            display_txt = card.display()
            print(display_txt)
        print(f"Total points for {self.name}: {self.calculate_points()}")
