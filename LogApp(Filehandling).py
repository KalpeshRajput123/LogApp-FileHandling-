        ##  Log App File Handling

def addrec(t):
    with open("database.txt", "a") as file:
        i, n, a, l = t
        file.write(f"{i:5} {n:10} {a:3} {l:12}\n")
    print("Record Inserted Successfully...")

def updaterec(ids, rec):
    with open("database.txt", "r") as file:
        content = file.readlines()

    data = [line.strip().split() for line in content]
    data.pop(ids)
    data.insert(ids, rec)

    with open("database.txt", "w") as file:
        for i, n, a, l in data:
            file.write(f"{i:5} {n:10} {a:3} {l:12}\n")
    print("Record Updated Successfully...")

def deleterec(ids):
    with open("database.txt", "r") as file:
        content = file.readlines()

    data = [line.strip().split() for line in content]
    data.pop(ids)

    with open("database.txt", "w") as file:
        for i, n, a, l in data:
            file.write(f"{i:5} {n:10} {a:3} {l:12}\n")
    print("Record Deleted Successfully...")

def read_data():
    with open("database.txt", "r") as file:
        content = file.read()
    print(content)

def print_menu():
    print("\nMenu:")
    print("1. Insert Record")
    print("2. Update Record")
    print("3. Delete Record")
    print("4. Read Data")
    print("5. Quit")

data = [
    ["Id", "Name", "Age", "Place"],
    ["1", "Kalpesh", "10", "Dombivli"],
    ["2", "Mahesh", "20", "Thane"],
    ["3", "Brijesh", "30", "Vasai"],
    ["4", "Kunal", "40", "Thane"]
]

with open("database.txt", "a") as file:
    for i, n, a, l in data:
        file.write(f"{i:5} {n:10} {a:3} {l:12}\n")

print("Initial Data Inserted Successfully...")

while True:
    print_menu()

    choice = input("Enter your choice (1/2/3/4/5): ").strip()

    if choice == '1':
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        place = input("Enter Place: ")
        new_record = [id, name, age, place]
        addrec(new_record)
    elif choice == '2':
        ids = int(input("Enter the ID of the record to update: "))
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        place = input("Enter Place: ")
        updated_record = [id, name, age, place]
        updaterec(ids, updated_record)
    elif choice == '3':
        ids = int(input("Enter the ID of the record to delete: "))
        deleterec(ids)
    elif choice == '4':
        read_data()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Try again.")

print("Exiting the program...")













