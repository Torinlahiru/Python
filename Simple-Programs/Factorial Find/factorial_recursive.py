
num = int(input("Enter number you want : ")) 
def find_factorial(n):
    if n == 0 or n ==1 :
        return 1
    else:
        return n * find_factorial(n-1)

print(find_factorial(num))
