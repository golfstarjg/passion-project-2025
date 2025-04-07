import random
#random.seed()


while True:

  computerChoice = random.randint(1,3)

  choice = input("Rock, Paper Scissors, Shoot! Choose rock, paper or scissors. 1 = rock, 2 = paper, 3 = scissors 4 = done      ")
  choice = int(choice)
  if choice == 1:
    print("You chose rock, lets see what the computer chose")
  elif choice == 2:
    print("You chose paper, lets see what the computer chose")
  elif choice == 3:
    print("You chose scissors, lets see what the computer chose")
  
  if computerChoice == 1:
    print("The Computer's Choice is rock, lets see who wins")
  elif computerChoice == 2:
    print("The Computer's Choice is paper, lets see who wins")
  elif computerChoice == 3:
    print("The Computer's Choice is scissors, lets see who wins")
  
  if computerChoice == choice:
    print("It was a tie")
  elif computerChoice == 1 and choice == 2:
    print("You win") 
  elif computerChoice == 1 and choice == 3:
    print("The Computer wins")
  elif computerChoice == 2 and choice == 1:
    print("The Computer wins")
  elif computerChoice == 2 and choice == 3:
    print("You win")
  elif computerChoice == 3 and choice == 1:
    print("You Win")
  elif computerChoice == 3 and choice == 2:
    print("The Computer wins")
  elif choice == 4:
    break
  