# 30 tips for python optimize

# use list comprehensions

cube_number1 = []
for n in range(0,100000000):
    if n % 2 == 1:
        cube_number1.append(n**3)

cube_number2 = [n**3 for n in range(1,100000000) if n%2 == 1] 