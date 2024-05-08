# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"C:/Users/MONOJYOTI/PycharmProjects/automated-mail/invited_names.txt") as invited_names:
    actual_names = invited_names.readlines()
with open(r"C:\Users\MONOJYOTI\Downloads\Mail Merge Project Start\Input\Letters\starting_letter.txt") as s:
    actual_letter = s.read()
placeholder = "[name]"
for names in actual_names:
    stripped_name = names.strip()
    new_letter = actual_letter.replace(placeholder, stripped_name)
    with open(r"C:\Users\MONOJYOTI\Downloads\Mail Merge Project Start\Output\letter_to_send.txt", mode="a") as s_letter:
        x = s_letter.write(new_letter)
        