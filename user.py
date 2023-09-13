import datetime
from expense import Expense


class User:
    def __init__(self):
        self.total_expenses = []

    def menu(self):
        while True:
            user_choice = self.get_menu_choice()
            self.process_choice(user_choice)

            cont = input("Do you want to continue? Yes (Y) or No (N): ").lower()
            if cont == 'n':
                print("Goodbye!")
                break

    def get_menu_choice(self) -> str:
        return input(
            "---Welcome to Expense Management App---\n"
            "1. Add expense\n"
            "2. Calculate total expenses\n"
            "3. Edit an expense\n"
            "4. Delete an expense\n"
            "5. Search an expense\n"
            "6. View all expenses\n"
            "7. Calculate total by category\n"
            "8. View all categories\n"
        )

    def process_choice(self, choice: str):
        if choice == "1":
            print("---Add expense---")
            card_name = input("Enter card name: ")
            title = input("Enter title: ")

            print("-Transaction date-")
            expense_date = self._get_date_from_user(prompt="Enter the expense")

            amount = float(input("Enter the expense amount: "))
            category = input("Enter category: ")
            note = input("Enter note (optional): ")

            expense = Expense(card_name, title, expense_date, amount, category, note)
            self.total_expenses.append(expense)

        elif choice == "2":
            print("---Calculate Total---")
            total = self.calculate_total()
            print(f"Total amount: {total}")

        elif choice == "3":
            print("---Edit an expense---")
            edit_id = input("Enter the expense ID you want to edit: ")
            self.edit_expense(search_id=edit_id)

        elif choice == "4":
            search_id = int(input("Enter the ID of the expense you want to delete: "))
            self.delete_expense(search_id)

        elif choice == "5":
            print("---Search---")
            self.search()

        elif choice == "6":
            print("---View all expenses---")
            self.view_all_expense()

        elif choice == "7":
            print("---Calculate total by category---")
            self.calculate_total_by_category()

        elif choice == "8":
            print("---View all categories---")
            self.view_all_categories()

        else:
            print("Invalid choice!")

    def add_expense(self, expense):
        self.total_expenses.append(expense)

    def calculate_total(self):
        total = 0
        for expense in self.total_expenses:
            total += expense.amount
        return total

    def edit_expense(self, search_id):
        # Search for expense by ID
        expense = self._find_expense_by_id(search_id)

        # Exit function if the expense is not found
        if expense is None:
            print("Invalid ID")
            return

        # Show editing options to the user
        edit_choice = self._get_edit_choice()

        # Apply the edit based on user's choice
        if self._apply_edit_to_expense(edit_choice, expense):
            print("Successfully edited!")
        else:
            print("Invalid choice")

    def _find_expense_by_id(self, search_id):
        for expense in self.total_expenses:
            if expense.id == int(search_id):
                return expense
        return None

    def _get_edit_choice(self):
        return input("What field do you want to edit?\n"
                     "1. Card name\n"
                     "2. Title\n"
                     "3. Expense date\n"
                     "4. Amount\n"
                     "5. Category\n"
                     "6. Note\n")

    def _apply_edit_to_expense(self, edit_choice, expense):
        if edit_choice == "1":
            new_card_name = input("Enter new card name: ")
            expense.card_name = new_card_name
            return True

        elif edit_choice == "2":
            new_title = input("Enter new title: ")
            expense.title = new_title
            return True

        elif edit_choice == "3":
            try:
                new_expense_date = self._get_date_from_user(prompt="Enter the expense")

                # Check if the entered date is in the future
                current_date = datetime.date.today()
                if new_expense_date > current_date:
                    print("The entered date cannot be in the future. Please try again.")
                    return False

                expense.expense_date = new_expense_date
                return True

            except ValueError:
                print("Invalid date entered. Please try again.")
                return False

        elif edit_choice == "4":
            new_amount = float(input("Enter new amount: "))
            expense.amount = new_amount
            return True

        elif edit_choice == "5":
            new_category = input("Enter new category: ")
            expense.category = new_category
            return True

        elif edit_choice == "6":
            new_note = input("Enter new note: ")
            expense.note = new_note
            return True

        return False

    def delete_expense(self, search_id):
        found = False
        for expense in self.total_expenses:
            if expense.id == search_id:
                self.total_expenses.remove(expense)
                found = True
                break

        if found:
            print("Successfully deleted!")
        else:
            print("Cannot find expense")

    def view_all_expense(self):
        if self.total_expenses:
            for expense in self.total_expenses:
                print(expense)
        else:
            print("No available expense.")

    def view_all_categories(self):
        categories = {}
        for expense in self.total_expenses:
            current_category = expense.category.lower()
            if current_category in categories:
                categories[current_category] += 1
            else:
                categories[current_category] = 1
        print("--- All Categories ---")
        for key in categories:
            if categories[key] < 2:
                print(f"{key}: {categories[key]} expense.")
            else:
                print(f"{key}: {categories[key]} expenses.")

    def calculate_total_by_category(self):
        search_category = input("Enter the category you want to calculate: ")
        found_expenses = []
        total = 0
        for expense in self.total_expenses:
            if expense.category.lower() == search_category.lower():
                found_expenses.append(expense)

        if found_expenses:
            for e in found_expenses:
                total += e.amount
            print(f"Total amount of expense in {search_category} category is ${total}")
        else:
            print(f"Cannot find any expense in {search_category} category.")

    def search(self):
        user_input = input("What field do you want to search expense by?\n"
                           "1. ID\n"
                           "2. Category\n"
                           "3. Card Name\n"
                           "4. Date\n"
                           "5. Amount\n"
                           "6. Note\n")

        if user_input == "1":
            print("- Search by ID -")
            search_id = input("Please enter the ID to look up: ")
            self._search_by_id(search_id=search_id)

        elif user_input == "2":
            print("- Search by category -")
            search_category = input("Please enter the category to look up: ")
            self._search_by_category(category=search_category)

        elif user_input == "3":
            print("- Search by card name -")
            search_card_name = input("Please enter the Card name to look up: ")
            self._search_by_card_name(card_name=search_card_name)

        elif user_input == "4":
            print("- Search by transaction date period -")
            try:
                search_start_date = self._get_date_from_user(prompt="Enter the starting")
                is_valid, message = self._validate_date(search_start_date)
                if not is_valid:
                    print(message)
                    return

                search_end_date = self._get_date_from_user(prompt="Enter the ending")
                is_valid, message = self._validate_date(search_end_date)
                if not is_valid:
                    print(message)
                    return

                # Validate that the start date is before or equal to the end date
                if search_start_date > search_end_date:
                    print("The start date must be before or equal to the end date. Please try again.")
                    return

                # Validate if the entered date is in the future
                current_date = datetime.date.today()
                if search_start_date > current_date or search_end_date > current_date:
                    print("The entered date cannot be in the future. Please try again.")
                    return

                self._search_by_date(start_date=search_start_date, end_date=search_end_date)

            except ValueError as e:
                print(f"An error occurred: {e}")
                print("Please enter a valid date.")

        elif user_input == "5":
            print("- Search by amount -")
            search_start_amount = float(input("Please enter the starting amount: "))
            search_end_amount = float(input("Please enter the ending amount: "))

            self._search_by_amount(start_amount=search_start_amount, end_amount=search_end_amount)

        elif user_input == "6":
            print("- Search by note - ")
            search_note = input("Enter search note: ")
            self._search_by_note(note=search_note)

        else:
            print("Invalid choice!")

    def _search_by_id(self, search_id):
        found = False
        found_expense = None
        for expense in self.total_expenses:
            if expense.id == int(search_id):
                found = True
                found_expense = expense
                break
        if found:
            print("Found the expense!")
            print(found_expense)
        else:
            print("Couldn't find the expense!")

    def _search_by_category(self, category):
        found_expenses = []
        for expense in self.total_expenses:
            if expense.category.lower() == category.lower():
                found_expenses.append(expense)

        if found_expenses:
            print(f"Expenses in {category} category: ")
            for e in found_expenses:
                print(e)
        else:
            print(f"Cannot find any expense in {category} category")

    def _search_by_card_name(self, card_name):
        found_expenses = []
        for expense in self.total_expenses:
            if expense.card_name.lower() == card_name.lower():
                found_expenses.append(expense)

        if found_expenses:
            print(f"Expenses with {card_name} card: ")
            for e in found_expenses:
                print(e)
        else:
            print(f"Cannot find any expense using {card_name} card")

    def _search_by_date(self, start_date: datetime.date, end_date: datetime.date):
        found_expenses = []
        for expense in self.total_expenses:
            if start_date <= expense.expense_date <= end_date:
                found_expenses.append(expense)

        if found_expenses:
            print(f"Expenses between {str(start_date)} - {str(end_date)}: ")
            for e in found_expenses:
                print(e)
        else:
            print(f"Cannot find any expense between {str(start_date)} - {str(end_date)}")

    def _search_by_amount(self, start_amount: float, end_amount: float):
        found_expenses = []
        for expense in self.total_expenses:
            if start_amount <= expense.amount <= end_amount:
                found_expenses.append(expense)

        if found_expenses:
            print(f"Expenses with amount in range {start_amount} - {end_amount}: ")
            for e in found_expenses:
                print(e)
        else:
            print(f"Cannot find any expenses in range {start_amount} - {end_amount}")

    def _search_by_note(self, note):
        found_expenses = []
        for expense in self.total_expenses:
            if expense.note.lower() == note.lower():
                found_expenses.append(expense)

        if found_expenses:
            print(f"Expenses with {note} note: ")
            for e in found_expenses:
                print(e)
        else:
            print(f"Cannot find any expense with {note} note")

    def _get_date_from_user(self, prompt):
        year = int(input(f"{prompt} YEAR: "))
        month = int(input(f"{prompt} MONTH: "))
        day = int(input(f"{prompt} DAY: "))

        return datetime.date(year, month, day)

    def _validate_date(self, date):
        if not (1 <= date.month <= 12) or not (1 <= date.day <= 31):
            return False, "Invalid month or day. Please try again."
        return True, ""
