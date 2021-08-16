n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<j:
            print(" ",end='  ')
    for j in range(1,n+2):
        if j<i-1:
            print(f"{i-j}",end='  ')
    for j in range(1,n+1):
        if j<i:
            print(f"{j}",end='  ')
    print('\n')

# OUTPUT->

#          1

#       2  1  2

#    3  2  1  2  3

# 4  3  2  1  2  3  4