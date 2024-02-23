# Open the file for reading
with open("DOB.txt", "r") as file:
    # Read lines from the file
    lines = file.readlines()

# Separate names and birthdates
names = []
birthdates = []

for line in lines:
    # Split the line into words
    words = line.strip().split()

    # Ensure there are at least two words
    if len(words) >= 2:
        # Join the first two words as the name
        name = " ".join(words[:2])
        # Join the remaining words as the birthdate
        birthdate = " ".join(words[2:])
        
        names.append(name)
        birthdates.append(birthdate)

# Print all names
print("Names:")
for name in names:
    print(name)

# Print all dates of birth
print("\nDates of Birth:")
for birthdate in birthdates:
    print(birthdate)