n = 5
for i in range(0, n):
    for j in range(0, n):
        if i < j:
            print('  ', end=' ')
    for k in range(0, n):
        if k <= i:
            print('*  ', end='')
    for l in range(0, n):
        if l < i:
            print('* ', end=' ')
    print('\n')



# Output -------->>

#             *

#          *  *  *

#       *  *  *  *  *

#    *  *  *  *  *  *  *

# *  *  *  *  *  *  *  *  *