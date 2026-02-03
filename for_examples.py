i = 0
while i < 10:
    print(i)
    i = i + 1
print(i)

for i in range(10):
    print(i)

for i in range(0,100,7): #all the multiples of 7 that are less than 100
    print(i)

for i in range(15): #same^
        print(7*i)

for i in range(1,11):
    for j in range(i,11): # this can use variables
        print(f"{i} x {j} = {i*j}") #f replaces i and j with their value between 1 and 10

    print()