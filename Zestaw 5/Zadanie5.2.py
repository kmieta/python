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
    if frac1[1] == 0 or frac2[1] == 0:
        raise ZeroDivisionError
    gDivisor = gcd(frac1[0] * frac2[0],frac1[1] * frac2[1])
    return [ int(frac1[0] * frac2[0]/gDivisor), int(frac1[1] * frac2[1]/gDivisor) ]

def div_frac(frac1, frac2):         # frac1 / frac2
    if is_zero(frac2):
        raise ZeroDivisionError
    return mul_frac(frac1, [frac2[1],frac2[0]])

def is_positive(frac):  # bool, czy dodatni
        if frac[1] == 0:
            raise ZeroDivisionError
        if (frac[0] < 0 and frac[1] >= 0 ) or (frac[0] >= 0 and frac[1] < 0):
            return False
        else:
            return True 
        
def is_zero(frac):      # bool, typu [0, x]
    if frac[1] == 0:
        raise ZeroDivisionError
    return frac[0] == 0                     

def cmp_frac(frac1, frac2):     # -1 | 0 | +1
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

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.banned = [0, 0]
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertRaises(ZeroDivisionError, add_frac, self.banned, [1,3])
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): 
        self.assertRaises(ZeroDivisionError, sub_frac, self.banned, [1,3])
        self.assertEqual(sub_frac([1,2], [1,3]), [1, 6])
        self.assertEqual(sub_frac([1,3], [1,2]), [-1, 6])

    def test_mul_frac(self):
      self.assertRaises(ZeroDivisionError, mul_frac, self.banned, [1,3])
      self.assertEqual(mul_frac([1,2], [1,3]), [1, 6])
      self.assertEqual(mul_frac([2,8],[3,9]),[1,12])
      self.assertEqual(mul_frac([9,12],[4,16]),[3,16])

    def test_div_frac(self):
        self.assertRaises(ZeroDivisionError, div_frac, [1,3], self.zero)
        self.assertRaises(ZeroDivisionError, div_frac, self.banned, [1,3])
        self.assertEqual(div_frac([1,2],[1,3]), [3 , 2])
        self.assertEqual(div_frac([2,3], [1,3]), [2, 1])
        self.assertEqual(div_frac([8,11],[3,5]),[40,33])
        self.assertEqual(div_frac([6,7],[24,7]),[1,4])

    def test_is_positive(self): 
        self.assertRaises(ZeroDivisionError, is_positive, self.banned)
        self.assertTrue(is_positive([1,2]))
        self.assertTrue(is_positive([-1,-2]))
        self.assertFalse(is_positive([-1,2]))
        
    def test_is_zero(self):
        self.assertRaises(ZeroDivisionError, is_zero, self.banned)
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero([1,2]))
        self.assertTrue(is_zero([0,5]))

    def test_cmp_frac(self): 
        self.assertRaises(ZeroDivisionError, cmp_frac, self.banned, [1,3])
        self.assertEqual(cmp_frac([1,2], [1,3]), -1)
        self.assertEqual(cmp_frac([1,3], [1,2]), 1)
        self.assertEqual(cmp_frac([1,3], [3,9]), 0)
        self.assertEqual(cmp_frac([2,5], [1,3]), -1)

    def test_frac2float(self): 
        self.assertRaises(ZeroDivisionError, frac2float, self.banned)
        self.assertEqual(frac2float([16,4]), 4)
        self.assertEqual(frac2float([0,2]), 0)
        self.assertEqual(frac2float([1,3]), float(1/3))
        self.assertEqual(frac2float([2,7]), float(2/7))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
