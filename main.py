#create random number guessing game

import random 

num = 0

def random_number_generator():
  num = random.randint(0,20)
  return num
  

print(random_number_generator())
  