from db import create_tables
from auth import signup, login
from quiz import start_quiz, add_sample_questions

def main():
    create_tables()
    add_sample_questions()

    while True:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            signup()
        elif choice == "2":
            if login():
                start_quiz()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
