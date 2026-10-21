# Travel Fare Calculator

## Description
This program calculates the total fare based on the distance, fare rate, and passengers with a safety check.

## Version 1 - Original code without input validation 
- Input: Accepts passenger name, distance in kilometers, and the number of passengers with safety checks.
- Process: Validates that the passenger name is not empty using .strip().
Validates that the distance is a valid numeric value greater than 0 using try-except.
Validates that the number of passengers is a positive whole number using .isdigit().
Calculates the total travel fare using the formula: distance * FARE_RATE * passengers.
- Output: Displays the passenger's name and the calculated total fare.
Does not include input validation
- Output: Displays the validated passenger's name and the total calculated fare.
-Error Handling & Re-entry: Utilizes while True loop structures to catch invalid entries and prompt the user for re-entry until valid data is provided.
