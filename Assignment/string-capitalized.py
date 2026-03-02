# Capitalize all characters in each line

print("Enter lines (press Enter on blank line to stop):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("\n--- Capitalized Output ---")
for line in lines:
    print(line.upper())