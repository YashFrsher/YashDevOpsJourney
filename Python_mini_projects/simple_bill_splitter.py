"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

def bill_calculation():
    members = []
    count = 1
    group = int(input("Enter the number of people in your group:\n"))
    while count <= group:
        name = input("Enter your group member names:\n")
        members.append(name)
        count += 1
    bill_amount = int(input("Enter total bill amount:\n"))
    share = round(bill_amount / len(members), 2)
    print(f"Total Bill: {bill_amount}")
    print("Group members are...")
    for person in members:
        print(person)
    print(f"Each Person Share...")
    for people in members:
        print(f"{people} owes {share}")

bill_calculation()