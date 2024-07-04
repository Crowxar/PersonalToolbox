import pyperclip

brief_info = []

while True:
    brief = input("Brief time: ")
    if brief == "":
        break
    else:
        names = []
        takeoff = input("Takeoff time: ")
        land = input("Land time: ")
        while True:
            name = input("Name: ")
            if name == "":
                break
            names.append(name)
        brief_info.append((brief, takeoff, land, names))

# Printing all the collected information at once
output_text = ""
for i, (brief, takeoff, land, names) in enumerate(brief_info):
    output_text += f"{len(names)}x {brief}, {takeoff}, {land} - {', '.join(names)}"
    if i != len(brief_info) - 1:
        output_text += "\n"

print(output_text)

# Copying the printed list to the clipboard
pyperclip.copy(output_text)
print("The list has been copied to the clipboard.")
