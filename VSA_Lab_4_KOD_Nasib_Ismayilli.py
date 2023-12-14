massiv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

bolunenler = [eded for eded in massiv if eded % 3 == 0]

Cem = sum(bolunenler)

with open('bolunenler.txt', 'w') as f:
    for eded in bolunenler:
        f.write(str(eded) + '\n')

print("3-e bolunen ededler:", bolunenler)
print("Cem:", Cem)

