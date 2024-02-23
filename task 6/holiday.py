# User inputs
city_flights = input("Where will you be flying to: (Vegas, Paris, London, Cancun): ").capitalize()
num_nights = int(input("How many nights will you be staying: "))
rental_days = int(input("How many days will you hire a car: "))

def plane_cost(city_flights): 
    if city_flights == "Vegas":
        return 500
    elif city_flights == "Paris":
        return 250
    elif city_flights == "London":
        return 120
    elif city_flights == "Cancun":
        return 700
    else:
        return 0 

def hotel_cost(num_nights):
    return num_nights * 85

def car_rental(rental_days):
    return rental_days * 30

def holiday_cost(flight, hotel, rental):
    return flight + hotel + rental

# Calculate Costs
flight = plane_cost(city_flights)
hotel = hotel_cost(num_nights)
rental = car_rental(rental_days)
total_cost = holiday_cost(flight, hotel, rental)

# Results
print(f"Flight Cost to {city_flights}: ${flight}")
print(f"Hotel Cost: ${hotel}")
print(f"Car Rental Cost: ${rental}")
print(f"The Total Cost of Your Holiday: ${total_cost}")

