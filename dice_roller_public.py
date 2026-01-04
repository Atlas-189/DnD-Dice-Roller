import random

def get_input():
    global dice_type
    dice_type = input("Enter what type of dice you'd like to roll from the following options:" \
    "\n" \
    "d4 \n" \
    "d6 \n" \
    "d8 \n" \
    "d10 \n" \
    "d12 \n" \
    "d20 \n" \
    "d100 \n" \
    "Dice type: "
    )
    dice_amount()
    roll_results(dice_type, dice_times)

def dice_amount():
    global dice_times
    dice_times = int(input("How many dice would you like to roll? \n" \
    "Amount: "))
    return dice_times

# d4
def roll_d4():
    d4 = random.randint(0, 4)
    return d4
# d6
def roll_d6():
    d6 = random.randint(0, 6)
    return d6
# d8
def roll_d8():
    d8 = random.randint(0, 8)
    return d8
# d10
def roll_d10():
    d10 = random.randint(0, 10)
    return d10
# d12
def roll_d12():
    d12 = random.randint(0, 12)
    return d12
# d20
def roll_d20():
    d20 = random.randint(0, 20)
    return d20
# d100
def roll_d100():
    d100 = random.randint(0, 100)
    return d100

def roll_results(dice_type, dice_times):
    for i in range(dice_times):
        if dice_type == "d4":
            print(f"Dice {i + 1}: {roll_d4()}")
        elif dice_type == "d6":
            print(f"Dice {i + 1}: {roll_d6()}")
        elif dice_type == "d8":
            print(f"Dice {i + 1}: {roll_d8()}")
        elif dice_type == "d10":
            print(f"Dice {i + 1}: {roll_d10()}")
        elif dice_type == "d12":
            print(f"Dice {i + 1}: {roll_d12()}")
        elif dice_type == "d20":
            print(f"Dice {i + 1}: {roll_d20()}")
        elif dice_type == "d100":
            print(f"Dice {i + 1}: {roll_d100()}")
    repeat_roll()

def repeat_roll():
    repeat = str(input("Would you like to roll again? (yes/no): "))
    if repeat == "yes":
        get_input()
    if repeat == "no":
        print("End")

if __name__ == "__main__":
    get_input()
