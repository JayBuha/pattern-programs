n= 5
for i in range(1, n+1):
    for j in range(1, n+1):
        
        if j<=i:
            print(f"{i-j}",end=' ')
    print('\n')

# OUTPUT->

# 0 

# 1 0

# 2 1 0

# 3 2 1 0

# 4 3 2 1 0