listX = []
for x in range(31):
    if(x % 3 != 0): 
        print(x)
        listX.append(x)

listY = []
y = 0
while y < 31:
    if(y % 3 != 0): 
        print(y)
        listY.append(y)
    y+=1

expectedX = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]

expectedY = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]


assert listX == expectedX
assert listY == expectedY