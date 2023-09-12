'''Hack's Letter grade calculator c.2023
___________________________________________________________________________
Taking python a second time, had an assignment to do and wanted
to go above and beyond to practice.

Notes:    
        Can add list to log student names, Add to tuple for -'s and +'s.
___________________________________________________________________________
'''

# Tuple storage for letter grades
lettergrade_tuple = ("A", 'B', 'C', 'D', 'F')

# List to store logged entries
log_entries = []

# Main loop for the program to run continuously
while True:
    # User interaction
    name = input("Please enter the student name: ")
    user_percent = input("Please enter the student's score (e.g., 90%): ")

    try:
        # Attempt to convert the user input to a float (assuming it's a valid number)
        user_percent = float(user_percent.strip('%'))

        # Check if the entered percentage is within a valid range (0-100)
        if 0 <= user_percent <= 100:
            # Calculate the letter grade
            if user_percent >= 90:
                letter_grade = lettergrade_tuple[0]
            elif user_percent >= 80:
                letter_grade = lettergrade_tuple[1]
            elif user_percent >= 70:
                letter_grade = lettergrade_tuple[2]
            elif user_percent >= 60:
                letter_grade = lettergrade_tuple[3]
            else:
                letter_grade = lettergrade_tuple[4]

            # Create a dictionary for the entry and append it to the log_entries list
            entry = {
                "Name": name,
                "Percentage": user_percent,
                "Letter Grade": letter_grade
            }
            log_entries.append(entry)

            print(f"{name} has a {user_percent}% which is a {letter_grade}.")

            # Ask the user if they want to continue or exit
            loop = input("Enter to continue, or press X to exit: ")
            if loop.lower() == 'x':
                exit(0)
        else:
            print("Please enter a valid score between 0% and 100%.")

    except ValueError:
        print("This is not a valid number. Please try again (e.g., 90%).")