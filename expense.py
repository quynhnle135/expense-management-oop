from typing import Optional
import datetime


class Expense:
    last_id = 0

    def __init__(self, card_name: str, title: str, expense_date: datetime.date, amount: float, category: str,
                 note: Optional[str] = None):
        Expense.last_id += 1
        self.id = Expense.last_id
        self.card_name = card_name
        self.title = title
        self.expense_date = expense_date
        self.amount = amount
        self.category = category
        self.note = note

    def __str__(self):
        return f"ID: {self.id}\nCard name: {self.card_name}\nTitle: {self.title}\n" \
               f"Date: {str(self.expense_date)}\nAmount: {self.amount}\nCategory: {self.category}\n" \
               f"Notes: {self.note}\n***"
