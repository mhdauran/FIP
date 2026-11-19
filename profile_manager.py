import json
import os

FILE_NAME = "profile.json"

def get_valid_name():
    """collect and validate the user's name."""
    while True:
        name = input("enter your full name: ").strip()
        if name.replace(" ", "").isalpha() and name:
            return name
        else:
            print("invalid name. please enter letters only.")

def get_valid_age():
    """collect and validate the user's age."""
    while True:
        try:
            age = int(input("enter your age: "))
            if 1 <= age <= 90:
                return age
            else:
                print("age must be between 1 and 90.")
        except valueError:
            print("invalid input. please enter a number.")

def get_valid_email():
    """collect and validate the user's email."""
    while True:
        email = input("enter your email: ").strip()
        if (
            email.count("@") == 1 and "." not in email
        ):
            return email
        else:
            print("invalid email address. try again.")


def collect_profile():
    """collect the user's profile information."""
    print("\n --- CREATE YOUR PROFILE ---")

    profile = {
        "name": get_valid_name(),
        "age": get_valid_age(),
        "email": get_valid_email(),
        "country": input("enter your country: ").strip()
    }

    if not profile["country"]:
        print("country cannot be empty.")
        profile["country"] = input("enter your country: ").strip()

    return profile

def save_profile(profile):
    """save the profile in a formatted JSON file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(profile, file, indent=4)
        print("\nprofile saved successfully!")

    except OSError as error:
        print(f"Error saving profile: {error}")

def read_profile():
    """read and display the saved profile."""
    if not os.path.exists(FILE_NAME):
        print("\nNo saved profile found.")
        return
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            profile = json.load(file)
        print("\n --- SAVED USER PROFILE ---")

        for key, value in profile.items():
            print(f"{key.capitalize()}: {value}")
    except (OSError, json.JSONDecodeError) as error:
        print(f"Eror reading profile: {error}")


def main():
    while True:
        print("\n===== USER PROFILE MANAGER =====")
        print("1. create a new profile")
        print("2. view saved profile")
        print("3. exit")

        choice = input("choose an option (1-3): ").strip()

        if choice == "1":
            profile = collect_profile()
            save_profile(profile)

        elif choice == "2":
            read_profile()

        elif choice == "3":
            print("thank you for using profile manager!")
            break
        else:
            print("invalid choise please select 1,2, or 3.")

if __name__ == "__main__":
    main()