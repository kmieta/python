def makeruler(x):
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
    return finalRuler

expectedRuler = '''|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   '''

assert makeruler(30) == expectedRuler

def make_grid(x , y):
    rows = ''
    dashes = ''

    for i in range(x):
        rows += "+---"
        dashes += '|   '
    rows += "+\n"
    dashes += "|\n"

    col = rows + dashes
    finalstr = ''
    for i in range(y):
        finalstr += col
    finalstr += rows

    return finalstr
    
expectedGrid = '''+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
'''

assert make_grid(4,2) == expectedGrid