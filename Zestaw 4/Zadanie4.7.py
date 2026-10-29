sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
def flatten(sequence):
    suma = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            suma.extend(flatten(i))
        else: suma.append(i)
    return suma

print(flatten(sequence))