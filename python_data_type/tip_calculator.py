# step one : welcome the user
print("Welcome to the Tip Calculator");

# step two : prompt for the total bill

total_bill = input("What is the total bill? $");

# step three : prompt for tip percentage 10, 12, 15

tip_percentage = input("What is the tip percentage? 10, 12, 15 ");

# step four : prompt for how many people 

total_people = input("How many people? ");


# convert all variables to float

num_total_bill = float(total_bill);
num_tip_percentage = float(tip_percentage)
# 12
num_total_people = float(total_people);


# math steps

total_tip_percentage = num_tip_percentage/100 + 1;

# calculating the bill per person

bill_amount = (num_total_bill/num_total_people) * total_tip_percentage;
