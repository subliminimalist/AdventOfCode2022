file = open(r'.\inputs\3-1.txt')

def get_priority(character):
    char_int = ord(character)
    if(char_int >= 65 and char_int <=90):
        return char_int - 38
    if(char_int >= 97 and char_int <= 122):
        return char_int - 96

def find_common_item(elf_group):
    for item in elf_group[0]:
        if item in elf_group[1] and item in elf_group[2]:
            return item
    return None

total_priority = 0
elf_group = []

for line in file:
    elf_group.append(line.replace('\n', ''))
    if len(elf_group) == 3:
        total_priority += get_priority(find_common_item(elf_group))
        elf_group = []

print(total_priority)
