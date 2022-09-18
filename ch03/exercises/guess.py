import random

result = range(1,11)

result = int(random.choice(result))
print(result)

for i in [result]*3:
  guess = input("Your guess?")
  guess = int(guess)
  if guess < i:
      print("Too low")
  if guess > i: 
      print("Too high")
  if guess == i: 
      print("Correct!")
      break

  #for i in [guess]:
    #if guess < result:
     # print("Too low")
    #if guess > result: 
     # print("Too high")
    #if guess == result: 
    #  print("Correct!")
      
    
      