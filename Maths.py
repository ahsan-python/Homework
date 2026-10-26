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




collatz_sequence()
        
