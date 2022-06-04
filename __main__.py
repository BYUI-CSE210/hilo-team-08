

import random
import time 

print("Welcome to a game of Hilo")
time.sleep(0.5)

print()

name = input("What is your name? ")

print()

print(f"Hello {name}. You have 300 points.")


class cards:

    def __init__(self, current_card):
        self.current_card = current_card

        def current_card(self):
                return self.current_card

class card:

    def __init__(self, next_card):
        self.next_card = next_card

        def next_card(self):
                return self.next_card

cards = (random.randint(1,13))
card = (random.randint(1,13))

points = 300

print(cards)

answer = print(input("Is the next card higher or lower? (higher / lower): "))

print(card)
         
current_card = cards
next_card = card

if answer == 'higher' and (current_card < next_card):
   points += 100
   print(f"You now have {points} points")
                                        
elif answer == 'lower' and (current_card > next_card):
   points += 100
   print(f"You now have {points} points")
                                        
elif answer == 'higher' and (current_card > next_card):
   points -= 75
   print(f"You now have {points} points")

elif answer == 'lower' and (current_card < next_card):
     points -= 75
     print(f"You now have {points} points")

else:
     print('Invalid input. Please try again.')
     answer

if points == 0:
     print('You lose. Thank you for playing')

elif points != 0:
     keep_playing = (input(f'You have {points}. Would you like to continue playing? (Y/N).'))

if keep_playing == "n" or "N":
        print("Thank you for playing")

        
                                
