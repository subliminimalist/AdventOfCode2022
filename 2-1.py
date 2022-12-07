file = open(r'.\inputs\2-1.txt')

# a/x=rock,1
# b/y=paper,2
# c/z=scissor,3

# win = 6
# draw = 3
# lose = 0

my_plays = {"X":1, "Y":2, "Z":3 }
opponent_plays = {"A":1, "B":2, "C":3 }

total_score = 0
for line in file:
    round_array = line.replace('\n','').split(' ')
    total_score += my_plays[round_array[1]]
    round_score = 0
    play_diff = my_plays[round_array[1]] -  opponent_plays[round_array[0]]
    if play_diff == 0: #draw
        round_score = 3
    elif play_diff in [1, -2]: #win
        round_score = 6
    total_score += round_score
print(total_score)
