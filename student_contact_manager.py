contacts = {}
emails = set()
phones = set()

while True:
    print("\nSTUDENT CONTACT MANAGER")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. List Contacts")
    print("6. Exit")

    choice = input("choose an option: ")

    if choice == "1":
        uid = input("enter ID/Email: ")
        name = input("Full Name: ")
        email = input("Email: ")
        phone = input("Phone Number: ")
        role = input("Role (Student/parent/teacher): ").lower()

        if uid in contacts:
            print("ID already exists!")
        elif email in emails:
            print("Email already exists!")
        elif phone in phones:
            print("phone number already exists!")
        elif not all([uid, name, email, phone, role]):
            print("All fields are required!")
        elif "@" not in email or "." not in email:
            print("Invalid email!")
        elif not phone.isdigit():
            print("phone must contain digits only!")
        elif role not in ["student", "parent", "teacher"]:
            print("invalid role!")
        else:
            contacts[uid] = {
                "name": name,
                "email": email,
                "phone": phone,
                "role": role
            }
            emails.add(email)
            phones.add(phone)
            print("contact added successfully!")

    elif choice == "2":
        uid = input("Enter ID to update: ")

        if uid in contacts:
            old = contacts[uid]
            email = input("New email: ")
            phone = input("New phone: ")

            if (email != old["email"] and email in emails) or \
               (phone != old["phone"] and phone in phones):
                print("Email or phone already exists!")

            elif "@" not in email or "." not in email:
                print("invalid email")

            elif not phone.isdigit():
                print("phone must contain digit only!")

            else:

                emails.discard(old["email"])
                phones.discard(old["phone"])

                old["email"] = email
                old["phone"] = phone

                email.add(email)
                phones.add(phone)

                print("contact Updated!")
        else:
            print("Contact not found!")

    elif choice == "3":
        uid = input("Enter ID to delete: ")
        if uid in contacts:
            emails.discard(contacts[uid]["email"])
            phones.discard(contacts[uid]["phone"])
            del contacts[uid]
            print("contact deleted!")
        else:
            print("contact not found!")

    elif choice == "4":
        uid = input("Enter ID to search: ")
        if uid in contacts:
            print(contacts[uid])
        else:
            print("contact not found!")

    elif choice =="5":
        for uid, details in contacts.items():
            print("\nID:", uid)
            for key, value in details.items():
                print(key.capitalize(), ":", value)

        if not contacts:
            print("No contacts available.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("invalid choice!")