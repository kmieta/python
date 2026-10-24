x = 1
y = 1
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

print(finalstr)    