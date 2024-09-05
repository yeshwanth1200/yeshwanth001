import random

def generate_number():
    """Generate a random 4-digit number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def get_cows_and_bulls(secret, guess):
    """Calculate the number of cows and bulls for the given guess."""
    cows = 0
    bulls = 0
    # Lists to track matched characters
    secret_used = [False] * 4
    guess_used = [False] * 4
    
    # Check for cows (correct digit and correct position)
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
            secret_used[i] = True
            guess_used[i] = True
    
    # Check for bulls (correct digit but incorrect position)
    for i in range(4):
        if not guess_used[i]:
            for j in range(4):
                if not secret_used[j] and guess[i] == secret[j]:
                    bulls += 1
                    secret_used[j] = True
                    break
    
    return cows, bulls

def main():
    print("Welcome to the Cows and Bulls game!")
    
    # Generate the secret number
    secret_number = generate_number()
    
    guess_count = 0
    
    while True:
        # Get user guess
        guess = input("Enter your 4-digit guess: ")
        
        # Validate the input
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        guess_count += 1
        
        # Get cows and bulls
        cows, bulls = get_cows_and_bulls(secret_number, guess)
        
        # Display results
        print(f"Cows: {cows}, Bulls: {bulls}")
        
        # Check if the user guessed the number correctly
        if cows == 4:
            print(f"Congratulations! You've guessed the number {secret_number} correctly.")
            print(f"It took you {guess_count} guesses.")
            break

if __name__ == "__main__":
    main()
