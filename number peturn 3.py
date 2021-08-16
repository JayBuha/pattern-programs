n= 5
for i in range(1, n+1):
    for j in range(1,n+1):
        if i < j:
            print(f' ',end='  ') 
    for j in range(1,n+1):
        if j <= i:
            print(f'{i}',end='  ') 
    for j in range(1,n+1):
        if j < i:
            print(f'{i}',end='  ')    
    print("\n")

# output --------->>

#             1

#          2  2  2

#       3  3  3  3  3

#    4  4  4  4  4  4  4

# 5  5  5  5  5  5  5  5  5