


#Definition av en while-loop
# n 0 -> 10
n = 0
while n < 10:
    print("while, index has value:", n)
    n+=1



input("continue...")
#Definition av en for-loop
# n 0 -> 10
for n in range(10):
    print("for, index has value:", n)




input("continue...")
# Definition av en recursiv funktion
# n 0 -> 10
def recursion(x, limit):
    if(x < limit):
        print("recursion, index has value:", x)
        recursion(x+1, limit)

recursion(0, 10)

input("continue...")
# Definition av en recursiv backtracking funktion
# n -> 10 -> 0
def recursivebacktracker(y, limit):
    if(y < limit):
        print("backtracking, index has value:", y)
        print("backtracking, index has value:", recursivebacktracker(y+1, limit))
    return y -1

recursivebacktracker(0,10)