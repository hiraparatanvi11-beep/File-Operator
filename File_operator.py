import os
from datetime import datetime


# ==========================================
# Personal Journal Manager
# ==========================================

class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    # ------------------------------------------
    # Add a New Entry
    # ------------------------------------------
    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry:\n")

            if entry.strip() == "":
                print("Entry cannot be empty.")
                return

            # Create file if it does not exist
            try:
                file = open(self.filename, "x")
                file.close()
            except FileExistsError:
                pass

            # Append new entry
            with open(self.filename, "a") as file:

                current_time = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                file.write(f"[{current_time}]\n")
                file.write(entry + "\n\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("\nError: Permission denied.")

        except Exception as e:
            print("\nError:", e)

    # ------------------------------------------
    # View All Entries
    # ------------------------------------------
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

            if data.strip() == "":
                print(
                    "\nNo journal entries found. "
                    "Start by adding a new entry!"
                )
            else:
                print("\nYour Journal Entries:")
                print()
                print(data)

        except FileNotFoundError:
            print(
                "\nError: The journal file does not exist. "
                "Please add a new entry first."
            )

        except PermissionError:
            print("\nError: Permission denied.")

        except Exception as e:
            print("\nError:", e)

    # ------------------------------------------
    # Search for an Entry
    # ------------------------------------------
    def search_entry(self):
        try:
            with open(self.filename, "r") as file:
                data = file.readlines()

            keyword = input(
                "\nEnter a keyword or date to search: "
            )

            if keyword.strip() == "":
                print("Search keyword cannot be empty.")
                return

            found = False
            entries = []
            current_entry = []

            # Separate journal entries
            for line in data:

                if line.strip() == "":
                    if current_entry:
                        entries.append(current_entry)
                        current_entry = []
                else:
                    current_entry.append(line.strip())

            if current_entry:
                entries.append(current_entry)

            print("\nMatching Entries:")
            print("-" * 30)

            for entry in entries:

                complete_entry = " ".join(entry)

                if keyword.lower() in complete_entry.lower():

                    for line in entry:
                        print(line)

                    print()
                    found = True

            if not found:
                print(
                    "No entries were found for keyword: "
                    + keyword
                    + "."
                )

        except FileNotFoundError:
            print(
                "\nError: The journal file does not exist. "
                "Please add a new entry first."
            )

        except PermissionError:
            print("\nError: Permission denied.")

        except Exception as e:
            print("\nError:", e)

    # ------------------------------------------
    # Delete All Entries
    # ------------------------------------------
    def delete_entries(self):
        try:

            if not os.path.exists(self.filename):
                print("\nNo journal entries to delete.")
                return

            confirmation = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            )

            if confirmation.lower() == "yes":

                # Clear the data inside the file
                # File itself will NOT be deleted
                with open(self.filename, "w") as file:
                    file.write("")

                print("\nAll journal entries have been deleted.")

            elif confirmation.lower() == "no":

                print("\nDelete operation cancelled.")

            else:

                print(
                    "\nInvalid input. "
                    "Please enter yes or no."
                )

        except PermissionError:
            print("\nError: Permission denied.")

        except Exception as e:
            print("\nError:", e)


# ==========================================
# Main Program
# ==========================================

journal = JournalManager()

print("Welcome to Personal Journal Manager!")
print("Please select an option:")

while True:

    print()
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    try:

        choice = int(input("\nEnter your choice: "))

        # --------------------------------------
        # Add New Entry
        # --------------------------------------
        if choice == 1:

            journal.add_entry()

        # --------------------------------------
        # View All Entries
        # --------------------------------------
        elif choice == 2:

            journal.view_entries()

        # --------------------------------------
        # Search Entry
        # --------------------------------------
        elif choice == 3:

            journal.search_entry()

        # --------------------------------------
        # Delete All Entries
        # --------------------------------------
        elif choice == 4:

            journal.delete_entries()

        # --------------------------------------
        # Exit
        # --------------------------------------
        elif choice == 5:

            print(
                "\nThank you for using "
                "Personal Journal Manager. Goodbye!"
            )

            break

        # --------------------------------------
        # Invalid Option
        # --------------------------------------
        else:

            print(
                "\nInvalid option. "
                "Please select a valid option from the menu."
            )

    except ValueError:

        print(
            "\nInvalid input. "
            "Please enter a number from 1 to 5."
        )

    except Exception as e:

        print("\nUnexpected Error:", e)