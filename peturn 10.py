n = 5
for i in range(0, n):
    for j in range(0,n):
        if i<j:
            print('  ',end=' ')
    for j in range(0,n):
        if j<i:
            print('* ',end=' ') 
    for j in range(0,n):
        if j<=i:
            print('* ',end=' ')
    for j in range(0,n):
        if i<j:
            print('  ',end=' ') 
    for j in range(0,n):
        if i<j:
            print('  ',end=' ')
    for j in range(0,n):
        if j<i:
            print('* ',end=' ') 
    for j in range(0,n):
        if j<=i:
            print('* ',end=' ')
    print('\n')
for i in range(0, n):
    for j in range(0, n-1):
        if j<n:
            print('  ',end=' ')
    for j in range(0, n):
        if j<i:
            print('  ',end=' ')
    for j in range(0, n):
        if i<j:
            print('*  ',end='')
    for j in range(0, n):
        if i<=j:
            print('*  ',end='')
    print('\n')


#  Output ------->>

#             *                          *

#          *  *  *                    *  *  *

#       *  *  *  *  *              *  *  *  *  *

#    *  *  *  *  *  *  *        *  *  *  *  *  *  *

# *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *

#             *  *  *  *  *  *  *  *  *

#                *  *  *  *  *  *  *

#                   *  *  *  *  *

#                      *  *  *

#                         *
