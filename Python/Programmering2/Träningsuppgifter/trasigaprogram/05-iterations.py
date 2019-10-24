# This program builds a list with fibonacci sequence numbers
# then prints the full list.
#
# Förklara VARJE kodrad med en kommentar.
# Motivera också varför kommandot behöver utföras. För ingenting är skrivet i onödan.
#
# När du vet hur programmet fungerar.
# -> Gör om loopen till en while-loop istället för en for!
#    Där du inte använder en "range"

# explain
FIBO = [] 

# explain
N, M = 0,1

# explain alot
for i in range(int(input("Enter sequence length: "))):
    TMP = M + N # explain
    FIBO.append(TMP) # explain
    N = M # explain
    M = TMP # explain

print(FIBO) # explain