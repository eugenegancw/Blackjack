from .participant import Participant


class Dealer(Participant):
    def __init__(self):
        super().__init__("Dealer")

    def display_hand(self, reveal_full_hand=False):
        if reveal_full_hand:
            super().display_hand()
        else:
            print("-" * 20)
            print("Dealer's hand")
            print(self.hand[0].display())
            print("**Hidden card**")
            print("=" * 20)
