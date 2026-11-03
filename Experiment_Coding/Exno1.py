from itertools import product

print("P Q R | Entry Permission")
for P, Q, R in product([0, 1], repeat=3):
    print(P, Q, R, "|", int((P and Q) or R))
