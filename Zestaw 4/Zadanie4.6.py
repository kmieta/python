sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
def sum_seq(sequence):
    suma = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            suma += sum_seq(i)
        else: suma += i
    return suma

print(sum_seq(sequence))