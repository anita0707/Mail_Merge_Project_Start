
with open("input/names/invited_names.txt","r") as names:
    text = names.readlines()

with open("input/letters/starting_letter.txt", "r") as message:
    full_message = message.read()

for position in text:
    # removing space from the names in the list
    stripped_name = position.strip()
    x = full_message.replace("[name]",stripped_name)
    #  creating individual invites
    with open(f"output/readytosend/curated_emails_for_{stripped_name}.txt","w") as final:
        final.write(x)
