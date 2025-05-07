
n = int(input("Enter number of fibonacci you want : "))

first = 0
second = 1
print(first,end=" ")
print(second,end=" ")
for i in range(2,n):
    third = first + second
    first = second
    second = third
    print(third,end=" ")

