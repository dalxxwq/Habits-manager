import json

habits = []
FILE_NAME = "habits.json"


"""Load habits"""
def load_habits():
    global habits
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            habits = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        habits = []


"""Save habits"""
def save_habits():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(habits, file, ensure_ascii=False, indent=4)


"""Menu"""
def menu():
    print("\n=== MY HABITS ===")
    print("1 — Add a habit")
    print("2 — Show habits")
    print("3 — Mark as done")
    print("4 — Statistics")
    print("0 — Exit")
    return int(input("Choose an option: "))


"""Add a habit"""
def add_habit():
    while True:
        name = input("What do u want to add to habits? ")
        habits.append({"name": name, "done": False})
        save_habits()

        repeat = input(f"{name} was added. Wanna add smth else? Yes/No: ")
        if repeat.lower() not in ["yes", "yeah", "yep", "y"]:
            break


"""Show habits"""
def show_habit():
    if not habits:
        print("\n[!] No habits found.")
        return

    print("\n" + "=" * 40)
    print(f"{'ID':<3} | {'HABIT NAME':<15} | DONE")
    print("-" * 40)

    for i, habit in enumerate(habits, start=1):
        status = "✅" if habit["done"] else "❌"
        print(f"{i:<3} | {habit['name']:<15} | {status}")

    print("=" * 40)


"""Mark a habit as done"""
def mark_done():
    while True:
        show_habit()
        try:
            choice = int(input("Enter habit ID to mark as done: "))
            habits[choice - 1]["done"] = True
            save_habits()
            print("Habit marked as done ✅")
        except (ValueError, IndexError):
            print("Invalid ID.")

        repeat = input("Do u wanna mark smth else? Yes/No: ")
        if repeat.lower() not in ["yes", "yeah", "yep", "y"]:
            break


"""Statistics"""
def statistic():
    if not habits:
        print("\nThere are no habits yet.")
        return

    total = len(habits)
    done = sum(1 for habit in habits if habit["done"])
    not_done = total - done
    progress = (done / total) * 100

    print("\n" + "=" * 30)
    print("📊 HABITS STATISTICS")
    print("-" * 30)
    print(f"Total habits : {total}")
    print(f"Done         : {done}")
    print(f"Not done     : {not_done}")
    print(f"Progress     : {progress:.1f}%")
    print("=" * 30)


if __name__ == "__main__":
    load_habits()

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
            print("Bye 👋 Habits saved.")
            break
        else:
            print("Wrong option, try again.")
