habits = []

"""Menu"""
def menu():
    print("=== MY HABITS ===")
    print("1 — Add a habit")
    print("2 — Show habits")
    print("3 — Mark as done")
    print("4 — Statistics")
    print("0 — Exit")
    choose = int(input("Choose an option: "))
    return choose

"""Add a habit"""
def add_habit():
    while True:
        choose = input("What do u want to add to a habit? ")
        habits.append(choose)
        repeat = input(f"{choose} was added to ur habits. Wanna add smth else? ")
        if repeat.lower() not in ["yes", "yeah", "yep"]:
            break

"Show habits"
def show_habit():
    print("Your habits:", habits)

def mark_done():
    print("This feature is not ready yet.")

def statistic():
    print("This feature is not ready yet.")


if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == 1:
            add_habit()
        elif choice == 2:
            show_habit()
        elif choice == 3:
            mark_done()
        elif choice == 4:
            statistic()
        elif choice == 0:
            print("Oh, you’re leaving? Alright then 😄 Bye, see you soon!")
            break
        else:
            print("I think u print smth wrong try again.")
