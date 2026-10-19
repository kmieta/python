line = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"""
word = "Halloween" 
L = [55 , 44 , 324 , 1 , 432 , 43 , 4 , 9 , 21 , 3 , 13 , 22]
bigInteger = 4593405430304034030
test_GVR = "To jest test GvR ma zmienic GvR"

lineList = line.split()
zad210 = len(lineList)
print("Wynik zadania 2.10: " + str(zad210))

zad211 = "_".join(list(word))
print("Wynik zadania 2.11: " + zad211)


newlist = []
newerList = []
for letter in lineList:
    newlist.append(letter[0])
for letter in lineList:
    newerList.append(letter[-1])
first212= "".join(newlist)
last212 = "".join(newerList)
print("Wynik zadania 2.12: " + first212 + " \n" + "Oraz: " + last212)


lengthList = []
for letter in lineList:
    lengthList.append(len(letter))
zad213 = sum(lengthList)
print("Wynik zadania 2.13: " + str(zad213))


largestLetterIndex = lengthList.index(max(lengthList))
longest214 = lineList[largestLetterIndex]
length214 = max(lengthList)
print("Wynik zadania 2.14: " + "\n" + "Najdluzszy wyraz: " + longest214 + "\n" + "Jego dlugosc: " + str(length214) + " liter")


strL = list(map(str, L))
zad215 = "".join(strL)
print("Wynik zadania 2.15: " + zad215)


zad216 = test_GVR.replace("GvR","Guido van Rossum")
print("Wynik zadania 2.16: " + zad216)


alphabetic217 = sorted(list(map(lambda x: x.lower(), lineList)))
length217 = sorted(lineList, key=len)
print("Wynik zadania 2.17: ")
print("Alfabetycznie:")
print(alphabetic217)
print("Wzgledem dlugosci:")
print(length217)


strBigInteger = str(bigInteger)
zad218 = strBigInteger.count('0')
print("Wynik zadania 2.18: " + str(zad218))


strL = list(map(str, L))
zerosL = []
for ls in strL:
    zerosL.append(ls.zfill(3))
zad219 = " ".join(zerosL)
print("Wynik zadania 2.19: " + zad219)

expected210 = 69
expected211 = "H_a_l_l_o_w_e_e_n"
expectedFirst212 = "LidsacaesdetiuledmaUeamvqneulnuaeeccDaidirivvecdefnpEsocnpsicqodmaiel"
expectedLast212 = "mmrt,rg,dodrttetea.tmdm,sdnositpxao.seerntnetemeuta.rtttn,tnaiattmdtm"
expected213 = 376
expectedLongest214 = "reprehenderit"
expectedLength214 = 13
expected215 = "5544324143243492131322"
expected216 = "To jest test Guido van Rossum ma zmienic Guido van Rossum"
expectedAlphabetically217 = ['ad', 'adipiscing', 'aliqua.', 'aliquip', 'amet,', 'anim', 'aute', 'cillum', 'commodo', 'consectetur', 'consequat.', 'culpa', 'cupidatat', 'deserunt', 'do', 'dolor', 'dolor', 'dolore', 'dolore', 'duis', 'ea', 'eiusmod', 'elit,', 'enim', 'esse', 'est', 'et', 'eu', 'ex', 'excepteur', 'exercitation', 'fugiat', 'id', 'in', 'in', 'in', 'incididunt', 'ipsum', 'irure', 'labore', 'laboris', 'laborum', 'lorem', 'magna', 'minim', 'mollit', 'nisi', 'non', 'nostrud', 'nulla', 'occaecat', 'officia', 'pariatur.', 'proident,', 'qui', 'quis', 'reprehenderit', 'sed', 'sint', 'sit', 'sunt', 'tempor', 'ullamco', 'ut', 'ut', 'ut', 'velit', 'veniam,', 'voluptate']
expectedLength217 = ['do', 'ut', 'et', 'Ut', 'ad', 'ut', 'ex', 'ea', 'in', 'in', 'eu', 'in', 'id', 'sit', 'sed', 'non', 'qui', 'est', 'enim', 'quis', 'nisi', 'Duis', 'aute', 'esse', 'sint', 'sunt', 'anim', 'Lorem', 'ipsum', 'dolor', 'amet,', 'elit,', 'magna', 'minim', 'irure', 'dolor', 'velit', 'nulla', 'culpa', 'tempor', 'labore', 'dolore', 'cillum', 'dolore', 'fugiat', 'mollit', 'eiusmod', 'aliqua.', 'veniam,', 'nostrud', 'ullamco', 'laboris', 'aliquip', 'commodo', 'officia', 'laborum', 'occaecat', 'deserunt', 'voluptate', 'pariatur.', 'Excepteur', 'cupidatat', 'proident,', 'adipiscing', 'incididunt', 'consequat.', 'consectetur', 'exercitation', 'reprehenderit']
expected218 = 6
expected219 = "055 044 324 001 432 043 004 009 021 003 013 022"

assert zad210 == expected210
assert zad211 == expected211
assert first212 == expectedFirst212
assert last212 == expectedLast212
assert zad213 == expected213
assert longest214 == expectedLongest214
assert length214 == expectedLength214
assert zad215 == expected215
assert zad216 == expected216
assert alphabetic217 == expectedAlphabetically217
assert length217 == expectedLength217
assert zad218 == expected218
assert zad219 == expected219


