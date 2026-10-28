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
