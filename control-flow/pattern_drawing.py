pattern = int(input('Enter the size of the pattern: '))
p = 0
while p < pattern:
    for i in range(pattern):
       print("*", end="")
    print()
    p +=1
