import random
low=0
high=10
find_in=1
dificulty= input("Enter the difficulty mode (E-easy,M-medium,H-hard,I-impossible): ").upper()
while True:
    if dificulty=="E":
      high=10
      choose=int(input("Choose no. b/w 0 to 10: "))
      break
    elif dificulty=="M":
      high=100
      choose=int(input("Choose no. b/w 0 to 100: "))
      break
    elif dificulty=="H":
     high=1000
     choose=int(input("Choose no. b/w 0 to 1000: "))
     break
    elif dificulty=="I":
      high=100000
      choose=int(input("Choose no. b/w 0 to 100000: "))
      break
    else:
     print("Invalid entry")
     dificulty= input("Enter the difficulty mode (E-easy,M-medium,H-hard,I-impossible): ").upper()
random_no= random.randint(low,high)

while True:
  if choose==random_no:
      print("-------Congratulation--------")
      print()
      print("-------You Won--------")
      break
  elif choose<random_no:
     print("Guess Higher")
     find_in+=1
     choose=int(input("Choose no. : "))
  else:
      print("Guess Lower")
      find_in+=1
      choose=int(input("Choose no. : "))
    
    
print()
print(f"You took {find_in} Guesses...")

