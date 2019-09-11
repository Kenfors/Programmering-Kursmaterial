import turtle
pen = turtle.Turtle()

# Skapa värden.
KEYBOARD = input("Choose distance: ")
DISTANCE1 = int(KEYBOARD)
KEYBOARD = input("Choose another distance:")
DISTANCE2 = int(KEYBOARD)

# Kör script.
pen.forward(DISTANCE1)
pen.left(DISTANCE1)
pen.forward(DISTANCE2)
pen.circle(DISTANCE2)


# Uppgiften.
# - Deklarera 10 variabler
# - Användaren skriver in värden som ska användas
# - Efter användaren har skrivit in värden, ritas resultatet.
# - Välj själv om programmet använder värderna för left/forward/circle


turtle.done()