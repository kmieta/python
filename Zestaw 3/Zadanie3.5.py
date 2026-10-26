x = 30
ruler = ''
for i in range(x):
    ruler +="|...."
ruler += "|\n"

rulerNumbers = ''
for i in range(x + 1):
    rulerNumbers += str(i)
    rulerNumbers +=  " "
    if i < 9:
        rulerNumbers += " "
    if i < 99:
        rulerNumbers += " "
    if i < 999:
        rulerNumbers += " "
    
    
finalRuler = ruler + rulerNumbers

print(finalRuler)


expected305 = '''|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   '''

assert finalRuler == expected305