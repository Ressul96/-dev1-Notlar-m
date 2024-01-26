import random as rn
from art import logo

bet_count=0
bank=500
Ace= 11
Queen= 10
King= 10
Jack= 10
Deck = [Ace, Queen, King, Jack, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_hand=[]
comp_hand=[]
game_over=True
user_score=0
comp_score=0
overall_score=0
cash_out=False
win=0

def hit():
  user_hand.append(rn.choice(Deck))
  print(user_hand)
def bet():
  global bet_count
  global bank
  bet_count=int(input("Your bet?"))
  if bet_count>bank:
    print("You don't have that much money.")
    bet()
  else:
    bank -= bet_count

def comp_hit():
  for i in range(0,3):
    a=rn.randint(0,1)
    if a==0:
      comp_hand.append(rn.choice(Deck))
      

def deal_card():
  user_hand.clear()
  comp_hand.clear()
  user_hand.append(rn.choice(Deck))
  user_hand.append(rn.choice(Deck))
  comp_hand.append(rn.choice(Deck))
  comp_hand.append(rn.choice(Deck)) 
  
def score():
  global overall_score
  global game_over
  global user_score
  global comp_score
  global win
  user_score=int(sum(user_hand))
  comp_score=int(sum(comp_hand))
  overall_score=int(user_score-comp_score)
  if user_score>21:
    print(f"Your hand is {user_hand}. You lose ")
    win=1
    game_over=False
  elif comp_score>21:
    print(f"Computer's hand is {comp_hand}. You win")
    game_over=False
    win=2
  elif user_score==21:
    print(f"Your hand is {user_hand}. BLACKJACK!")
    game_over=False
    win=2
  elif comp_score==21:
    print(f"Computer's hand is {comp_hand}. BLACKJACK!")
    game_over=False
    win=1
    
    
def stand():
  global win
  comp_hit()
  score()
  if comp_score <21 and user_score<21:
    if overall_score>0:
      print(f"Your hand is {user_hand}.\nComputer's hand is {comp_hand}. You win ")
      win=2
    elif overall_score<0:
      print(f"Your hand is {user_hand}.\nComputer's hand is {comp_hand}. You lose")
      win=1
    elif overall_score==0:
      print(f"Your hand is {user_hand}.\nComputer's hand is {comp_hand}. Draw")

def one_turn():
  global game_over
  game_over=True
  deal_card()
  print(f"your hand is {user_hand}")
  print(f"computer's first card is {comp_hand[0]}")
  score()
  a=0
  while game_over:
    hit_stand=input("Hit or stand?\n").lower()
 
    if a==2:
      stand()
      game_over=False
    elif hit_stand=="hit":
      hit()
      a= a+1
    elif hit_stand=="stand":
      stand()
      game_over=False

if input("Wanna play blackjack? Yes or No\n").lower() == "yes":
  print(logo)
  print(f"bank gives you ${bank} credit")
  while bank>0 and cash_out==False:
    bet()
    one_turn()
    if win==0:
      bank+= bet_count
    elif win==2:
      bank+= bet_count*2
    print(f"You've ${bank}")
    if input("cash out?") =="yes":
      print(f"Game is over. You've ${bank}")
      cash_out=True
      
      
 

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

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

