"""
3. Password Strength Checker
Check length, uppercase, digits, special characters
Teaches: strings, loops, regex (optional)
"""

import re  # Regular expressions 

# ========== METHOD 1: USING LOOPS ==========
def check_length(password):
    """Check if password meets minimum length requirement"""
    min_length = 8
    if len(password) >= min_length:
        return True, f"✓ Length: {len(password)} characters (Good!)"
    else:
        return False, f"✗ Length: {len(password)} characters (Need at least {min_length})"


def check_uppercase(password):
    """Check if password contains uppercase letters"""
    has_upper = False              # Start by assuming no uppercase 
    for char in password:          # Loop through each character
        if char.isupper():         # Check if character is uppercase
            has_upper = True       # Found one! Set to True
            break                  # Exit loop immediately (no need to check more)

    if has_upper:
        return True, "✓ Contains uppercase letters"
    else:
        return False, "✗ Missing uppercase letters (A-Z)"


def check_digits(password):
    """Check if password contains numbers"""
    has_digit = False                 # Start by assuming no digits
    for char in password:             # Loop through each character in password
        if char.isdigit():            # Check if it is a digit
            has_digit = True          # Found One! Set function to True
            break                     # Stop! No need to look for more digits
    
    if has_digit:
        return True, "✓ Contains numbers"
    else:
        return False, "✗ Missing numbers (0-9)"


def check_special_chars(password):
    """Check if password contains special characters"""
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"        # Define what's special
    has_special = False                      # Start by assuming no special character
    
    for char in password:                    # Loop through each character in the password  
        if char in special_characters:       # Check if a chac=racter exist in the special string
            has_special = True               # Found One! 
            break                            # Stop! No need to look for more special characters
    
    if has_special:
        return True, "✓ Contains special characters"
    else:
        return False, "✗ Missing special characters (!@#$%^&* etc.)"


# ========== METHOD 2: USING REGEX (ADVANCED) ==========
def check_password_regex(password):
    """Alternative method using regular expressions instead of loops"""
    checks = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),     # Search for uppercase letter in the string
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digits": bool(re.search(r'\d', password)),            # Search if there exist any digit in the string
        "special": bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?/~`]', password))
    }
    return checks


# ========== STRENGTH CALCULATION ==========
def calculate_strength(password):
    """Calculate overall password strength"""
    score = 0         # Holds the total score
    feedback = []       # Empty list to store feedback
    
    # Each function returns two variables (Boolean (True/False), and the message string)
    """
    E.g.: If password is "Pass@123"
        length_ok, length_msg = check_length("Pass@123")
        length_ok = True
        length_msg = ✓ Length: 8 characters (Good!) 
    """

    # Run all checks
    length_ok, length_msg = check_length(password)
    upper_ok, upper_msg = check_uppercase(password)
    digit_ok, digit_msg = check_digits(password)
    special_ok, special_msg = check_special_chars(password)
    
    # Add to feedback list
    feedback.append(length_msg)
    feedback.append(upper_msg)
    feedback.append(digit_msg)
    feedback.append(special_msg)
  
    # Calculate score
    if length_ok:
        score += 20
    if upper_ok:
        score += 25
    if digit_ok:
        score += 30
    if special_ok:
        score += 25
    
    return score, feedback


def get_strength_rating(score):
    """Convert score to strength rating"""
    if score >= 90:
        return "💪 VERY STRONG", "green"
    elif score >= 70:
        return "✓ STRONG", "green"
    elif score >= 50:
        return "⚠ MODERATE", "yellow"
    elif score >= 30:
        return "⚠ WEAK", "orange"
    else:
        return "✗ VERY WEAK", "red"


# ========== DISPLAY FUNCTIONS ==========
def display_results(password, score, feedback, rating):
    """Display the analysis results"""
    print("       PASSWORD STRENGTH ANALYSIS")
    print("="*50)
    print(f"\nPassword: {'*' * len(password)} ({len(password)} characters)")
    print(f"\nScore: {score}/100")
    print(f"Rating: {rating[0]}")
    print("DETAILED FEEDBACK:")
    print("-"*50)
    
    for item in feedback:      # Loop through the feedback List
        print(item)            # Print each message


def generate_suggestions(score):
    """Provide suggestions for improvement"""
    if score < 90:        # Only show suggestions if not perfect
        print("\n💡 SUGGESTIONS FOR IMPROVEMENT:")
        print("-"*50)
        if score < 50:    # Extra suggestions for weak passwords
            print("• Use at least 12 characters")
            print("• Mix uppercase and lowercase letters")
            print("• Add numbers and special characters")
        print()


# ========== MAIN PROGRAM ==========
def main():
    """Main program"""
    print("      PASSWORD STRENGTH CHECKER")
    print("="*50)
    print("\nThis tool evaluates your password security.")
    print("Note: Your password is NOT stored or transmitted.")
    
    while True:
        print("\n" + "-"*50)
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("\n👋 Thank you for using Password Checker!")
            break
        
        # Calculate strength
        score, feedback = calculate_strength(password)
        rating = get_strength_rating(score)
        
        # Display results
        display_results(password, score, feedback, rating)
        generate_suggestions(score)
        
        # Optional: Show regex method
        show_regex = input("Show regex analysis? (y/n): ").lower()
        if show_regex == 'y':
            regex_results = check_password_regex(password)
            print("\n📊 REGEX METHOD RESULTS:")
            print("-"*50)
            for check, result in regex_results.items():
                status = "✓" if result else "✗"
                print(f"{status} {check}: {result}")
            print()

# Run the program
if __name__ == "__main__":
    main()