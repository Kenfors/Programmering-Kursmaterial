
DATA = []

def cap():
    size = len(DATA)
    print(size)
    while size >= 0:
        DATA[size-1] += " visited"
        size -= 1

i = 0
while i <= 5:
    DATA.append("Obj" + str(i))
    i += 1
    cap()

for item in DATA:
    print("item:", item)

