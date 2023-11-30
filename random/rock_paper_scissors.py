rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to Rock Paper Scissors GAME!")
player_choose = input("What do you choose?");
player_pick = ""
computer_pick =""

if player_choose == "Rock":
    print(rock)
    player_pick = "rock"
elif player_choose =="Paper":
    print(paper)
    player_pick = "paper"
else:
    print(scissors)
    player_pick = "scissors"

computer_pick_number = random.randint(1,3)

if computer_pick_number == 1:
    print(rock)
    computer_pick = "rock"
elif computer_pick_number == 2:
    print(paper)
    computer_pick ="paper"
else:
    print(scissors)
    computer_pick = "scissors"

if player_pick == "rock" and computer_pick == "rock":
    print("Y'all tied!")
elif player_pick == "rock" and computer_pick =="paper":
    print("Computer wins!")
elif player_pick =="rock" and computer_pick == "scissors":
    print("Player wins!")

if player_pick == "scissors" and computer_pick == "rock":
    print("Computer wins")
elif player_pick == "scissors" and computer_pick == "scissors":
    print("Y'all tied!")
elif player_pick == "scissors" and computer_pick == "paper":
    print("Player wins!")

if player_pick == "paper" and computer_pick == "rock":
    print("Player wins!")
if player_pick == "paper" and computer_pick == "scissors":
    print("Computer wins!")
if player_pick == "paper" and computer_pick == "paper":
    print("Y'all tied")