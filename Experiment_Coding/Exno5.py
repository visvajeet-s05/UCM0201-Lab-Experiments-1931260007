A = {1, 2, 3, 4}
B = {"IT", "CSE", "ECE"}
f = {1: "IT", 2: "CSE", 3: "ECE", 4: "CSE"}

print("Function Mapping:")
for student in sorted(A):
    print(student, "->", f[student])

r = set(f.values())
print("\nRange:", r)
print("Injective:", len(r) == len(A))
print("Surjective:", r == B)
