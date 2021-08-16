n= 5
k = 0
for i in range(1,n+1):
    k = k+1
    for j in range(1, n+1):
        if j<=i:
            print(f'{k} ',end='  ')
            k = k+1
    print('\n')

# OUTPUT->

# 1   

# 3   4

# 6   7   8

# 10   11   12   13

# 15   16   17   18   19