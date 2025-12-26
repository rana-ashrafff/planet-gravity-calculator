gravity = {
    "mercury": 0.38,
    "venus": 0.91,
    "earth": 1.00,
    "moon": 0.165,
    "mars": 0.38,
    "jupiter": 2.34,
    "saturn": 1.06,
    "uranus": 0.92,
    "neptune": 1.19    
}

print("Gravity on different planets : ")
weight = float(input("Enter your weight on Earth (in Kg) : "))

print("\nChoose a planet:")

for planet in gravity:
    print("-", planet)

choice = input("Enter the name of the planet from the above list : ").lower()

if choice in gravity:
    new_weight = weight * gravity[choice]

    print(f"\nYour weight on {choice.capitalize()} is {new_weight:.2f} kg")

else:
    print("\nInvalid planet name")    