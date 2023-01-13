import sys
import random

if len(sys.argv) != 2:
  print("Error: Missing command-line argument.")
  sys.exit(1)

try:
  with open(sys.argv[1], "r") as input_file:
    lines = input_file.readlines()
except FileNotFoundError:
  print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")
  sys.exit(1)

emails = []
for line in lines:
  student_id, name = line.split(None, 1)
  surname, forenames = name.split(",", 1)
  initials = ".".join([f[0] for f in forenames.split()])
  email = f"{initials.lower()}.{surname.lower()}_{random.randint(1000, 9999)}@poppleton.ac.uk"
  email = email.replace("-", "").replace("_", "").replace(" ", "").replace("'", "")
  emails.append((student_id, email))

with open("emails.txt", "w") as output_file:
  for student_id, email in emails:
    output_file.write(f"{student_id} {email}\n")
