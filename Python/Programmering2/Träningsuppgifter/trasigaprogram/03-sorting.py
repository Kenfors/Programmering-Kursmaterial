# Programmet sorterar två listor av random tal
# Men det blir inte rätt!
# Fixa

import random

RANDOM = []
for i in range(50):
    RANDOM.append(random.randint(0, 100))

print("Random list: ", RANDOM)

SORTED = RANDOM.copy()

for i in range(len(SORTED)):
    j = i
    while j < len(SORTED) -1:
        if SORTED[j] > SORTED[j +1]:
            TMP = SORTED[j]
            SORTED[j] = SORTED[j + 1]
            SORTED[j + 1] = TMP
        else:
            j += 1
        

print("Sorted list:", SORTED)

