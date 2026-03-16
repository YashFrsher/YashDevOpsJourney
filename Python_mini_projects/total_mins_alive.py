"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""
from datetime import datetime
def calc_min_alive():
    age_years = float(input("Enter your age in years:\n"))
    now = datetime.now()
    current_year = now.year
    age = current_year - age_years
    if current_year % 4 == 0 and current_year % 400 == 0:
        age_in_days = age * 365.25
        age_hours = age_in_days * 24
        age_in_min = age_hours * 60
        return f"You are approximately\n - {age_in_days} days old\n - {age_hours} hours old\n - {age_in_min} minutes old"
    else:
        age_in_days = age * 365
        age_hours = age_in_days * 24
        age_in_min = age_hours * 60
        return f"You are approximately\n - {age_in_days} days old\n - {age_hours} hours old\n - {age_in_min} minutes old"
while True:
    output = calc_min_alive()
    print(output)
    again = input("Do you want to check again(y/n)").lower().strip()
    if again!= 'y':
        print("Good Bye!!!")
        break
    