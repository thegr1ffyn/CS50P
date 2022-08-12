x, y,z = input("Enter an arithmetic expression: ").split()

if y == "+":
    solution = float(x) + float(z)

elif y == "-":
    solution = float(x) - float(z)

elif y == "*":
    solution = float(x) * float(z)

elif y == "/":
    solution = float(x) / float(z)

print(solution)