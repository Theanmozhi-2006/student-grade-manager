import json
students = {}

def add_student(name, mark):
    # add name and mark to students dictionary
    students[name] = mark

def view_students():
    print(students)

def highest_scorer():
    name=max(students, key=lambda x: students[x])
    print(name, students[name])

def lowest_scorer():
    name = min(students, key=lambda x: students[x])
    print(name, students[name])

def class_average():
    print(sum(students.values())/len(students))


def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f)

def load_data():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except:
        students = {}

def menu():

    load_data()
    while True:
        print("\n--- Student Grade Manager ---")
        print("1. Add Student")
        save_data()
        print("2. View All Students")
        print("3. Highest Scorer")
        print("4. Lowest Scorer")
        print("5. Class Average")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            mark = int(input("Enter mark: "))
            add_student(name, mark)
        elif choice == "2":
            view_students()
        elif choice == "3":
            highest_scorer()
        elif choice == "4":
            lowest_scorer()
        elif choice == "5":
            class_average()
        elif choice == "6":
            break
menu()
