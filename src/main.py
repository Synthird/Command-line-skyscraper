print("How many floors do you want in your skyscraper?")

floors = int(input("Floors (Please enter only integers): "))

for _ in range(3):
    print("   .")

for _ in range(floors):
    print(".......")
