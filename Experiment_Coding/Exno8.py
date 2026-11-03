
students = {1, 2, 3, 4, 5, 6}
year = {1:1, 2:1, 3:2, 4:2, 5:3, 6:3}
R = {(a,b) for a in students for b in students if year[a] == year[b]}
ref = all((a,a) in R for a in students)
sym = all((b,a) in R for a,b in R)
trans = all((a,c) in R for a,b in R for x,c in R if b == x)
print("Reflexive:", ref)
print("Symmetric:", sym)
print("Transitive:", trans)
print("Equivalence Relation:", ref and sym and trans)
print("\nEquivalence Classes:")
for y in sorted(set(year.values())):
    print("Year", y, ":", {s for s in students if year[s] == y})
