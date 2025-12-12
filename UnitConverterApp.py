"""2. Unit Converter App
Examples: km ↔ miles, °C ↔ °F, kilograms ↔ pounds
Teaches: arithmetic, variables, modular functions
"""

"""
Best Approach:
- Functions for each conversion
- Input() to get the values from the user
- if/else to choose the conversion 
"""

"""
Unit Converter App
Converts between common units: distance, temperature, and weight
"""

# ========== DISTANCE CONVERSIONS ==========
def km_to_miles(km):
    """Convert kilometers to miles"""
    miles = km * 0.621371
    return miles

def miles_to_km(miles):
    """Convert miles to kilometers"""
    km = miles * 1.60934
    return km

# ========== TEMPERATURE CONVERSIONS ==========
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# ========== WEIGHT CONVERSIONS ==========
def kg_to_pounds(kg):
    """Convert kilograms to pounds"""
    pounds = kg * 2.20462
    return pounds

def pounds_to_kg(pounds):
    """Convert pounds to kilograms"""
    kg = pounds * 0.453592
    return kg

# ========== MAIN MENU ==========
def display_menu():
    print("\n" + "="*40)
    print("        UNIT CONVERTER APP")
    print("="*40)
    print("1. Kilometers ↔ Miles")
    print("2. Celsius ↔ Fahrenheit")
    print("3. Kilograms ↔ Pounds")
    print("4. Exit")
    print("="*40)


def distance_converter():
    """Handle distance conversions"""
    print("\n--- Distance Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    
    choice = input("Choose conversion (1 or 2): ")
    
    if choice == "1":
        km = float(input("Enter kilometers: "))
        result = km_to_miles(km)
        print(f"{km} km = {result:.2f} miles")
    elif choice == "2":
        miles = float(input("Enter miles: "))
        result = miles_to_km(miles)
        print(f"{miles} miles = {result:.2f} km")
    else:
        print("Invalid choice!")

def temperature_converter():
    """Handle temperature conversions"""
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Choose conversion (1 or 2): ")
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {result:.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {result:.2f}°C")
    else:
        print("Invalid choice!")


def weight_converter():
    """Handle weight conversions"""
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    
    choice = input("Choose conversion (1 or 2): ")
    
    if choice == "1":
        kg = float(input("Enter weight in kilograms: "))
        result = kg_to_pounds(kg)
        print(f"{kg} kg = {result:.2f} lbs")
    elif choice == "2":
        pounds = float(input("Enter weight in pounds: "))
        result = pounds_to_kg(pounds)
        print(f"{pounds} lbs = {result:.2f} kg")
    else:
        print("Invalid choice!")


# ========== MAIN PROGRAM ==========
def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            distance_converter()
        elif choice == "2":
            temperature_converter()
        elif choice == "3":
            weight_converter()
        elif choice == "4":
            print("\nThank you for using Unit Converter!")
            print("Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice! Please enter 1-4.")
        
        input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()
