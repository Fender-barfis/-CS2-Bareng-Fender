# Travel Fare Calculator
FARE_RATE = 14

# 1. Validate passenger name
while True:
    name = input("Enter passenger name: ")
  
    if name.strip() != "":
        break  # Stops the loop once a valid name is entered.
    else:
        print("Invalid name. Name cannot be empty.")
    
# 2. Validate distance (Number greater than 0)
while True:
    distance_input = input("Enter distance (km): ")
    try:
        distance = float(distance_input)
        if distance > 0:
            break  # Stops the loop once a valid input is entered.
        else:
            print("Invalid distance. Enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Enter a valid number for distance.")


# 3. Validate number of passengers (Positive whole number)
while True:
    passengers = input("Enter number of passengers: ")
    
    if passengers.isdigit() and int(passengers) > 0:
        passengers = int(passengers)
        break  # Stops the loop once a valid input is entered.
    else:
        print("Invalid input. Enter a positive whole number.")
        
#Calculation
total_fare = distance * FARE_RATE * passengers

# Output
print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
