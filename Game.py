import random

Random_Number = random.randint(1, 100)
guess = -1
Number = 0

while Number != Random_Number:
    Number = int(input("Enter the number: "))
    guess += 1
    if Number < Random_Number:
        print("Enter a higher number.")
    elif Number > Random_Number:
        print("Enter a lower number.")
    else:
        print(f"You guessed the right number {Number} in {guess} guesses!")

count = 0
try: 
    with open("Game_count.txt", "r") as f:
        file_content = f.read().strip()
        if file_content:
            count = int(file_content)
except (FileNotFoundError, ValueError):
    pass

count += 1

with open("Game_count.txt", "w") as f:
    f.write(str(count))

print(f"Your wins: {count}")
