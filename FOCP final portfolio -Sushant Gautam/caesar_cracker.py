import sys
if len(sys.argv) < 2:
    print("Usage: caesar_cracker.py <encrypted_message_file>")
    sys.exit(1)
filename = sys.argv[1]
try:
    with open(filename, "r") as input_file:
        encrypted_message = input_file.read()
except IOError:
    print("Cannot open '{}'. Sorry about that.".format(filename))
    sys.exit(1)

decryption_found = False

for shift in range(26):
    decrypted_message = ""
    for ch in encrypted_message:
        if ch.isalpha():
            if ch.isupper():
                decrypted_message += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
            else:
                decrypted_message += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        else:
            decrypted_message += ch
            
    if "the" in decrypted_message and "and" in decrypted_message:
        decryption_found = True
        print("Shift {}: {}".format(shift, decrypted_message))
        break

if not decryption_found:
    print("Cannot decrypt. Most likely not a Caesar Cypher at work here.")