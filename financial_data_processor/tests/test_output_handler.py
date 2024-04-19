import sys
from unittest import mock, TestCase
sys.path.append(r"C:\Users\abhay\Desktop\RRC_Polytech\Courses\COMP-1327_Software_Development_Fundamentals\Projects\assignment_07\P7\financial_data_processor")
from unittest.mock import patch, mock_open
import unittest
from output_handler.output_handler import OutputHandler

class TestOutputHandler(TestCase):
    ACCOUNT_SUMMARIES = { '1001': {'account_number': '1001', 'balance': 50, 
                            'total_deposits': 100, 'total_withdrawals': 50},
                            '1002': {'account_number': '2', 'balance': 200, 
                            'total_deposits': 200, 'total_withdrawals': 0}}
    
    SUSPICIOUS_TRANSACTIONS = [{"Transaction ID":"1" ,"Account number":"1001" ,
                            "Date":"2023-03-14" ,"Transaction type": "deposit",
                            "Amount":250,"Currency":"XRP","Description":"crypto investment"}  ]

    TRANSACTION_STATISTICS = {'deposit': {'total_amount': 300, 'transaction_count': 2}, 
                            'withdrawal': {'total_amount': 50, 'transaction_count': 1}}

    @patch('output_handler.output_handler.csv.writer')
    @patch('builtins.open', new_callable=mock_open)
    def test_write_account_summaries_to_csv(self, mock_open_file, mock_csv_writer):
        output_handler = OutputHandler(self.ACCOUNT_SUMMARIES, 
                                        self.SUSPICIOUS_TRANSACTIONS, 
                                        self.TRANSACTION_STATISTICS)
        output_handler.write_account_summaries_to_csv('test.csv')
        mock_open_file.assert_called_once_with('test.csv', 'w', newline='')
        mock_csv_writer.return_value.writerow.assert_called()

    @patch('output_handler.output_handler.csv.writer')
    @patch('builtins.open', new_callable=mock_open)
    def test_write_suspicious_transactions_to_csv(self, mock_open_file, mock_csv_writer):
        output_handler = OutputHandler(self.ACCOUNT_SUMMARIES, 
                                        self.SUSPICIOUS_TRANSACTIONS, 
                                        self.TRANSACTION_STATISTICS)
        output_handler.write_suspicious_transactions_to_csv('test.csv')
        mock_open_file.assert_called_once_with('test.csv', 'w', newline='')
        mock_csv_writer.return_value.writerow.assert_called()

    @patch('output_handler.output_handler.csv.writer')
    @patch('builtins.open', new_callable=mock_open)
    def test_write_transaction_statistics_to_csv(self, mock_open_file, mock_csv_writer):
        output_handler = OutputHandler(self.ACCOUNT_SUMMARIES, 
                                        self.SUSPICIOUS_TRANSACTIONS, 
                                        self.TRANSACTION_STATISTICS)
        output_handler.write_transaction_statistics_to_csv('test.csv')
        mock_open_file.assert_called_once_with('test.csv', 'w', newline='')
        mock_csv_writer.return_value.writerow.assert_called()

if __name__ == "__main__":
    unittest.main()
