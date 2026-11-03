AI = {101, 102, 103, 104}
DS = {103, 104, 105, 106}
CS = {104, 106, 107, 108}

print("All students:", AI | DS | CS)
print("Enrolled in all three:", AI & DS & CS)
print("Only AI:", AI - (DS | CS))

exactly_one = ((AI - (DS | CS)) |
               (DS - (AI | CS)) |
               (CS - (AI | DS)))

print("Exactly one course:", exactly_one)
