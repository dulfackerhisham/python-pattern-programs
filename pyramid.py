n = 4
# for i in range(1,n+1):
#   print(" "*(n-i),("*"+' ')*(i))

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    print("* "* i)
