"""
Dice Roller & Number Guessing Games
Teaches: Random module, Loops, Game Logic, Conditionals
"""

import random  # Module for generating random numbers
import time    # Module for adding delays


# ========== DICE ROLLER GAME ==========
def roll_single_die():
    """Roll one die (1-6)"""
    return random.randint(1, 6)


def roll_multiple_dice(num_dice):
    """Roll multiple dice and return results"""
    rolls = []
    
    for i in range(num_dice):
        roll = roll_single_die()
        rolls.append(roll)
    
    return rolls


def display_dice(number):
    """Display dice as ASCII art"""
    dice_art = {
        1: [
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"
        ],
        2: [
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"
        ],
        3: [
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"
        ],
        4: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"
        ],
        5: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"
        ],
        6: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"
        ]
    }
    
    return dice_art[number]


def dice_roller_game():
    """Main dice roller game"""
    print("\n" + "="*50)
    print("           🎲 DICE ROLLER GAME 🎲")
    print("="*50)
    
    while True:
        print("\n--- Roll Dice ---")
        
        # Get number of dice from user
        try:
            num_dice = int(input("How many dice do you want to roll? (1-10): "))
            
            if num_dice < 1 or num_dice > 10:
                print("❌ Please enter a number between 1 and 10!")
                continue
        
        except ValueError:
            print("❌ Please enter a valid number!")
            continue
        
        # Roll the dice
        print("\n🎲 Rolling", num_dice, "dice...")
        time.sleep(1)  # Dramatic pause
        
        rolls = roll_multiple_dice(num_dice)
        
        # Display results
        print("\n" + "─"*50)
        print("RESULTS:")
        print("─"*50)
        
        # Show ASCII art for each die
        if num_dice <= 3:  # Show fancy art for 1-3 dice
            for i, roll in enumerate(rolls, start=1):
                print(f"\nDie #{i}:")
                dice_lines = display_dice(roll)
                for line in dice_lines:
                    print(line)
        else:  # Show simple format for many dice
            for i, roll in enumerate(rolls, start=1):
                print(f"Die #{i}: {roll}")
        
        # Calculate and show total
        total = sum(rolls)  # sum() adds all numbers in list
        print("\n" + "─"*50)
        print(f"🎯 TOTAL: {total}")
        print(f"📊 Average: {total / num_dice:.2f}")
        print("─"*50)
        
        # Special messages
        if all(roll == 6 for roll in rolls):
            print("🎉 WOW! ALL SIXES! You're incredibly lucky!")
        elif all(roll == 1 for roll in rolls):
            print("😅 Oh no! All ones... Better luck next time!")
        elif len(set(rolls)) == 1:  # All same number
            print(f"🌟 Amazing! All dice show {rolls[0]}!")
        
        # Ask to play again
        play_again = input("\nRoll again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing Dice Roller!")
            break


# ========== NUMBER GUESSING GAME ==========
def get_difficulty():
    """Let user choose difficulty level"""
    print("\n--- Choose Difficulty ---")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    print("4. Expert (1-500, 7 attempts)")
    
    while True:
        choice = input("\nSelect difficulty (1-4): ")
        
        if choice == '1':
            return 50, 10, "Easy"
        elif choice == '2':
            return 100, 7, "Medium"
        elif choice == '3':
            return 200, 5, "Hard"
        elif choice == '4':
            return 500, 7, "Expert"
        else:
            print("❌ Please choose 1-4!")


def give_hint(secret, guess, attempt, max_attempts):
    """Provide helpful hints"""
    difference = abs(secret - guess)
    
    if difference <= 5:
        print("🔥 VERY HOT! You're super close!")
    elif difference <= 10:
        print("🌡️  Hot! Getting closer!")
    elif difference <= 20:
        print("😊 Warm! You're in the right area!")
    elif difference <= 50:
        print("❄️  Cold! Not very close...")
    else:
        print("🧊 Freezing! Far away!")
    
    # Additional hints
    if attempt >= max_attempts - 2:
        # Give extra help near the end
        if secret % 2 == 0:
            print("💡 Hint: The number is EVEN")
        else:
            print("💡 Hint: The number is ODD")


def number_guessing_game():
    """Main number guessing game"""
    print("\n" + "="*50)
    print("        🎯 NUMBER GUESSING GAME 🎯")
    print("="*50)
    print("\nI'm thinking of a number. Can you guess it?")
    
    # Game statistics
    games_played = 0
    games_won = 0
    
    while True:
        # Get difficulty
        max_num, max_attempts, difficulty = get_difficulty()
        
        # Generate secret number
        secret_number = random.randint(1, max_num)
        
        print(f"\n🎮 Starting {difficulty} Mode!")
        print(f"I'm thinking of a number between 1 and {max_num}")
        print(f"You have {max_attempts} attempts. Good luck!\n")
        
        # Track guesses
        attempts = 0
        guessed_numbers = []
        won = False
        
        # Main game loop
        while attempts < max_attempts:
            attempts += 1
            
            print(f"\n--- Attempt {attempts}/{max_attempts} ---")
            
            # Show previous guesses
            if guessed_numbers:
                print(f"Previous guesses: {sorted(guessed_numbers)}")
            
            # Get guess from user
            try:
                guess = int(input("Enter your guess: "))
                
                if guess < 1 or guess > max_num:
                    print(f"❌ Please guess between 1 and {max_num}!")
                    attempts -= 1  # Don't count this attempt
                    continue
                
                if guess in guessed_numbers:
                    print("⚠️  You already guessed that number!")
                    attempts -= 1  # Don't count this attempt
                    continue
                
                guessed_numbers.append(guess)
            
            except ValueError:
                print("❌ Please enter a valid number!")
                attempts -= 1  # Don't count this attempt
                continue
            
            # Check the guess
            if guess == secret_number:
                # WON!
                print("\n" + "🎉"*20)
                print(f"🏆 CONGRATULATIONS! You guessed it! 🏆")
                print(f"The number was {secret_number}!")
                print(f"You won in {attempts} attempt(s)!")
                print("🎉"*20)
                won = True
                games_won += 1
                break
            
            elif guess < secret_number:
                print(f"📈 Too low! The number is HIGHER than {guess}")
                give_hint(secret_number, guess, attempts, max_attempts)
            
            else:  # guess > secret_number
                print(f"📉 Too high! The number is LOWER than {guess}")
                give_hint(secret_number, guess, attempts, max_attempts)
            
            # Show remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"\n💪 You have {remaining} attempt(s) left!")
        
        # Game over
        if not won:
            print("\n" + "💔"*20)
            print(f"😢 Game Over! You ran out of attempts!")
            print(f"The number was: {secret_number}")
            print("💔"*20)
        
        # Update statistics
        games_played += 1
        
        # Show statistics
        print(f"\n📊 Your Statistics:")
        print(f"   Games Played: {games_played}")
        print(f"   Games Won: {games_won}")
        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print(f"   Win Rate: {win_rate:.1f}%")
        
        # Play again?
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing Number Guessing Game!")
            break


# ========== MAIN MENU ==========
def display_main_menu():
    """Display game selection menu"""
    print("\n" + "="*50)
    print("          🎮 GAME ARCADE 🎮")
    print("="*50)
    print("1. 🎲 Dice Roller")
    print("2. 🎯 Number Guessing Game")
    print("3. 🚪 Exit")
    print("="*50)


def main():
    """Main program"""
    print("\n" + "🎮"*25)
    print("     WELCOME TO THE GAME ARCADE!")
    print("🎮"*25)
    
    while True:
        display_main_menu()
        choice = input("\nChoose a game (1-3): ").strip()
        
        if choice == '1':
            dice_roller_game()
        
        elif choice == '2':
            number_guessing_game()
        
        elif choice == '3':
            print("\n" + "🌟"*25)
            print("   Thanks for playing! Come back soon!")
            print("🌟"*25 + "\n")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-3.")
        
        input("\nPress Enter to return to main menu...")


# Run the program
if __name__ == "__main__":
    main()