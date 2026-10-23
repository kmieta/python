## Zadanie 3.1
    x = 2; y = 3;
    if (x > y):
        result = x;
    else:
        result = y;

Program się skompiluje, aczkolwiek w pythonie nie używa się średników na końcu linii. Nawiasy w operacji warunkowej również są opcjonalne. Instrukcję warunkową można uprościć pisząc wyrażenie trójargumentowe **result = x if x > y else y**

## 
    for i in "axby": if ord(i) < 100: print (i)

Program się nie skompiluje, kod jest niepoprawny składniowo. Pętla for wymaga aby instrukcja warunkowa była umieszczona w osobnej linii.

##
    for i in "axby": print (ord(i) if ord(i) < 100 else i)

Program się skompiluje, w przeciwieństwie do poprzedniego przykładu python pozwala na pojawienie się wyrażenia po prawej stronie gdyż jest ono instrukcją prostą czyli mieszczącą się w jednym wierszu.

## Zadanie 3.2

    L = [3, 5, 4] ; L = L.sort()
W drugiej linijce L.sort() zwraca None oraz przypisuje je do zmiennej L. poprawnie byłoby: 

    L = [3, 5, 4] ; L.sort()
##
    x, y = 1, 2, 3

Jedna zmienna przypisuje jedną wartość, tutaj wartości jest więcej niż zmiennych. Poprawne wyznaczenie tupli natomiast wyglądałoby następująco: __x, *y = 1 , 2 , 3__
##
    X = 1, 2, 3 ; X[1] = 4
Tuple są niemodyfikowalne (immutable) nie można zatem przypisać na nowo jej wartości.
##
    X = [1, 2, 3] ; X[3] = 4
Lista kończy się na elemencie numer 2, index trzeci jest poza zasięgiem.
##
    X = "abc" ; X.append("d")
.append() działa tylko na obiektach modyfikowalnych, stringi w pythonie są niemodyfikowalne (immutable).
##
    L = list(map(pow, range(8)))
Funkcja pow przyjmuje od 2 do 3 argumentów, w przykładzie jest jeden argument, brakuje natomiast wykładnika potegi. 
