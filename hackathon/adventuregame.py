import random

class Card:
    def __init__(self, suite, value, name):
        self.suite = suite
        self.value = value
        self.name = name

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(1, 14):
            self.cardHelper("Hearts", i)
        for i in range(1, 14):
            self.cardHelper("Diamonds", i)
        for i in range(1, 14):
            self.cardHelper("Clubs", i)
        for i in range(1, 14):
            self.cardHelper("Spades", i)
    def cardHelper(self, suite, value):
            if(value == 11):
                self.deck.append(Card(suite, 10, "Jack"))
            elif(value == 12):
                self.deck.append(Card(suite, 10, "Queen"))
            elif(value == 13):
                self.deck.append(Card(suite, 10, "King"))
            elif (value == 1):
                self.deck.append(Card(suite, 11, "Ace"))
            else:
                self.deck.append(Card(suite, value, str(value)))

mydeck = Deck()
print("Please enter your name:")
player_name = input()
print("Hello, " + player_name + "!")

playagain = True
while (playagain):
    mycard = random.randint(0,51)
    mysuite = ""
    if mydeck.deck[mycard].suite == "Hearts":
        mysuite = "♥️"
    elif mydeck.deck[mycard].suite == "Diamonds":
        mysuite = "♦️"
    elif mydeck.deck[mycard].suite == "Clubs":
        mysuite = "♣️"
    elif mydeck.deck[mycard].suite == "Spades":
        mysuite = "♠️"
    else:
        mysuite = mydeck.deck[mycard].suite
    mycardname = str(mydeck.deck[mycard].name) + " of " + mydeck.deck[mycard].suite
    mynewcardname = str(mydeck.deck[mycard].name) + " of " + mysuite
    if player_name == "Dennis":
        print(mycardname)
    print("Guess the top card in the deck:")
    player_choice = input()
    if player_choice == mycardname:
        print("Correct! ☺️")
    else:
        print("Sorry, " + player_name + ", it's the " + mynewcardname + ".")
    print("Would you like to play again? (y/n)")
    yes_or_no = input()
    if yes_or_no == "n":
        break
