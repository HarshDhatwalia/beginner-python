import random
options=("Rock","Paper","Sesiors")
player= None
round_no=1
pick=5
score_computer=0
score_player=0
while round_no<=pick:
    print(f"Round no. {round_no}")
    print("-----------")
    player= input("Pick (Rock , Paper, Sesiors): ").strip().capitalize()
    while player not in options:
        print("Invalid Entry")
        player= input("Pick (Rock , Paper, Sesiors): ").strip().capitalize()
    computer= random.choice(options)
    print(f"You picked: {player:20}")
    print(f"Computer picked: {computer:20}")
    if player == computer:
        print("It's a tie! Replay this round.")
        continue  # Do not count this round
    elif(player=="Rock" and computer=="Sesiors") or (player=="Paper"and computer=="Rock")or(player=="Sesiors"and computer=="Paper"):
         print("You win this round!")
         score_player += 1
    else:
         print("Computer wins this round!")
         score_computer += 1
    print(f"Score → You: {score_player} | Computer: {score_computer}")
    print("------")
    
    round_no += 1 
print("\nFinal Result:")
if score_player > score_computer:
    print("🎉 You won the game!")
elif score_player < score_computer:
    print("😢 Computer won the game!")
else:
    print("🤝 It's a draw!")
    



