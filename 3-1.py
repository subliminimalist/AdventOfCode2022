file = open(r'.\inputs\3-1.txt')

def get_priority(character):
    char_int = ord(character)
    if(char_int >= 65 and char_int <=90):
        return char_int - 38
    if(char_int >= 97 and char_int <= 122):
        return char_int - 96
total_priority = 0
for line in file:
    sack_size = int(len(line.replace('\n','')) /2)
    sack_1 = line[0:sack_size]
    sack_2 = line[sack_size:len(line.replace('\n',''))]
    for character in sack_1:
        if character in sack_2:
            total_priority += get_priority(character)
            break
print(total_priority)
