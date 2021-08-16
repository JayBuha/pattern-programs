
n = 5
for i in range(0, n):
    for j in range(0, n):
        if j<i:
            print('  ',end='  ')
    for k in range(0, n):
        if i<=k:
            print('* ',end='  ')
    print('\n')


# Output ------>>

# *   *   *   *   *

#     *   *   *   *

#         *   *   *

#             *   *

#                 *