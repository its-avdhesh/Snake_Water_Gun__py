import random

# Generate a random number
Random_Number = random.randint(1, 100)
guess = -1
Number = 0

# Loop for guessing the number
while Number != Random_Number:
    Number = int(input("Enter the number: "))
    guess += 1  # Increment guess count
    if Number < Random_Number:
        print("Enter a higher number.")
    elif Number > Random_Number:
        print("Enter a lower number.")
    else:
        print(f"You guessed the right number {Number} in {guess} guesses!")

# Initial count setup for storing the number of wins
count = 0
try:
    # Try to read previous count from file
    with open("Game_count.txt", "r") as f:
        file_content = f.read().strip()
        if file_content:  # Only convert if content is not empty
            count = int(file_content)
except (FileNotFoundError, ValueError):
    # File does not exist or content is not an integer, so start from 0
    pass

# Update count after win
count += 1

# Write only the count to the file for the next run
with open("Game_count.txt", "w") as f:
    f.write(str(count))

# Display the win count with a formatted string
print(f"Your wins: {count}")
