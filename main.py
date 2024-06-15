import random
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card

def calculate_score(cards):
  if len(cards)==2 and 11 in cards and 10 in cards: #sum(cards)==21 and len(cards)==2
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score==computer_score:
    return "Draw!"
  elif computer_score==0 or user_score>21:
    return "Computer wins!"
  elif user_score==0 or computer_score>21:
    return "User wins!"
  elif computer_score>user_score:
      return "Computer wins!"
  else:
    return "User wins!"

def play_game():

  print(logo)
  
  user_cards=[]
  computer_cards=[]
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  is_game_over=False
  while True:
    if is_game_over==True:
      break
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over=True

    if is_game_over==False:
      ask=input("Press 'y' to draw a card, 'n' to end the game: ")
      if ask=="y":
        user_cards.append(deal_card())
      elif ask=="n":
        is_game_over=True

  while True:
    if computer_score !=0 and computer_score<17:
      computer_cards.append(deal_card())
      computer_score=calculate_score(computer_cards)
    else:
      break

  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you want to Play a game o fblackjack? Type 'y'or 'n': ")=="y":
  clear()
  play_game()
