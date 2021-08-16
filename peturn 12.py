n= 5
for i in range(1, n):
    for j in range(1, n+1):
        if i<j:
            print(f" ",end='  ')
    for j in range(1, n+1):
        if j<i:
            if j==1:
                print(f"*",end='  ')
            else:
                print(f" ",end='  ')
        
    for j in range(1, n+1):
        if j<=i:
            if i==j:  
                print(f"*",end='  ')
            else:
                print(f" ",end='  ')

    print('\n')
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<i:
            print(f"{' '}",end='  ')
    for j in range(1, n+1):
        if i<=j:
            if i==j:
                print(f"*",end='  ')
            else:
                print(f' ',end='  ')
    for j in range(1, n+1):
        if i<j:
            if j==n:
                print(f"*",end='  ')
            else:
                print(f' ',end='  ')
    print('\n')

# OUTPUT->

#             *  

#          *     *

#       *           *

#    *                 *

# *                       *

#    *                 *

#       *           *

#          *     *

#             *