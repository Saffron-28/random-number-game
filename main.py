#create random number guessing game

import random 

num = 0
player_guess = int(input("please guess a number?"))

def random_number_generator():
  num = random.randint(0,20)
  return num

# print(random_number_generator())

def difference_from_answer(num,player_guess):
  
  if player_guess < num:
    return ('tooo low')
  elif player_guess > num:
    return ('tooo high')
  else:
    return ('match whooo')

print(difference_from_answer(num,player_guess))
