import datetime


class Expense:
    last_id = 0

    def __init__(self, card_name: str, title: str, expense_date: datetime.date, amount: float, category: str,
                 expense_type: str, note="", tags=[]):
        Expense.last_id += 1  # Increment the last ID
        self.id = Expense.last_id  # Assign new ID to new Expense
        self.card_name = card_name
        self.title = title
        self.expense_date = expense_date
        self.amount = amount
        self.category = category
        self.expense_type = expense_type
        self.note = note
        self.tags = tags

    def __str__(self):
        tag_strings = []
        if self.tags:
            tag_strings = ", ". join(self.tags)
        return f"ID: {self.id}\n" \
               f"Card name: {self.card_name}\n" \
               f"Title: {self.title}\n" \
               f"Date: {str(self.expense_date)}\n" \
               f"Amount: {self.amount}\n" \
               f"Category: {self.category}\n" \
               f"Expense type: {self.expense_type}\n" \
               f"Notes: {self.note}\n" \
               f"Tags: {tag_strings}\n" \
               f"***"

