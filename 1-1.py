

file = open(r'.\inputs\1-1.txt')

current_elf_cals = 0
elf_cals = []
for line in file:
    if line != '\n':
        current_elf_cals = current_elf_cals + int(line)
    else:
        elf_cals.append(current_elf_cals)
        current_elf_cals = 0
elf_cals.sort(reverse=True)
i = 0
top_three_total = 0
while i < 3:
    top_three_total += elf_cals[i]
    i += 1
print(top_three_total)