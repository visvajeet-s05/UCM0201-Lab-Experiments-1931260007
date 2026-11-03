A = {1, 2, 3}
R = {(1,1), (2,2), (3,3), (1,2), (2,3), (1,3)}

reflexive = all((a,a) in R for a in A)
symmetric = all((b,a) in R for a,b in R)
antisymmetric = all(a == b or (b,a) not in R for a,b in R)
transitive = all((a,c) in R for a,b in R
                 for x,c in R if b == x)

print("Reflexive:", reflexive)
print("Symmetric:", symmetric)
print("Antisymmetric:", antisymmetric)
print("Transitive:", transitive)
print("Partial Order:", reflexive and antisymmetric and transitive)
