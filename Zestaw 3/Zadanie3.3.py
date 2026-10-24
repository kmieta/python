

for x in range(31):
    if(x % 3 != 0): print(x)

y = 0
while y < 31:
    if(y % 3 != 0): print(y)
    y+=1


while  True:
    line = input("Podaj liczbe rzeczywista, napisz stop aby zakończyć: ")
    if line == "stop":
        break
    try:
        line = float(line)
    except ValueError:
        print("Podana wartość nie jest liczbą")
    if(type(line) == float):
        print(line, line**3)


    

    