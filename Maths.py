def collatz_sequence():
    try:
        n = int(input("Enter a positive number: "))
        steps = 0
        
        # Jab tak n 1 nahi ho jata, loop chalega
        while n > 1:
            if n % 2 == 0:
                n = n // 2  # integer division
            else:
                n = (n * 3) + 1
            
            steps += 1
            print(f"Step {steps}: {n}")
            
        print(f"\nFinished! Total steps to reach 1: {steps}")
        
    except ValueError:
        print("Please enter a valid integer!")


def two_sum_numbers(numbers,targets):
    left = 0
    right = len(numbers)-1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == targets:
            return numbers[left],numbers[right]

        elif current_sum < targets:
            left +=1
        else:
            right -=1
            return "couldn't find the pair"
my_list = [2,7,11,15,18,21]
target_number = 26
result = two_sum_numbers(my_list,target_number)
print("Target numbers:", target_number)
print("Pair found:", result)
import math

print("=== Triangle Calculator (Sine & Cosine Rules) ===")

while True:
    print("\n" + "="*40)
    choice = input("Kaunsa rule lagana hai? ('sine', 'cosine', ya 'exit' to quit): ").strip().lower()
    
    if choice == 'exit':
        print("\nProgram exited. Keep grinding! ⚔️")
        break
        
    if choice not in ['sine', 'cosine']:
        print("Invalid choice! Please type 'sine', 'cosine', or 'exit'.")
        continue

    # Teeno sides user se dynamically input karwana inside the loop
    sides = {}
    try:
sides['a'] = float(input("Give the first side (a): "))
        sides['b'] = float(input("Give the second side (b): "))
        sides['c'] = float(input("Give the third side (c): "))
    except ValueError:
        print("❌ Invalid number entered! Please enter valid numeric values.")
        continue

    print(f"\n[Saved Sides] -> a: {sides['a']}, b: {sides['b']}, c: {sides['c']}")

    if choice == 'sine':
        print("\n--- Sine Rule Calculation ---")
        try:
            angle_A_deg = float(input("Enter angle A (in degrees, opposite to side a): "))
            angle_B_deg = float(input("Enter angle B (in degrees, opposite to side b): "))
            
            angle_A_rad = math.radians(angle_A_deg)
            angle_B_rad = math.radians(angle_B_deg)
            
            calculated_side = (sides['b'] * math.sin(angle_A_rad)) / math.sin(angle_B_rad)
            print(f"👉 Calculated Side using Sine Rule: {calculated_side:.2f}")
        except ValueError:
            print("❌ Invalid angle entered!")
sides['a'] = float(input("Give the first side (a): "))
        sides['b'] = float(input("Give the second side (b): "))
        sides['c'] = float(input("Give the third side (c): "))
    except ValueError:
        print("❌ Invalid number entered! Please enter valid numeric values.")
        continue

    print(f"\n[Saved Sides] -> a: {sides['a']}, b: {sides['b']}, c: {sides['c']}")

    if choice == 'sine':
        print("\n--- Sine Rule Calculation ---")
        try:
            angle_A_deg = float(input("Enter angle A (in degrees, opposite to side a): "))
            angle_B_deg = float(input("Enter angle B (in degrees, opposite to side b): "))
            
            angle_A_rad = math.radians(angle_A_deg)
            angle_B_rad = math.radians(angle_B_deg)
            
            calculated_side = (sides['b'] * math.sin(angle_A_rad)) / math.sin(angle_B_rad)
            print(f"👉 Calculated Side using Sine Rule: {calculated_side:.2f}")
        except ValueError:
            print("❌ Invalid angle entered!")


collatz_sequence()
        
