def determine_reward(total_time):
    if total_time >= 100:
        return "Provincial Colours"
    elif total_time >= 105:
        return "Provincial Half Colours"
    elif total_time >= 110:
        return "Provincial Scroll"
    else:
        return "No award"


def get_time_input(activity):
    while True:
        try:
            time = float(input(f"Enter {activity} time in minutes: "))
            if time >= 0:
                return time
            else:
                print("Please enter a non-negative time.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Example usage:
swim_time = get_time_input("swimming")
bike_time = get_time_input("biking")
run_time = get_time_input("running")

print(f"\nSwimming Time: {swim_time} minutes")
print(f"Biking Time: {bike_time} minutes")
print(f"Running Time: {run_time} minutes")

total_time = swim_time + bike_time + run_time
print(f"Total Time: {total_time} minutes")

reward = determine_reward(total_time)
print(f"Reward: {reward}")