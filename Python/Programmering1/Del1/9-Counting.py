print("\n\n")
distance = int(input("Enter distance (kilometers): "))
time = int(input("Enter time (hours): "))
speed = distance / time
print("The speed is", speed, "km/h")

# 1. Konvertera distance till "meter" (km -> m)
distance = (distance * 1000)

# 2. Konvertera time till "sekunder"  (h -> s)
time = (time * 3600)

# 3. Gör ny beräkning till speed.
speed = distance / time

print("The speed is", speed, "m/s")
