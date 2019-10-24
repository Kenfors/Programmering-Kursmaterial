# Detta program jämför åldrar
# användaren matar in sin ålder
# och programmer säger om personen är äldre eller större än den andra
# Det finns blandade fel. typfel, fel i jämförelseberäkningarna och
# fel med uträkningarna!


AGE1 = input("Enter person A's age: ")
AGE2 = input("Enter person B's age: ")

MORELESS = ""
DIFF = 0
if AGE1 != AGE2:
    MORELESS = "older"
    DIFF = AGE1 + AGE2
else:
    MORELESS = "younger"
    DIFF = AGE2 + AGE1

print("Person A is", DIFF, "years", MORELESS, "than Person B")
