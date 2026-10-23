x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

Program się skompiluje, aczkolwiek w pythonie nie używa się średników na końcu linii. Nawiasy w operacji warunkowej również są opcjonalne. Instrukcję warunkową można uprościć pisząc wyrażenie trójargumentowe result = x if x > y else y 


for i in "axby": if ord(i) < 100: print (i)

Program się nie skompiluje, kod jest niepoprawny składniowo. Pętla for wymaga aby instrukcja warunkowa była umieszczona w osobnej linii.


for i in "axby": print (ord(i) if ord(i) < 100 else i)

Program się skompiluje, w przeciwieństwie do poprzedniego przykładu python pozwala na pojawienie się wyrażenia po prawej stronie gdyż jest ono instrukcją prostą czyli mieszczącą się w jednym wierszu