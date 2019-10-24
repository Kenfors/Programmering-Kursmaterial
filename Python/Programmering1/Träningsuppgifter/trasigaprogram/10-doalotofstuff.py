# Detta program ska loopa fibonacci-sekvensen
# "0 1 1 2 3 5 8 13 21 ...etc"
# men det blir inte rätt!
# det blir ju så här:
# 0 1 2 4 8 16 32..
# Fixa!


LAST_NUM = 0
THIS_NUM = 1


TIMES = 0

print(0)
while TIMES < 20:
    print(THIS_NUM)
    LAST_NUM = THIS_NUM
    THIS_NUM = LAST_NUM + THIS_NUM
    TIMES += 1
