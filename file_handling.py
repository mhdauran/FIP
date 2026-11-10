with open("notes.txt", 'w') as file:
    file.write("i am learning python.\n")
    file.write("today i studied file handling.")

with open("notes.txt", "r") as file:
    content = file.read()
print(content)
