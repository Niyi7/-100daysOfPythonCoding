

print("Welcome to the Love Calculator")
your_name = input("What is your name? \n").lower()
their_name = input("What is their name? \n").lower()

our_names = your_name + their_name

value_for_true = str(
    (
        int(our_names.count("t"))
        + int(our_names.count("r"))
        + int(our_names.count("u"))
        + int(our_names.count("e"))
    )
)
value_for_love = str(
    (
        int(our_names.count("l"))
        + int(our_names.count("o"))
        + int(our_names.count("v"))
        + int(our_names.count("e"))
    )
)
total_value = int(value_for_true + value_for_love)

if total_value < 10 or total_value > 90:
    print(f"Your score is {total_value}, you go together like coke and mentos")
elif total_value > 40 and total_value < 50:
    print(f"Your score is {total_value}, you are alright together")
else:
    print(f"Your score is {total_value}")
