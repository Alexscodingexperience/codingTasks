target_number = -1 

total_sum = 0
count = 0

while True:
    try:
        user_input = int(input("Enter the number -1: "))
        
        if user_input == target_number:
            print("Congratulations.")
            break  # Exit the loop if the correct number is guessed
        else:
            total_sum += user_input
            count += 1
            print("Try again. Incorrect.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Calculate average excluding the correct answer
if count > 0:
    average = total_sum / count
    print(f"\nAverage of incorrect answers: {average:.2f}")