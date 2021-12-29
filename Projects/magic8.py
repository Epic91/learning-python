import random

# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

# Assigned Variables
name = "Joe"
question = "Will I win the loterry?"
answer = ""
random_number = random.randint(1, 9)

# Conditional
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
    answer = "Yes - definitely."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else:
  answer = "Error"

# Conditional if name is empty
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

# Conditiona if question is empty
if question == "":
  print("You must first ask a question!")
else:
  print("Magic 8-ball's answer: " + answer)