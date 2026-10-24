x = 100
ruler = ''
for i in range(x):
    ruler +="|...."
ruler += "| \n"

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
