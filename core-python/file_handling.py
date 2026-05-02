while True:
    print("\n1. Add Note\n2. View Notes\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        note = input("Enter note: ")
        with open("notes.txt", "a") as f:
            f.write(note + "\n")

    elif choice == "2":
        with open("notes.txt", "r") as f:
            print("\nYour Notes:")
            print(f.read())

    elif choice == "3":
        break

    else:
        print("Invalid choice")