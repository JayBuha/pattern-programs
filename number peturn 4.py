n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i<j:
            print(" ", end="  ")
    for j in range(1, n+1):
        if j<=i:
            print(f"{j}", end="  ")
    for j in range(1, n+1):
        if j<i:
            print(f"{j}", end="  ")
    print("\n")

# Output -------->>

#             1

#          1  2  1

#       1  2  3  1  2

#    1  2  3  4  1  2  3

# 1  2  3  4  5  1  2  3  4