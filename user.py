import datetime
from expense import Expense


class User:
    def __init__(self):
        self.total_expenses = []

    def menu(self):
        while True:
            user_choice = input("---Welcome to Expense Management App---\n"
                                "1. Add expense\n"
                                "2. Calculate total expenses\n"
                                "3. Edit expense\n"
                                "4. Delete expense\n"
                                "5. Search expense\n"
                                "6. View all expense\n"
                                "7. Calculate total by Category\n"
                                "8. View all Categories\n")
            if user_choice == "1":
                print("---Add expense---")
                card_name = input("Enter card name: ").capitalize()
                title = input("Enter title: ").capitalize()
                expense_date_year = int(input("Enter expense date YEAR: "))
                expense_date_month = int(input("Enter expense date MONTH: "))
                expense_date_day = int(input("Enter expense date DAY: "))
                expense_date = datetime.date(expense_date_year, expense_date_month, expense_date_day)
                amount = float(input("Enter expense amount: "))
                category = input("Enter Category: ").capitalize()
                note = input("Enter note (optional): ").capitalize()
                tags = list(input("Enter tags (optional): "))

                expense = Expense(card_name, title, expense_date, amount, category, note, tags)

                self.total_expenses.append(expense)
            elif user_choice == "2":
                total = self.calculate_total()
                print(f"Total amount: {total}")
            elif user_choice == "3":
                pass
            elif user_choice == "4":
                search_id = int(input("Enter the ID of the expense you want to delete: "))

                self.delete_expense(search_id)
            elif user_choice == "5":
                self.search()
            elif user_choice == "6":
                print("---All Expenses---")
                self.view_all_expense()
            elif user_choice == "7":
                self.calculate_total_by_category()
            elif user_choice == "8":
                self.view_all_categories()
            else:
                print("Invalid choice!")

            user_choice = input("Do you want to continue? Yes (Y) or No (N): ")

            if user_choice == 'N' or user_choice == "n":
                print("Good bye!")
                break

    def add_expense(self, expense):
        self.total_expenses.append(expense)

    def calculate_total(self):
        total = 0
        for expense in self.total_expenses:
            total += expense.amount
        return total

    def edit_expense(self, search_id, **kwargs):
        found = False
        for expense in self.total_expenses:
            if expense.id == search_id:
                for key, value in kwargs.items():
                    if hasattr(expense, key):
                        setattr(expense, key, value)
                found = True
                break

        if found:
            print("Successfully updated!")
        else:
            print("Cannot find expense")

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
        for expense in self.total_expenses:
            print(expense)

    def view_all_categories(self):
        categories = {}
        for expense in self.total_expenses:
            if expense.category in categories:
                categories[expense.category] += 1
            else:
                categories[expense.category] = 1
        print("---All Categories---")
        for key in categories:
            print(f"{key}: {categories[key]}")

    def calculate_total_by_category(self):
        search_category = input("Enter the category you want to calculate: ").capitalize()
        found_expenses = []
        total = 0
        for expense in self.total_expenses:
            if expense.category == search_category:
                found_expenses.append(expense)

        if found_expenses:
            for e in found_expenses:
                total += e.amount
            print(f"Total amount of expense in {search_category} category is ${total}")
        else:
            print(f"Cannot find any expense in {search_category} category!")

    def search(self):
        user_input = int(input("What field do you want to search expense by?\n"
                               "1. ID\n"
                               "2. Category\n"
                               "3. Card Name\n"
                               "4. Date\n"
                               "5. Amount\n"
                               "6. Note\n"
                               "7. Tags\n"))
        if user_input == 1:
            search_id = int(input("Please enter the ID to look up: "))

            self._search_by_id(search_id=search_id)
        elif user_input == 2:
            search_category = input("Please enter the Category to look up: ").capitalize()

            self._search_by_category(category=search_category)
        elif user_input == 3:
            search_card_name = input("Please enter the Card name to look up: ").capitalize()

            self._search_by_card_name(card_name=search_card_name)
        elif user_input == 4:
            search_start_year = int(input("Please enter the starting year: "))
            search_start_month = int(input("Please enter the starting month: "))
            search_start_day = int(input("Please enter the starting day: "))
            search_start_date = datetime.date(search_start_year, search_start_month, search_start_day)

            search_end_year = int(input("Please enter the ending year: "))
            search_end_month = int(input("Please enter the ending month: "))
            search_end_day = int(input("Please enter the ending day: "))
            search_end_date = datetime.date(search_end_year, search_end_month, search_end_day)

            self._search_by_date(start_date=search_start_date, end_date=search_end_date)
        elif user_input == 5:
            search_start_amount = float(input("Please enter the starting amount: "))
            search_end_amount = float(input("Please enter the ending amount: "))

            self._search_by_amount(start_amount=search_start_amount, end_amount=search_end_amount)
        elif user_input == 6:
            search_tags = list(input("Please enter the tag to look up: "))
            self._search_by_tags(search_tags)
        else:
            print("Invalid choice!")

    def _search_by_id(self, search_id):
        found = False
        found_expense = None
        for expense in self.total_expenses:
            if expense.id == search_id:
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
            if expense.category == category.capitalize():
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
            if expense.card_name == card_name.capitalize():
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
            if expense.note == note.capitalize():
                found_expenses.append(expense)

        if found_expenses:
            print(f"Expenses with {note} note: ")
            for e in found_expenses:
                print(e)
        else:
            print(f"Cannot find any expense with {note} note")

    def _search_by_tags(self, tags:list):
        found_expenses = []
        for tag in tags:
            for expense in self.total_expenses:
                if tag in expense.tags:
                    found_expenses.append(expense)
        if found_expenses:
            print(f"Expenses with {tags} tags: ")
            for e in found_expenses:
                print(e)
        else:
            print(f"Cannot find any expense with {tags} tags")
