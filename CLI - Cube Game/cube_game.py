#The Cube Game #1

import random
import os

class Player:
    def __init__(self):
        self.roundscore = 0
        self.score = 0

class Game:
    def __init__(self):
        self.event = 1
        self.active = 1
        self.roundscore = 0
        self.dice = 0
        

    def play_game(self):
        if self.active ==1:
            self.player1_status()
        else:
            self.player2_status()
                
    def player1_status(self):
        os.system('clear')
        print("Player1*       |   Player 2")
        print(f"Score: {player1.score}       |   Score: {player2.score}")
        print(f"Roundscore: {player1.roundscore}  |   Roundscore: {player2.roundscore}")
        print(f"You rolled: {self.dice}")
        print("r - roll\nh - hold\nn - new game\ne - exit")
        self.menu = input()
        while True:
            if self.menu == "r":
                self.roll_btn()
            elif self.menu == "h":
                self.hold_btn()
            elif self.menu == "n":
                self.newgame_btn()
            elif self.menu == "e":
                quit()
            else:
                self.menu = input("Wrong alphabet!\n")
        
    def player2_status(self):
        os.system('clear')
        print("Player1        |   Player 2*")
        print(f"Score: {player1.score}       |   Score: {player2.score}")
        print(f"Roundscore: {player1.roundscore}  |   Roundscore: {player2.roundscore}")
        print(f"You rolled: {self.dice}")
        print("r - roll\nh - hold\nn - new game\ne - exit")
        self.menu = input()
        while True:
            if self.menu == "r":
                self.roll_btn()
            elif self.menu == "h":
                self.hold_btn()
            elif self.menu == "n":
                self.newgame_btn()
            elif self.menu == "e":
                quit()
            else:   
                self.menu = input("Wrong alphabet!\n")
    
    #Rolls with dice
    def roll_btn(self):
        #If the game isn't ended
        if self.event == 1:
            #Generate a dice number 1-6
            self.dice = random.randint(1, 6)
            
            #If Player 1 is active
            if self.active == 1:
                #If you rolled 1, roundscore is zero, then switch to Player 2
                if self.dice == 1:
                    player1.roundscore = 0
                    self.active = 2
                    self.player2_status()
                else:    
                    #Sum roundscore and print it
                    player1.roundscore += self.dice
                    self.player1_status()
            
            #If Player 2 is active
            else:
                #If you rolled 1, roundscore is zero, then switch to Player 1
                if self.dice == 1:
                    player2.roundscore = 0
                    self.active = 1
                    self.player1_status()
                else:    
                    #Sum roundscore and print it
                    player2.roundscore += self.dice
                    self.player2_status()
    def hold_btn(self):
        #If the game isn't ended
        if self.event == 1:
            #If Player 1 is active
            if self.active == 1:
                #Sum score, roundscore 0, and switch to Player 2
                player1.score = player1.roundscore
                
                #If score >= 50, then Player 1 win!
                if player1.score >= 20:
                    print("PLAYER 1 WIN!")
                    print("Type n for new game!")
                    self.event = 0
                    self.menu = input()
                    if self.menu == "n":
                        self.newgame_btn()
                    
                else:
                    player1.roundscore = 0
                    self.active = 2
                    self.player2_status()
                
            #If Player 2 is active    
            else:
                #Sum score, roundscore 0, and switch to Player 1
                player2.score = player2.roundscore
                
                #If score >= 50, then Player 2 win!
                if player2.score >= 50:
                    print("PLAYER 2 WIN!")
                    print("Type n for new game!")
                    self.event = 0
                    self.menu = input()
                    if self.menu == "n":
                        self.newgame_btn()
                    
                else:    
                    player2.roundscore = 0
                    self.active = 1
                    self.player1_status()
                    
    def newgame_btn(self):
        self.event = 1
        self.active = 1
        player1.roundscore = 0
        player2.roundscore = 0
        player1.score = 0
        player2.score = 0
        self.dice = 0
        self.play_game()
            

#Player 1, Player 2, Game
player1 = Player()
player2 = Player()
play = Game()

while True:
    play.play_game()