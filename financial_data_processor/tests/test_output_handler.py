import sys
from unittest import mock
sys.path.append(r"C:\Users\abhay\Desktop\RRC_Polytech\Courses\COMP-1327_Software_Development_Fundamentals\Projects\assignment_07\P7\financial_data_processor")

import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open

from output_handler.output_handler import OutputHandler

class TestOutputHandler(TestCase):
    """The following constants have been provided to reduce the amount of 
    code needed when creating OutputHandler class objects in the tests that 
    follow.  To use the constants, prefix them with self.  Examples:
    self.ACCOUNT_SUMMARIES
    self.SUSPICIOUS_TRANSACTIONS
    self.TRANSACTION_STATISTICS
    e.g.:  output_handler = OutputHandler(self.ACCOUNT_SUMMARIES, 
                            self.SUSPICIOUS_TRANSACTIONS, self.TRANSACTION_STATISTICS)
    """

    ACCOUNT_SUMMARIES = { '1001': {'account_number': '1001', 'balance': 50, 
                            'total_deposits': 100, 'total_withdrawals': 50},
                            '1002': {'account_number': '2', 'balance': 200, 
                            'total_deposits': 200, 'total_withdrawals': 0}}
    
    SUSPICIOUS_TRANSACTIONS = [{"Transaction ID":"1" ,"Account number":"1001" ,
                            "Date":"2023-03-14" ,"Transaction type": "deposit",
                            "Amount":250,"Currency":"XRP","Description":"crypto investment"}  ]

    TRANSACTION_STATISTICS = {'deposit': {'total_amount': 300, 'transaction_count': 2}, 
                            'withdrawal': {'total_amount': 50, 'transaction_count': 1}}
        
    def test_filter_account_summaries_less_than(self):
        account_summaries = {'1001': {'account_number': '1001', 'balance': 50, 
                                      'total_deposits': 100, 'total_withdrawals': 50},
                            '1002': {'account_number': '1002', 'balance': 200, 
                                      'total_deposits': 200, 'total_withdrawals': 0}}
        expected_result = [{'account_number': '1001', 'balance': 50, 
                            'total_deposits': 100, 'total_withdrawals': 50}]
        output_handler = OutputHandler(account_summaries, [], {})
        filtered_data = output_handler.filter_account_summaries('balance', 100, False)
        self.assertEqual(filtered_data, expected_result)

    def test_filter_account_summaries_greater_than(self):
        account_summaries = {'1001': {'account_number': '1001', 'balance': 50, 
                                      'total_deposits': 100, 'total_withdrawals': 50},
                            '1002': {'account_number': '1002', 'balance': 200, 
                                      'total_deposits': 200, 'total_withdrawals': 0}}
        expected_result = [{'account_number': '1002', 'balance': 200, 
                            'total_deposits': 200, 'total_withdrawals': 0}]
        output_handler = OutputHandler(account_summaries, [], {})
        filtered_data = output_handler.filter_account_summaries('balance', 100, True)
        self.assertEqual(filtered_data, expected_result)

    def test_write_filtered_summaries_to_csv(self):
         # Mocking the csv.writer and open function
        with mock.patch('output_handler.output_handler.csv.writer'), \
             mock.patch('builtins.open', mock.mock_open()):
             account_summaries = {'1001': {'account_number': '1001', 'balance': 50, 
                                      'total_deposits': 100, 'total_withdrawals': 50}}
        output_handler = OutputHandler(account_summaries, [], {})
        filtered_data = [{'account_number': '1001', 'balance': 50, 
                          'total_deposits': 100, 'total_withdrawals': 50}]
        output_handler.write_filtered_summaries_to_csv(filtered_data, 'test.csv')




if __name__ == "__main__":
    unittest.main()