from replit import clear
import random
from art import logo
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
def user():
    n=random.choice(cards)
    user_drawn_cards.append(n)
    
def computer():
    nu=random.choice(cards)
    comp_drawn_cards.append(nu)
    
user_drawn_cards=[]
comp_drawn_cards=[]

def scores(user_drawn_cards):
  print(f"Your cards:- {user_drawn_cards}, your score:- {current_score}")
  n=len(user_drawn_cards)
  for i in range(1, n):
    computer()
  comp_score=sum(comp_drawn_cards)  
  print(f"Computer Chose:- {comp_drawn_cards}, computer's score:- {comp_score}") 

def compare():
  comp_score=sum(comp_drawn_cards)
  if current_score==comp_score:
   print("Draw!!!")
  elif comp_score>21:
    print("Computer Exceeded 21😲\nYou Winn!!😁") 
  else:    
    if current_score>=19:
      if comp_score>=19:
        if current_score>comp_score:
          print("You are ahead of the Computer!\nYou WIN!😇") 
        else:
          print("Your score is lesser than Computer's!\nYou LOSE!😩")
      else:
        print("Computer's Score is lesser than 19! AND Your's is more than 19, So..\nYou WIN!😇")
    else:
      if current_score<comp_score:
        print("Your score is lesser than Computer!!(for condition: score<19)\nYou WIN!!😇")
      else:
        print("Your Score is more than The Computer's(for condition: score<19)\nYou LOSE!😩") 
note=input("Do you want to go through the rules? Type 'y' if yes!").lower()
if note=="y":
  print("---------------------")
  print("Here the computer is the dealer, and Cards are chosen at random from deck!\nIf your score exceeds 21, You Lose😩---\nThe Score(from 19 to 21) greater in comparison with the dealer and user is considered Winner 🥳")
  print("If score lesser than 19? The one having score less in comparison is the Winner!! 🥳")
  print("All the best! Enjoy!")
ready=input("Ready?-------Type 'yes'!!!").lower()

clear() 
if not ready=='yes':
  print("Not Ready? Play Anyways😁")              
print(logo)
user()
user()
computer()
computer()
current_score=sum(user_drawn_cards)
comp_score=sum(comp_drawn_cards)
print(f"You Cards:- {user_drawn_cards}, your current score:- {current_score} ")
print(f"Computer Cards:- {comp_drawn_cards}, computer's score:- {comp_score}")

add_card=input("Do you want to pick one more card?----Type'y' for yes or 'n' to pass: ").lower()
if add_card=='n':
  scores(user_drawn_cards)
  compare()
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.          


while add_card=="y":
  user()
  current_score=sum(user_drawn_cards)
  comp_score=sum(comp_drawn_cards)
  if current_score>21:
    print(f"Your cards:- {user_drawn_cards}, your score:- {current_score}")
    print(f"Computer earlier Chose:- {comp_drawn_cards}")
    print("You Exceeded 21😲\nYou Lose!!😱")
    add_card="n"
    break  
  else:  
    print(f"Your cards:- {user_drawn_cards}, your current score:- {current_score}")
    print(f"Computer earlier Chose:- {comp_drawn_cards}")
    add_card=input("Do you want to pick one more card?----Type'y' for yes or 'n' to pass ☺️ ").lower()
  if add_card=='n':
    scores(user_drawn_cards)
    compare()  

      



   




    

############## Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
# http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

