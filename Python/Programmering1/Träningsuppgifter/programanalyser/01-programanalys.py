ZU = 88
CE = 34
GU = 49
ZU += 2
ZU += 7 * 5
print("1", ZU > 100)
print("2", CE + ZU < 50)
CE -= 40
print("3", CE <= 0)
GU += ZU - CE
print("4", GU > 170)
CE -= GU - ZU -100
ZU += 40
GU -= 50
print("5", CE > GU)
print("6", GU > ZU)
ZU = ZU + GU
GU = CE
CE = CE - ZU
ZU = 55 - ZU
print("7", ZU > -250)
print("8", GU < 40)
print("9", CE > 250)
CE *= -1
print("10", CE <= 250)
ZU *= -1
ZU = ZU - 200
ZU /= 8
print("11", ZU > 4 and ZU != 7)
print("12", ZU == 7 or ZU == CE/51.2)
CE = ZU - CE + GU
GU = CE - GU + ZU
ZU = GU - ZU + CE
print("13", CE*-1 > 200)
print("14", (GU*-1 + 10) / 8 == 32 and ZU < -500)
CE *= -1
GU *= -1
ZU *= -1
CE = CE / 10
ZU = ZU / 10
GU = GU / 10
print("15", CE)
print("16", GU)
print("17", ZU)
