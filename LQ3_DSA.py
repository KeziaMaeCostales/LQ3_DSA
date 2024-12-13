import getpass

# Ticket Persons with username and password
users = {"admin": "123", "staff": "pass"}

# Bus data (3 buses, 30 seats each)
buses = {
    "Cubao": ["AVAILABLE" for _ in range(30)],
    "Baguio": ["AVAILABLE" for _ in range(30)],
    "Pasay": ["AVAILABLE" for _ in range(30)]
}

def view_buses():
    """Display all buses and their seats."""
    for bus, seats in buses.items():
        print(f"\n{bus} Bus:")
        for i, seat in enumerate(seats, start=1):
            print(f"Seat {i}: {seat}")

def manage_bus(bus_name):
    """Add or remove reservations for a specific bus."""
    while True:
        print("\n(a) Add Reservation\n(b) Remove Reservation\n(c) Back")
        action = input("Choose: ").lower()

        if action == "a":
            print(f"\n{bus_name} - Add Reservation")
            for i, seat in enumerate(buses[bus_name], start=1):
                if seat == "AVAILABLE":
                    print(f"Seat {i}: {seat}")
            try:
                seat_no = int(input("Enter seat number: "))
                if 1 <= seat_no <= 30 and buses[bus_name][seat_no - 1] == "AVAILABLE":
                    name = input("Enter customer name: ")
                    buses[bus_name][seat_no - 1] = name
                    print("Reservation successful!")
                else:
                    print("Invalid or taken seat.")
            except ValueError:
                print("Invalid input.")

        elif action == "b":
            print(f"\n{bus_name} - Remove Reservation")
            for i, seat in enumerate(buses[bus_name], start=1):
                print(f"Seat {i}: {seat}")
            try:
                seat_no = int(input("Enter seat number: "))
                if 1 <= seat_no <= 30 and buses[bus_name][seat_no - 1] != "AVAILABLE":
                    buses[bus_name][seat_no - 1] = "AVAILABLE"
                    print("Reservation removed.")
                else:
                    print("Seat is already available.")
            except ValueError:
                print("Invalid input.")

        elif action == "c":
            return

        else:
            print("Invalid choice.")

def ticket_person_menu():
    """Menu for Ticket Person."""
    while True:
        print("\n(a) View Buses\n(b) Manage Bus\n(c) Logout")
        choice = input("Choose: ").lower()

        if choice == "a":
            view_buses()
        elif choice == "b":
            print("\nWhich bus? (a) Cubao (b) Baguio (c) Pasay")
            bus_choice = input("Choose: ").lower()
            if bus_choice == "a":
                manage_bus("Cubao")
            elif bus_choice == "b":
                manage_bus("Baguio")
            elif bus_choice == "c":
                manage_bus("Pasay")
            else:
                print("Invalid bus choice.")
        elif choice == "c":
            print("Logging out...")
            return
        else:
            print("Invalid choice.")

def main():
    """Main program."""
    while True:
        print("\nWelcome to Bus Reservation System")
        print("(a) Ticket Person\n(b) Exit")
        user_type = input("Choose: ").lower()

        if user_type == "a":
            print("\nLogin")
            username = input("Username: ")
            password = getpass.getpass("Password: ")

            if username in users and users[username] == password:
                print("Login successful!")
                ticket_person_menu()
            else:
                print("Invalid credentials.")

        elif user_type == "b":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
