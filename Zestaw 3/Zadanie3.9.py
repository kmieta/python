A = [[],[4],(1,2),[3,4],(5,6,7)]
B = []

for i in A: 
    B.append(sum(i))

print(B)

expected309 = [0, 4, 3, 7, 18]
assert B == expected309