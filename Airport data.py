airport_data = {}

def add_new_airport():
    icao = input("Enter the ICAO code of the airport: ")
    name = input("Enter the name of the airport: ")
    airport_data[icao] = name
    print("Airport added successfully!")

def fetch_airport_info():
    icao = input("Enter the ICAO code of the airport: ")
    if icao in airport_data:
        print(f"The name of the airport with ICAO code {icao} is {airport_data[icao]}")
    else:
        print("Airport not found!")

while True:
    print("Choose an option:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        add_new_airport()
    elif choice == "2":
        fetch_airport_info()
    elif choice == "3":
        break
    else:
        print("Invalid choice! Please try again.")
print("Program execution ended.")