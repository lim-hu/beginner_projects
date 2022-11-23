#Blackjack

import random
import os

#---Create the cards---
class Card:
  
  colors = ["Pikes", "Treff", "Hearts", "Diamond"]
  numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
  }

#---Build the deck and shuffle it---
class Deck:

  def __init__(self):
    self.cards = []
    self.pulled = []

  def build_deck(self):
    for c in range(4):
      for n in range(13):
        self.cards.append(f'{Card.colors[c]} {Card.numbers[n]}')

  def shuffle_deck(self):
    random.shuffle(self.cards)


#---Declare the score and win's number of player---
class Player:
  
  def __init__(self):
    self.score = 0
    self.wins = 0
    self.pulled = []
    self.active = 1

#---Algorithm of the game---
class Game:

  def __init__(self):
    self.event = 1

  def play_game(self):
    if self.event == 1:
      self.status1()
      self.main_menu()

  def status1(self):
    os.system('clear')
    print("Player 1*     Player 2")
    print(f"Score: {player1.score}      Score: {player2.score}")
    print("Win: 0         Win: 0")
    print("p - pull card")
    print("h - hold")
    print("n - new game")
    
  def status2(self):
    os.system('clear')
    print("Player 1      Player 2*")
    print(f"Score: {player1.score}      Score: {player2.score}")
    print("Win: 0         Win: 0")
    print("p - pull card")
    print("h - hold")
    print("n - new game")

  def main_menu(self):
    self.menu = input()
    while True:
      if self.menu == "p":
        self.pull_card()

      elif self.menu == "h":
        pass

      elif self.menu == "n":
        pass

      else:
        self.menu = input()
    
  
  def pull_card(self):
    if player1.active == 1:  
      #Pull a card and add to score
      player1.pulled.append(deck.cards.pop(0))
      p_card = player1.pulled[-1]
      player1.score += Card.values[f'{p_card[-2:]}'.strip()]

      #If score higher as 21, then switch player
      if player1.score >= 22:
        print("Your score is higher as 21! Player 2 win.")
     #   player.2.win????!!!¿
      else:
        print(p_card)
        self.status1()
        print('Pulled cards: ')
        for p in player1.pulled:
          print(p)
        self.main_menu()
    else:
      #Pull a card and add to score
      player2.pulled.append(deck.cards.pop(0))
      p_card = player2.pulled[-1]
      player2.score += Card.values[f'{p_card[-2:]}'.strip()]

      #If score higher as 21, then switch player
      if player2.score >= 22:
        print("Your score is higher as 21! Player 1 win.")
    #    Player 1 win!!!!???
      else:
        print(p_card)
        self.status1()
        print('Pulled cards: ')
        for p in player1.pulled:
          print(p)
        self.main_menu()


  def hold(self):
    pass

  def nextturn(self):
    pass

  def newgame(self):
    self.event = 1




#---Game Events---

#Build deck and shuffle it
deck = Deck()
deck.build_deck()
deck.shuffle_deck()

#Create the player and NPC
player1 = Player()
player2 = Player()

#Create the game and play it
blackjack = Game()
blackjack.play_game()


# #Check value of the card (example)
# card = str(deck.cards[51])
# print(Card.values[f'{card[-2:]}'.strip()])

