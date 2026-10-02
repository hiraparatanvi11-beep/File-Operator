# 📔 Personal Journal Manager

A simple Python-based **Personal Journal Manager** that uses file handling and exception handling to manage personal journal entries.

## 👩‍💻 Project Details

- Project:-Personal Journal Manager
- Language:- Python
- Tool:- Visual Studio Code
- File Used:- 'journal.txt'

## 🎯 Objective

The objective of this project is to create a Personal Journal Manager using Python file handling and exception handling.

The program allows the user to:

- Add a new journal entry
- View all journal entries
- Search for an entry using a keyword or date
- Delete all journal entries
- Handle file-related exceptions
- Handle invalid user input

## 📌 Features

### 1. Add a New Entry

The user can add a new journal entry.

The program:

- Checks whether the journal file exists
- Creates `journal.txt` if it does not exist
- Prevents blank entries
- Adds the current date and time
- Stores the entry using append mode

### 2. View All Entries

The program reads the journal file and displays all stored journal entries.

If the file does not exist or contains no entries, an appropriate message is displayed.

### 3. Search for an Entry

The user can search for journal entries using:

- Keyword
- Date

The search is case-insensitive.

If a matching entry is found, it is displayed.

### 4. Delete All Entries

The user can delete all journal entries after confirmation.

The program clears the contents of `journal.txt` but does not delete the file.

The user can enter `yes` to confirm or `no` to cancel.

## 🧠 File Handling Concepts Used

### File Creation

The program uses `x` mode to create the journal file if it does not already exist.

->python
file = open(self.filename, "x")

->Append Mode
 -Append mode is used to add new journal entries without removing existing entries.
  ex:-with open(self.filename, "a") as file:

->Read Mode
 -Read mode is used to display and search existing journal entries.
  ex:-with open(self.filename, "r") as file:

 ->Write Mode
 -Write mode is used to clear all journal entries.
  ex:-with open(self.filename, "w") as file:
     file.write("")

⚠️ Exception Handling

->The project demonstrates different types of exception handling.

FileNotFoundError
-Handled when the journal file does not exist.

FileExistsError
-Handled when the program tries to create a file that already exists.

PermissionError
-Handled when the program does not have permission to access the file.

ValueError
-Handled when the user enters an invalid menu choice.

Exception
-A general exception is used to handle unexpected errors.

🕒 Date and Time

-The datetime module is used to store the current date and time with every journal entry.
 ex:-datetime.now().strftime("%Y-%m-%d %H:%M:%S")

📦 Modules Used
 ->os
   -The os module is used to check whether the journal file exists.
    ex:-os.path.exists(self.filename)

 ->datetime
   -The datetime module is used to get the current date and time.
    ex:-from datetime import datetime

🏗️ Class Used
 The project uses a class named:
 ->JournalManager

 The class contains the following methods:
 - __init__()
 - add_entry()
 - view_entries()
 - search_entry()
 - delete_entries()

📋 Main Menu
 1. Add a New Entry
 2. View All Entries
 3. Search for an Entry
 4. Delete All Entries
 5. Exit

🔄 Program Flow

   Start
     ↓
Create JournalManager Object
     ↓
 Display Main Menu
     ↓
 Select an Option
     ↓
1 → Add New Entry
2 → View All Entries
3 → Search Entry
4 → Delete All Entries
5 → Exit
     ↓
Repeat Until Exit

🖥️ Sample Output

Main Menu
========================================
     PERSONAL JOURNAL MANAGER
========================================

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

Enter your choice:

Add New Entry
Enter your journal entry:
Today I completed my Python file handling assignment.

Entry added successfully!
->The entry is stored in journal.txt with the current date and time.

Example:
[2026-09-30 15:30:00]
Today I completed my Python file handling assignment.

View All Entries
Enter your choice: 2

========== JOURNAL ENTRIES ==========

[2026-09-30 15:30:00]
Today I completed my Python file handling assignment.

Search Entry
Enter your choice: 3

Enter keyword or date to search:
Python

========== SEARCH RESULTS ==========

[2026-09-30 15:30:00]
Today I completed my Python file handling assignment.

No Matching Entry
Enter keyword or date to search:
College

No matching entries found.

Delete All Entries
Enter your choice: 4

Are you sure you want to delete all entries? (yes/no):
yes

All journal entries have been deleted.

Invalid Input
Enter your choice: abc

Invalid input. Please enter a valid number.

Exit
Enter your choice: 5

Thank you for using Personal Journal Manager. Goodbye!

📁 Project Structure
Personal-Journal-Manager/
│
├── journal_manager.py
├── journal.txt
└── README.md

journal_manager.py → Main Python program
journal.txt → Stores journal entries
README.md → Project documentation

🛠️ Technologies Used
- Python
- File Handling
- Exception Handling
- Object-Oriented Programming
- OS Module
- Datetime Module
- Visual Studio Code

📌 Project Summary
- The Personal Journal Manager is a Python-based file handling project that allows users to add, view, search, and delete journal entries.
- This project demonstrates important Python concepts such as file creation, reading, writing, appending, searching, date and time handling,
  exception handling, and object-oriented programming.

 👩‍💻 Created By
  
 Tanvi Hirapara
  







