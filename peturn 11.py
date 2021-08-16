n= 5
for i in range(1, n):
    for j in range(1, n+1):
        if i<j:
            print(f" ",end='  ')
    for j in range(1, n+1):
        if j<=i:
            print(f"*",end='  ')
        
    for j in range(1, n+1):
        if j<i:
            print(f"*",end='  ')
    print('\n')
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<i:
            print(f" ",end='  ')
    for j in range(1, n+1):
        if i<=j:
            print(f"*",end='  ')
    for j in range(1, n+1):
        if i<j:
            print(f"*",end='  ')
    print('\n')



# output ------->>

#             *  

#          *  *  *

#       *  *  *  *  *

#    *  *  *  *  *  *  *

# *  *  *  *  *  *  *  *  *

#    *  *  *  *  *  *  *

#       *  *  *  *  *

#          *  *  *

#             *