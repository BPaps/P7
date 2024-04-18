import unittest
from data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    INPUT_DATA = [
        {"Transaction ID": "1", "Account number": "1001", "Date": "2023-03-01",
         "Transaction type": "deposit", "Amount": 1000, "Currency": "CAD",
         "Description": "Salary"},
        {"Transaction ID": "2", "Account number": "1002", "Date": "2023-03-01",
         "Transaction type": "withdrawal", "Amount": 500, "Currency": "USD",
         "Description": "Rent"}
    ]

    def test_update_account_summary_deposit(self):
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor._update_account_summary(self.INPUT_DATA[0])
        self.assertEqual(data_processor.account_summary['total_deposits'], 1000)
        self.assertEqual(data_processor.account_summary['balance'], 1000)

    def test_update_account_summary_withdrawal(self):
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor._update_account_summary(self.INPUT_DATA[1])
        self.assertEqual(data_processor.account_summary['total_withdrawals'], 500)
        self.assertEqual(data_processor.account_summary['balance'], -500)

    def test_check_suspicious_transactions_large_amount(self):
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor._check_suspicious_transactions({"Amount": 20000, "Currency": "USD"})
        self.assertIn({"Amount": 20000, "Currency": "USD"}, data_processor._suspicious_transactions)

    def test_check_suspicious_transactions_uncommon_currency(self):
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor._check_suspicious_transactions({"Amount": 1000, "Currency": "JPY"})
        self.assertIn({"Amount": 1000, "Currency": "JPY"}, data_processor._suspicious_transactions)

    def test_update_transaction_statistics(self):
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor._update_transaction_statistics(self.INPUT_DATA[0])
        self.assertEqual(data_processor._transaction_statistics['total_transactions'], 1)
        self.assertEqual(data_processor._transaction_statistics['total_deposit_amount'], 1000)

    def test_get_average_transaction_amount(self):
        data_processor = DataProcessor(self.INPUT_DATA)
        data_processor._update_transaction_statistics(self.INPUT_DATA[0])
        data_processor._update_transaction_statistics(self.INPUT_DATA[1])
        avg_deposit, avg_withdrawal = data_processor.get_average_transaction_amount()
        self.assertEqual(avg_deposit, 1000)
        self.assertEqual(avg_withdrawal, 500)

if __name__ == '__main__':
    unittest.main()