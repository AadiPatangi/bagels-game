#bagelsgame
#aadi
print("Welcome to the bagels game by Aadi \n")
print("************************************")

import random
num = str(random.randint(100, 999))
guesses = 10
x = 0
guess = 000

def checker(guess, num):
  if guess[x] == num[x]:
    print("Fermi")
  elif guess[x] in num:
    print("Pico")
  elif guess[x] not in num:
    print("Bagels")

while guesses != 0 and guess != num:
  print(str(guesses) + " guesses left")
  guess = input("Guess a number:  ")
  guesses = guesses - 1
  x = 0
  checker(guess, num)
  x = 1
  checker(guess, num)
  x = 2
  checker(guess, num)
  print("-----------------------")

if guess == num:
  print("Good Job! You guessed the number!")
else:
  print("You ran out of chances")