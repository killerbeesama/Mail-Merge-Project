with open(r"Input/Names/invited_names.txt") as name_file:
    name_data = name_file.readlines()
    emp_data = []
    for i in name_data:
        x = i.strip('\n')
        emp_data.append(x)

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_data = letter_file.read()
    for i in emp_data:
        x=letter_data.replace("[name]",i)
        with open(f"Output/ReadyToSend/letter_for_{i}.txt",mode='w') as new_file:
            new_file.write(x)