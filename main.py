# main.py

# 1. Importing Standard/Library Modules (built into Python)
import math
import datetime

# 2. Importing the User-Defined Module (created by you)
import my_math_module

def main():
    # --- Using Standard Library Modules ---
    print("--- STANDARD MODULES ---")
    
    # Using the 'datetime' module to get the current date
    today = datetime.date.today()
    print(f"Today's date is: {today}")
    
    # Using the 'math' module to calculate a square root and use Pi
    number = 25
    print(f"The square root of {number} is: {math.sqrt(number)}")
    print(f"The value of Pi is approximately: {math.pi:.4f}")


    # --- Using User-Defined Module ---
    print("\n--- USER-DEFINED MODULE ---")
    
    side = 4
    # Using the functions we defined in my_math_module.py
    area = my_math_module.calculate_square_area(side)
    volume = my_math_module.calculate_cube_volume(side)
    
    print(f"For a shape with side length {side}:")
    print(f"Area of the square: {area}")
    print(f"Volume of the cube: {volume}")

if __name__ == "__main__":
    main()