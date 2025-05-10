m = int(input("Enter number of row : "))
n = int(input("Enter number of col : "))

matrix = []

print("Enter element row by row : ")

for i in range(m):
    row = list(map(int,input(" ").split()))
    matrix.append(row)

for i in matrix:
    print(*i)

# Also you can use this
# for i in matrix:
#     print(" " .join(map(str,i)))
