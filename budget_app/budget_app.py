class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            amount = entry["amount"]
            description = entry["description"][:23]
            items += f"{description:<23}{amount:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)


def create_spend_chart(categories):
    # Step 1: Calculate spending for each category
    spending = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        spending.append(total)

    total_spent = sum(spending)
    percentages = [int((amount / total_spent) * 10) * 10 for amount in spending]  # rounded down to nearest 10

    # Step 2: Build the chart title
    chart = "Percentage spent by category\n"

    # Step 3: Build the bar graph
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    # Step 4: Add the horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"


    # Step 5: Build the category name labels (vertical)
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        line = "     "
        for category in categories:
            name = category.name
            line += f"{name[i] if i < len(name) else ' '}  "
        chart += line + "\n"  # keep spaces and newline

    return chart.rstrip("\n")  # remove final newline only
