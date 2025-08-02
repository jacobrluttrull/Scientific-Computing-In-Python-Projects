import unittest
from budget_app import Category, create_spend_chart

class TestBudgetApp(unittest.TestCase):

    def setUp(self):
        self.food = Category("Food")
        self.clothing = Category("Clothing")
        self.entertainment = Category("Entertainment")

    def test_deposit(self):
        self.food.deposit(100, "initial deposit")
        self.assertEqual(self.food.ledger[0], {"amount": 100, "description": "initial deposit"})

    def test_deposit_blank_description(self):
        self.food.deposit(50)
        self.assertEqual(self.food.ledger[0], {"amount": 50, "description": ""})

    def test_withdraw(self):
        self.food.deposit(100)
        self.food.withdraw(25.75, "groceries")
        self.assertEqual(self.food.ledger[1], {"amount": -25.75, "description": "groceries"})

    def test_withdraw_blank_description(self):
        self.food.deposit(100)
        self.food.withdraw(25.75)
        self.assertEqual(self.food.ledger[1], {"amount": -25.75, "description": ""})

    def test_withdraw_return_value(self):
        self.food.deposit(50)
        result = self.food.withdraw(20)
        self.assertTrue(result)

    def test_get_balance(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.assertAlmostEqual(self.food.get_balance(), 854.33)

    def test_transfer_creation_and_return(self):
        self.food.deposit(100)
        result = self.food.transfer(25, self.clothing)
        self.assertTrue(result)
        self.assertEqual(self.food.ledger[1]["description"], "Transfer to Clothing")
        self.assertEqual(self.clothing.ledger[0]["description"], "Transfer from Food")

    def test_transfer_balance_adjustment(self):
        self.food.deposit(100)
        self.food.transfer(30, self.clothing)
        self.assertAlmostEqual(self.food.get_balance(), 70)
        self.assertAlmostEqual(self.clothing.get_balance(), 30)

    def test_check_funds_false(self):
        self.assertFalse(self.food.check_funds(100))

    def test_check_funds_true(self):
        self.food.deposit(100)
        self.assertTrue(self.food.check_funds(50))

    def test_withdraw_insufficient_funds(self):
        result = self.food.withdraw(10)
        self.assertFalse(result)

    def test_transfer_insufficient_funds(self):
        result = self.food.transfer(50, self.clothing)
        self.assertFalse(result)


    def test_create_spend_chart(self):
        self.food.deposit(1000, "deposit")
        self.food.withdraw(150.00, "groceries")
        self.clothing.deposit(500, "deposit")
        self.clothing.withdraw(100, "clothes")
        self.entertainment.deposit(300, "deposit")
        self.entertainment.withdraw(200, "movies and games")
        chart = create_spend_chart([self.food, self.clothing, self.entertainment])

        # Remove this check, it assumes horizontal names
        # self.assertIn("Food", chart)

        # Just check chart starts correctly
        self.assertTrue(chart.startswith("Percentage spent by category"))


if __name__ == "__main__":
    unittest.main()
