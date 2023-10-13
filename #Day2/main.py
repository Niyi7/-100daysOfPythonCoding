# # Adding Two Digit Numbers
# two_digit_number = input("Type a two digit number: ")
# add_numbers = int(two_digit_number[0]) + int(two_digit_number[1])
# print(add_numbers)

# # BMI Calculator
# user_weight = int(input("How much do you weigh(in kg)?\n"))
# user_height = float(input("How tall are you (in m)?\n"))
# body_mass_index = round(user_weight / user_height**2)
# print(f"Your Body Mass Index (BMI) is {body_mass_index}")

# Life in Weeks
# current_age = int(input("What is your current age?\n"))
# years_left = int(90 - current_age)
# print(f"You have {years_left} years left")
# print(
#     f"This implies that you have {years_left * 365 } days, {years_left * 52} weeks, and {years_left * 12} months left"
# )

# Tip Calculator
print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))

given_tip = True
while given_tip:
    percentage_tip = int(
        input("What percentage tip would you like to give? 10, 12, or 15? ")
    )
    if percentage_tip == 10:
        total_bill_plus_tip = total_bill * 1.10
    elif percentage_tip == 12:
        total_bill_plus_tip = total_bill * 1.12
    elif percentage_tip == 15:
        total_bill_plus_tip = total_bill * 1.15
    else:
        input("Please input a valid tip percentage: ")
    given_tip = False
num_of_people = int(input("How many people will slipt the bill? "))
amount_individual_pays = round(total_bill_plus_tip / num_of_people, 2)
print(f"Each person will pay ${amount_individual_pays}")
