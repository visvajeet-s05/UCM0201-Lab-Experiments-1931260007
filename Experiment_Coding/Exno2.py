from itertools import product

equivalent = True
print("P Q | E1 | E2")
for P, Q in product([0, 1], repeat=2):
    E1 = not (P and Q)
    E2 = (not P) or (not Q)
    print(P, Q, "|", int(E1), "|", int(E2))
    equivalent = equivalent and (E1 == E2)

print("\nEquivalent:", equivalent)
