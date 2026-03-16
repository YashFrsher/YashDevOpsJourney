"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""

from datetime import date
from datetime import datetime

def journal():
    learned = input("Please enter the description what you have learned:\n")
    productivity = int(input("Enter how productive your are out of 5:\n"))
    current_date = date.today()
    current_time = datetime.now()
    filename = f"learning_Journal.txt"
    with open(filename, "a") as file:
        file.write(f"📅 {current_date} - {current_time}\n {learned}\n Productivity Rating: {productivity}/5" + '\n')
    print(f"Journal has been updated.")

while True:
    journal()
    again = input("Do you want to update the file again (y/n):\n")
    if again == "n":
        print("Good Bye!!!!")
        break
        
        