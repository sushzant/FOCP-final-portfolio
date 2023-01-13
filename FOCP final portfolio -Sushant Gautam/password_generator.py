import random

LIST_1 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "huckleberry", "lemon", "mango"]
LIST_2 = ["nectarine", "orange", "papaya", "peach", "pear", "plum", "raspberry", "strawberry", "watermelon"]
LIST_3 = ["aardvark", "baboon", "crocodile", "dolphin", "elephant", "flamingo", "gazelle", "hippopotamus", "iguana"]

try: 
  num_passwords = int(input("How many passwords are needed?: "))
  if num_passwords < 1 or num_passwords > 24:
    print("Please enter a value between 1 and 24.")

  else:
    for i in range(num_passwords):
      password = random.choice(LIST_1) + random.choice(LIST_2) + random.choice(LIST_3)
      print(f"{i+1} --> {password}")

except ValueError:
  print("Please enter a number.")
