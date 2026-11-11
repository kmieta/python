#from fractions import gcd   # Py2
from math import gcd   # Py3

def commonDenominator(frac1, frac2):
    if frac1[1] == 0 or frac2[1] == 0:
        raise ZeroDivisionError
    mianownik = frac1[1] * frac2[1]
    licznik1 = frac1[0] * frac2[1]
    licznik2 = frac2[0] * frac1[1]
    return [licznik1 , licznik2, mianownik]

def add_frac(frac1, frac2):         # frac1 + frac2
    commonfrac = commonDenominator(frac1, frac2)
    return [ commonfrac[0] + commonfrac[1] , commonfrac[2] ]
 
def sub_frac(frac1, frac2):         # frac1 - frac2
    commonfrac = commonDenominator(frac1, frac2)
    return [ commonfrac[0] - commonfrac[1] , commonfrac[2] ]

def mul_frac(frac1, frac2):        # frac1 * frac2
    commonfrac = commonDenominator(frac1, frac2)
    return [ commonfrac[0] * commonfrac[1] , commonfrac[2] ]

def div_frac(frac1, frac2):         # frac1 / frac2
    commonfrac = commonDenominator(frac1, frac2)

    return [ commonfrac[0] , commonfrac[1]]

def is_positive(frac):  # bool, czy dodatni
        if (frac[0] < 0 and frac[1] >= 0 ) or (frac[0] >= 0 and frac[1] < 0):
            return False
        else:
            return True 
        
def is_zero(frac):          # bool, typu [0, x]
    if frac[1] == 0:
        raise ZeroDivisionError
    return frac[0] == 0                     

def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    fr2fl1 = frac2float(frac1)
    fr2fl2 = frac2float(frac2)
    if fr2fl1 == fr2fl2:
        return 0
    elif fr2fl1 > fr2fl2:
        return -1
    else: 
        return 1
    
def frac2float(frac): # konwersja do float
    if frac[1] == 0:
        raise ZeroDivisionError
    return frac[0] / frac[1]

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        pass
     #   self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): pass

    def test_mul_frac(self): pass

    def test_div_frac(self): pass

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def test_cmp_frac(self): pass

    def test_frac2float(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    #unittest.main()     # uruchamia wszystkie testy

    print(add_frac([1,5],[4,7]))
    print(sub_frac([1,5],[4,7]))
    print(div_frac([3,5],[4,9]))
    print(is_positive([-1,-7]))
    print(cmp_frac([6,5],[6,10]))