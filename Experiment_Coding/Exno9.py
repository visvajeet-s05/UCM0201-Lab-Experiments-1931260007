f = lambda x: x + 5000
g = lambda x: 0.9 * x
salary = 30000
gf, fg = g(f(salary)), f(g(salary))
print("Basic Salary:", salary)
print("After Bonus:", f(salary))
print("g(f(x)):", gf)
print("f(g(x)):", fg)
print("Equal:", gf == fg)
