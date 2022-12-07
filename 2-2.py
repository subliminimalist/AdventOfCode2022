file = open(r'.\inputs\2-1.txt')

# a/x=rock,1
# b/y=paper,2
# c/z=scissor,3

# Z win = 6
# Y draw = 3
# X lose = 0

opponent_plays = {"A":1, "B":2, "C":3 }
result_score = {"X":0, "Y":3, "Z":6}

total_score = 0
for line in file:
    round_array = line.replace('\n','').split(' ')
    total_score += result_score[round_array[1]]
    opponent_play = int(opponent_plays[round_array[0]])
    round_score = 0
    if round_array[1] == 'Y':
        round_score = opponent_play
    elif round_array[1] == 'Z':
        round_score = opponent_play + 1 
    elif round_array[1] == 'X':
        round_score = opponent_play - 1
    if round_score == 4:
        round_score = 1
    if round_score == 0:
        round_score = 3
    total_score += round_score
print(total_score)