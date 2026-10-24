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
