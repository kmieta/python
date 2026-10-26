x = 4
y = 2
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

expected306 = '''+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
'''

assert finalstr == expected306