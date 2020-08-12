print ("Hello world")

import random

class Card:
  def __init__(self, suit, val):
    self.suit = suit
    self.value = val

  def show(self):
    print ("{} of {}".format(self.value, self.suit))

class Deck:
  def __init__(self):
    self.cards = []
    self.build()

  def build(self):
    for s in ["Hearts", "Spades", "Diamonds", "Clubs"]:
      for v in range(1,14):
        self.cards.append(Card(s,v))

  def show(self):
    for c in self.cards:
      c.show()

  def shuffle(self): # Fisher-Yates shuffle algorithm
    for i in range(len(self.cards)-1,0,-1):
      r = random.randint(0,i)
      self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

  def drawCard(self):
    return self.cards.pop() # draw from top of card stack

class Player:
  def __init__(self, name):
    self.name = name
    self.hand = []

  def draw(self, deck):
    self.hand.append(deck.drawCard())
    return self

  def showHand(self):
    for card in self.hand:
      card.show()

class Game:
  def __init__(self):
    self.deck = Deck()
    self.deck.shuffle()
    self.table = []
    self.burnPile = []

  def newDeck(self):
    self.deck = Deck()
    self.deck.shuffle()
    self.table = []
    self.burnPile = []

  def burn(self):
    self.burnPile.append(self.deck.drawCard())

  def drawFlop(self):
    self.burn()
    for i in range(0,3):
      self.table.append(self.deck.drawCard())

  def showTable(self):
    for card in self.table:
      card.show()

  def pairsGame(self):
    self.newDeck()
    me = Player("Me")

    num_pairs = 0
    num_hands = 0
    identified_pairs = 0
    while True:
      me.draw(self.deck)
      me.draw(self.deck)

      self.drawFlop()
      print("Flop: ")
      self.showTable()
      print(" ")
      print("My hand: ")
      me.showHand()
      num_pairs, num_hands = self.askPairsQuestion(num_pairs, num_hands)
      identified_pairs += self.checkForPairs(me.hand,self.table)
      print('Computed number of pairs: {0:2d}'.format(identified_pairs))
      print(" ")
      self.deck = Deck()
      self.deck.shuffle()
      self.table = []
      self.burnPile = []
      me.hand = []

  def statistics(self):
    self.num_hands = 0
    self.num_pairs = 0
    # ??????

  def askPairsQuestion(self, num_pairs, num_hands): # statistics should not be kept here
    num_pairs += input("Number of pairs I hit on this hand: ")
    num_hands += 1

    print(" ")

    print('Total games: {0:2d}'.format(num_hands))
    print('Total pairs: {0:2d}'.format(num_pairs))

    return num_pairs, num_hands

  def checkForPairs(self, hand, table):

    table_values = []
    for card in table:
      table_values.append(card.value)

    for card in hand:
      if card.value in table_values:
        return True # a pair is found on the table

    if hand[0].value == hand[1].value:
      return True # the player is holding a pair

    return False # no pairs were found


def main():
  game = Game()
  for i in range(0,19):
    game.deck = Deck()
    game.deck.shuffle()
    game.burnPile = []
    game.table = []
    game.pairsGame()


if __name__ == '__main__':
    main()