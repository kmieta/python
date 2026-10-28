def odwracanieIteracyjnie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1 
        right -= 1
    return L

print(odwracanieIteracyjnie([1,2,3,4,5,6,7,8,9,10],0,9))

def odwracanieRekurencyjnie(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanieRekurencyjnie(L , left + 1, right - 1)
    return L

print(odwracanieRekurencyjnie([1,2,3,4,5,6,7,8,9,10],0,9))


