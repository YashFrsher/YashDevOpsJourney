"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""


username = input("Please enter your full name:\n").strip()
profession = input("Please enter your profession:\n").strip()
passion = input("Write a one liner for your passion:\n").strip()
emoji = input("Which emoji best describes you:\n").strip()
website = input("Enter your email or portfolio link:\n").strip()

print("\nChoose your style: ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")

choice = int(input("Enter you style choice: "))
def generator():
    if choice == 1:
        return f"{emoji} {username} | {profession}\n 💡 {passion}\n 🔗 {website}"
    elif choice == 2:
        return f"{emoji} {username}\n {profession}\n 💡 {passion}\n 🔗 {website}"
    elif choice == 3:
        return f"{emoji*3} {username} | {profession}\n 💡 {passion}\n 🔗 {website}"
bio = generator()

print("Do you want to save your output to a file (y/n)")
save = input("Do you want to save your details (y/n): ").lower()

if save == "y":
    print("Saving the details...")
    filename = f"{username.replace(" ", "_")}_bio.txt"
    with open(filename,"w") as file:
        file.write(bio)
print("File Saved to",filename)

