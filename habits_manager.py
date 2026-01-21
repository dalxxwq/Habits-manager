from traceback import print_tb

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
        habits.append({"name": choose, "done": False})
        repeat = input(f"{choose} was added. Wanna add smth else? Yes/No")
        if repeat.lower() not in ["yes", "yeah", "yep", "y"]:
            break

"Show habits"
def show_habit():
    if not habits:
        print("\n[!] No habits found.")
        return

    print("\n" + "=" * 40) #print forty "=" in a next line
    print(f"{'ID':<3} | {'HABIT NAME':<15} | {'DONE'}") #print id, name of habit and its done or not
    print("-" * 40) #print forty "-"

    for i, habit in enumerate(habits, start=1):# i = id of habit start with 1 not with 0; habit = name and done of habit
        status = "✅" if habit["done"] else "❌"# set status
        print(f"{i:<3} | {habit['name']:<15} | {status}")
        # i:<3              → prints the index (ID) in a field 3 characters wide, left-aligned
        # |                 → column separator
        # habit['name']:<15 → prints the habit name in a field 15 characters wide, left-aligned
        # |                 → column separator
        # status            → prints the habit status (DONE / NOT DONE)

    print("=" * 40)

"""Mark a habit as done"""
def mark_done():
    while True:
        show_habit()
        try:
            choice = int(input("Enter habit ID to mark as done: "))
            habits[choice - 1]["done"] = True # rename habits if it's false to true
            print("Habit marked as done ✅")
            choose = input("Do u wanna mark ass done smth else? Yes/No ")
            if choose.lower() not in ["yes", "yep", "yeah", "ye"]:
                break
        except:
            print("Invalid ID.")
            choose = input("Do u wanna mark as done smth else? Yes/No ")
            if choose.lower() not in ["yes", "yep", "yeah", "ye"]:
                break

def statistic():
    if not habits:
        print("\nThere is no habits yet. Try add smth to ur habits")
        return

    total = len(habits)
    done = sum(1 for habit in habits if habit["done"])
    not_done = total-done
    progress = (done/total) * 100

    print("\n" + "="*30)
    print("📊 HABITS STATISTICS")
    print("-"*30)
    print(f"Total habits : {total}")
    print(f"Done         : {done}")
    print(f"Not done     : {not_done}")
    print(f"Progress     : {progress}")
    print("="*30)


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
