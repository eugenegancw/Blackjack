# Blackjack Game

**Overview**

This package implements a simple console-based Blackjack game. The design is modular, making it easy to understand, maintain, and extend. The main components are the Deck, Card, Participant, Dealer, Player, and Game classes.

---
**Folder Structure**
* [blackjack/](./Blackjack/blackjack)
  * [card.py](./Blackjack/blackjack/card.py)
  * [dealer.py](./Blackjack/blackjack/dealer.py)
  * [deck.py](./Blackjack/blackjack/deck.py)
  * [game.py](./Blackjack/blackjack/game.py)
  * [participant.py](./Blackjack/blackjack/participant.py)
  * [player.py](./Blackjack/blackjack/player.py)
* [.gitignore](./Blackjack/.gitignore)
* [main.py](./Blackjack/main.py)
* [requirements.txt](./Blackjack/requirements.txt)

<br>
---

<ins>**Design of the Code**</ins>

**Class Structure**

- **Card**: Represents a single card in the deck.
- **Deck**: Represents a deck of cards, allowing shuffling, dealing and even reshuffling.
- **Participant**: A superclass for both players and the dealer, containing common methods like adding cards to hand and calculating scores.
- **Dealer**: Inherits from Participant and represents the dealer.
- **Player**: Inherits from Participant and represents a player. Additionally, it tracks the player's points.
- **Game**: Manages the flow of the game, including dealing cards, handling player and dealer moves, and determining the winner of each round.

**Inheritance and Superclass**

The Participant class serves as a superclass for Player and Dealer. This design avoids code duplication by allowing common functionality, like managing a hand of cards, to be implemented once in the Participant class and reused by both Player and Dealer.

<ins>**Instructions for Execution**</ins>

**Steps to Execute**

1. Ensure you have Python installed on your machine and install requirements using: *pip install -r requirements.txt*
1. Navigate to the main directory.
1. To play the game, run the following command: *python main.py* 

**Game Flow**:

1. A new round starts by shuffling the deck, dealing two cards to the player and the dealer, and checking for Blackjack immediately.
1. If neither the player nor the dealer has Blackjack, the player can choose to hit or stay until they either bust (exceed 21) or decide to stay.
   1. During this point, the player’s hand is revealed in the console, while only the dealer’s first card is revealed.
1. After the player stays, the dealer draws cards until his score is 17 or higher.
1. All the hands are revealed for both the player and dealer, and the winner is determined based on the final scores.
1. The player’s points are adjusted accordingly based on that round’s outcome.
1. You can decide whether to continue playing after each round, but it is dependent on the amount of points you are left with.


<ins>**Assumptions**</ins>

1. **Starting Points**:
   1. Every player starts with 100 points, similar to the initial buy-in at a casino. This provides players with a starting balance for participating in multiple rounds.
1. **Game Continuation**:
   1. Players can continue playing rounds until they have no points left. This allows for extended gameplay and numerous opportunities to win or lose points.
1. **Dealer's Advantage**:
   1. If a player’s score exceeds 21, it is considered a loss for the player, regardless of the dealer's hand. 
   1. If the Dealer gets a Blackjack, it is also considered a loss for the player, regardless of the player’s hand.
   1. Both assumptions simplify the game logic and outcome determination, ensuring clarity in scoring.
1. **Standard Loss Penalty**: 
   1. Any loss incurred by the player, regardless of whether the dealer gets a blackjack or the player exceeds 21, results in a deduction of 10 points. This simplifies the scoring mechanism, ensuring consistency in point adjustments for all loss scenarios.
1. **Automatic Player Stop**:
   1. The game automatically stops for a player if his score exceeds 21 during a round. Drawing cards beyond 21 is unnecessary and is a loss regardless of the dealer's hand.
1. **Input Handling:**
   1. The player’s name is the input at the start of the game for a personalised experience.
   1. Input for making decisions, i.e. whether to hit/stay or continue the game, is handled in a loop until valid input is provided
1. **Minimum Hand Requirement:**
   1. It is assumed that users are aware that they must achieve at least a minimum hand value of 12 to participate in the game.


<ins>**Future Work**</ins>

1. **Support for Multiple Players**:
   1. Extend the game to support more than one player competing against the dealer in the same round.
1. **More features in Blackjack**:
   1. This Blackjack implementation currently does not support certain winning scenarios like obtaining five cards without exceeding 21 or holding a hand with two aces. Integrating these features would enrich the gameplay by offering additional winning opportunities and strategic depth.
1. **Additional Betting Options:**
   1. Introduce features such as doubling down or even allowing the modification of the number of points gained/lost in each round.