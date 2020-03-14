import time
from random import randrange
import os

def prGreen(skk):
    print("\033[92m{}\033[00m" .format(skk))


def prRed(skk):
    print("\033[91m{}\033[00m" .format(skk))


def prYellow(skk):
    print("\033[93m{}\033[00m" .format(skk))


class Deck:
    def __init__(self):
        cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        card_types = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
        self.deck_o_cards = []
        for type in card_types:
            for card in cards:
                self.deck_o_cards.append(card+' of '+type)

    def show_deck(self):
        print(self.deck_o_cards)

class Player:
    num_of_players=0
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.cash = 500
        self.aces = 0
        Player.num_of_players += 1

    def reset(self):
        self.hand_value = 0
        self.hand = []
        self.aces = 0

    def win(self):
        self.cash = self.cash+50

    def lose(self):
        self.cash = self.cash-50

    def convert_hand_value(self):
        self.aces = 0
        card_value = 0
        for card in self.hand:
            card_number = card.split(" ")[0]
            if card_number == "King" or card_number == "Queen" or card_number == "Jack":
                card_value=card_value+10
            elif card_number == "Ace":
                self.aces = self.aces+1
            else:
                card_value=card_value+int(card_number)
        self.hand_value = card_value

        if self.aces > 1:
            if self.hand_value > 10:
                self.hand_value = self.hand_value+self.aces
            else:
                potential_value_1s = self.hand_value+self.aces
                potential_value_11_1s = self.hand_value+(self.aces-1)+11
                ace_input_1 = int(input(str(potential_value_1s)+' or '+str(potential_value_11_1s)+'?'))
                self.hand_value = ace_input_1
        elif self.aces == 1:
            if self.hand_value == 10:
                self.hand_value = 21
            elif self.hand_value > 10:
                self.hand_value = self.hand_value+1
            elif self.hand_value < 10:
                potential_value_1 = self.hand_value+1
                potential_value_11 = self.hand_value+11
                ace_input = int(input(str(potential_value_1)+' or '+str(potential_value_11)+'?'))
                self.hand_value=ace_input
        else:
            pass

        return self.hand_value

class Fourdeck:
    def __init__(self):
        self.four_deck = []

    def add_deck(self,deck):
        self.four_deck = self.four_deck+deck
        return

    def show_stack(self):
        return self.four_deck

    def check_cards(self):
        if len(self.four_deck) == (52*4):
            return True
        else:
            return False

    def is_empty(self):
        if len(self.four_deck) <= 4:
            return True
        else:
            return False

    def hit(self):
        return self.four_deck.pop()

    def shuffle(self):
        shuffled_cards = []
        while len(self.four_deck) >= 1:
            if len(self.four_deck) == 1:
                shuffled_cards.append(self.four_deck.pop(0))
            else:
                shuffled_cards.append(self.four_deck.pop(randrange(0,len(self.four_deck)-1)))
        self.four_deck = shuffled_cards

stack = Fourdeck()
for i in range(1,5):
    d = Deck()
    stack.add_deck(d.deck_o_cards)

stack.shuffle()
p1 = Player()
d1 = Player()

os.system('clear')
print("""Let's play Blackjack!\n""")
while not stack.is_empty():
    print("Dealing cards...\n")
    time.sleep(0.5)
    p1.hand.append(stack.hit())
    print("Your first card",p1.hand)
    time.sleep(0.5)
    d1.hand.append(stack.hit())
    prYellow("Dealer shows:"+str(d1.hand)+'\n')
    time.sleep(0.5)
    p1.hand.append(stack.hit())
    print("Your hand:",p1.hand)
    p1.convert_hand_value()
    print("Your hand value:",p1.hand_value,'\n')
    d1.hand.append(stack.hit())

    if p1.hand_value == 21:
        prGreen("\n\tYou win!\n")
        p1.win()
        print("You have $", p1.cash)
        p1.reset()
        d1.reset()
        time.sleep(1.5)
        os.system('clear')
    else:
        stay_or_hit = input("Hit or Stay (H/S)? ")
        reset_game=False
        while stay_or_hit.upper() == 'H' and p1.hand_value <= 21 and not reset_game:
            p1.hand.append(stack.hit())
            p1.convert_hand_value()
            time.sleep(0.5)
            print("Your hand:", p1.hand, p1.hand_value)
            if p1.hand_value > 21:
                print("You busted! :(")
                prRed("\n\t Dealer Wins!\n")
                p1.lose()
                print("You have $",p1.cash)
                time.sleep(1.5)
                p1.reset()
                d1.reset()
                os.system('clear')
                reset_game=True
            else:
                stay_or_hit = input("Hit or Stay (H/S)? ")
                time.sleep(0.5)

        if p1.hand_value <= 21 and not reset_game:
            print("Dealer has:",d1.hand)
            d1.convert_hand_value()
            if d1.hand_value > p1.hand_value and d1.hand_value >= 17:
                prRed("\n\tDealer wins!\n")
                p1.lose()
                print("You have $", p1.cash)
                p1.reset()
                d1.reset()
                reset_game=True
                time.sleep(1.5)
                os.system('clear')

            while d1.hand_value < 17 and not reset_game:
                print("Dealer hits...")
                time.sleep(0.5)
                d1.hand.append(stack.hit())
                print(d1.hand)
                d1.convert_hand_value()
                print(d1.hand, d1.hand_value)

            if d1.hand_value > 21 and not reset_game:
                prGreen("\n\tDealer busts! YOU WIN :)\n")
                p1.win()
                print("You have $", p1.cash)
                p1.reset()
                d1.reset()
                time.sleep(1.5)
                os.system('clear')
            elif d1.hand_value > p1.hand_value and not reset_game:
                prRed("\n\tDealer wins! :(\n")
                p1.lose()
                print("You have $", p1.cash)
                p1.reset()
                d1.reset()
                time.sleep(1.5)
                os.system('clear')
            elif d1.hand_value == p1.hand_value and not reset_game:
                print("\n\tEven... :/")
                print("You have $", p1.cash)
                p1.reset()
                d1.reset()
                time.sleep(1.5)
                os.system('clear')
            elif d1.hand_value < p1.hand_value and not reset_game:
                prGreen("\n\tYOU WIN! :)\n")
                p1.win()
                print("You have $", p1.cash)
                p1.reset()
                d1.reset()
                time.sleep(1.5)
                os.system('clear')
            else:
                p1.reset()
                d1.reset()
        else:
            pass

print("You ended up netting: ",str(p1.cash-500))
print("Game Over, we are out of cards")


# Blackjack
# 1 dealer
# hits on soft 17
# stays on anything above 17
# dealer shows first card that is dealt to him.
# dealer has 1 card face down.

# ace can be 1 or 11
# if the player has cards  > 10, the ace is automatically 1.
# if the player has cards <= 10, the player may choose 1 or 11

# each player has a move to "Stay" or "Hit"

# any player including the dealer, who has more than 21 busts
# any player who gets 21 from the draw wins automatically.
# player and dealer can draw on 21 if the player hits to get 21.

# up to 6 players
# 4 decks

