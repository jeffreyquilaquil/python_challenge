import random

def random_number():
    return random.randint(1,6)

def display_dice(value):
    # ASCII art representations for a d6
    if value == 1:
        art = ("+-------+", "|       |", "|   o   |", "|       |", "+-------+")
    elif value == 2:
        art = ("+-------+", "| o     |", "|       |", "|     o |", "+-------+")
    elif value == 3:
        art = ("+-------+", "| o     |", "|   o   |", "|     o |", "+-------+")
    elif value == 4:
        art = ("+-------+", "| o   o |", "|       |", "| o   o |", "+-------+")
    elif value == 5:
        art = ("+-------+", "| o   o |", "|   o   |", "| o   o |", "+-------+")
    elif value == 6:
        art = ("+-------+", "| o   o |", "| o   o |", "| o   o |", "+-------+")
    else:
        art = (f"|   {value}   |") # Fallback for different dice sizes

    for line in art:
        print(line)

def dice_simulator():
    command = input("Press any key excep 'Q' to generate a random dice face: ")
    
    while True:
        if command.lower() == 'q':
            print('Thank you!')
            break
        elif command == '':
            result = random_number()
            display_dice(result)
            print("-" * 10)
        else:
            print('hol')

if __name__ == '__main__':
    dice_simulator()
