n = 5

for row in range(n+1):
    for col in range(n-row):
        print(" ",end='')
    for col in range(row):
        print("*",end='')
    print()
    


# Output

#     *
#    **
#   ***
#  ****
# ***** 

 