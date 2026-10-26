A = "djfheosujrfoesfoshdf39reew09fe3256"
B = "fdoogfdpogopfdjogij0-49rdoijfdso3"
setA = set(A)
setB = set(B)


intersection = list(setA.intersection(setB))
union = list(setA.union(setB))
intersection.sort()
union.sort()
print(intersection)
print(union)

expectedIntersection = ['0', '3', '9', 'd', 'f', 'j', 'o', 'r', 's']
expectedUnion = ['-', '0', '2', '3', '4', '5', '6', '9', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'o', 'p', 'r', 's', 'u', 'w']

assert intersection == expectedIntersection
assert union == expectedUnion