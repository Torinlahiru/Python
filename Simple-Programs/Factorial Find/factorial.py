n = int(input("Enter number you want factorial : "))

fac = 1

for i in range(n):
    fac = fac + fac * i
print(fac)