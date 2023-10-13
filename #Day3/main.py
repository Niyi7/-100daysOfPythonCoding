# Check if number is Even or Odd
# given_number = int(input("Write out a whole number: "))
# module = given_number % 2
# if module == 0:
#     print(f"{given_number} is an even number")
# else:
#     print(f"{given_number} is an odd number")


# BMI 2.0 - Interpretation of BMI
# user_weight = int(input("How much do you weigh(in kg)?\n"))
# user_height = float(input("How tall are you (in m)?\n"))
# body_mass_index = round(user_weight / user_height**2)
# if body_mass_index < 18.5:
#     print(f"Your Body Mass Index (BMI) is {body_mass_index}, you are underweight")
# elif body_mass_index < 25:
#     print(f"Your Body Mass Index (BMI) is {body_mass_index}, you have a normal weight")
# elif body_mass_index < 30:
#     print(f"Your Body Mass Index (BMI) is {body_mass_index}, you are overweight")
# elif body_mass_index < 35:
#     print(f"Your Body Mass Index (BMI) is {body_mass_index}, you are obese")
# else:
#     print(f"Your Body Mass Index (BMI) is {body_mass_index}, you are clinically obese")


# Leap Year Challenge - Find out if the inputted year is a Leap Year! - My Solution😎
# year = int(input("What year is it? "))
# divisible_by_4 = year % 4
# divisible_by_100 = year % 100
# divisible_by_400 = year % 400
# if divisible_by_4 == 0:
#     year_type = f"{year} is a Leap year"
#     if divisible_by_100 == 0:
#         year_type = f"{year} is not a Leap year"
#         if divisible_by_400 == 0:
#             year_type = f"{year} is a Leap year"
#         elif divisible_by_400 != 0:
#             year_type = f"{year} is not a Leap year"
#     elif divisible_by_100 != 0:
#         year_type = f"{year} is a Leap year"
# else:
#     year_type = f"{year} is a not Leap year"

# print(year_type)


# Leap Year - Angela's Solution
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not Leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")


# Rollercoaster Example - Angela Yu
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("People experiencing mid-life crisis ride for free")
    else:
        bill = 12
        print("Adult tickets are $12.")

    photo = input("Are you taking pictures? Y or N? ")
    if photo == "Y":
        bill += 3
    print(f"Your total bill is: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
