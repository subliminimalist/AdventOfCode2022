file = open(r'.\inputs\4-1.txt')

def is_total_overlap(assignment_1, assignment_2):
    if int(assignment_1.split('-')[0]) >= int(assignment_2.split('-')[0]) and int(assignment_1.split('-')[1]) <= int(assignment_2.split('-')[1]):
        return True
    else:
        return False

overlap_count = 0

for line in file:
    assignments = line.replace('\n','').split(',')
    if is_total_overlap(assignments[0], assignments[1]) or is_total_overlap(assignments[1], assignments[0]):
        overlap_count += 1

print(overlap_count)