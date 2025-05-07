# take input from user
nums = int(input("Enter your numbers : "))

r = 0

while nums>0:
    digit = nums % 10
    r = digit + r * 10
    nums = nums // 10
print(r)