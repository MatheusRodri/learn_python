fam = ["liz",1.73,"emma",1.68,"mom",1.71,"dad",1.89]
print(fam)

fam[0] = "lisa"
print(fam)


fam[0:2] = ["lisa",1.74]
print(fam)

fam += ["me",1.79]
print(fam)

del fam[6]
print(fam)


x = ["a", "b", "c", "d"]
y = x
y[1] = "z"
print(x)
print(y)

x = ["a", "b", "c", "d"]
y = x[:]
y[1] = "z"
print(x)
print(y)