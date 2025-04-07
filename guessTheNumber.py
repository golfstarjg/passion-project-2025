import random

number = random.randint(1,20)
while True:
  numberGuessed = input("Guess a number between 1 and 20!: ")
  numberGuessed = int(numberGuessed)
  if numberGuessed > number:
    print("too high")
  elif numberGuessed < number:
    print("too low")
  elif numberGuessed == number:
    print("correct")
    break
