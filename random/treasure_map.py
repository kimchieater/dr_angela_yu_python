line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜","⬜️️"]

map = [line1, line2, line3]

# 2 1
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

first_position = ""
second_position = ""

if position[0] == "A":
  first_position += "0"
elif position[0] =="B":
  first_position += "1"
elif position[0] =="C":
  first_position += "2"

if position[1] == "1":
  second_position += "0"
elif position[1] == "2":
  second_position += "1"
elif position[1] == "3":
  second_position += "2"

first_position = int(first_position)
second_position = int(second_position)


map[second_position][first_position] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

