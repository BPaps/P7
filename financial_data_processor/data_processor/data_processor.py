from typing import Any, Dict, List


class DataProcessor:
    """Processes data records to extract insights and perform analytics."""

    def __init__(self, data: List[Dict[str, Any]]):
        """
        Initialize the DataProcessor object.

        Args:
            data (List[Dict[str, Any]]): List of dictionaries representing records to be processed.
        """
        self.data = data
        self.account_summary = {
            'balance': 0,
            'total_deposits': 0,
            'total_withdrawals': 0
        }
        self._suspicious_transactions = []
        self._transaction_statistics = {
            'total_transactions': 0,
            'total_deposit_amount': 0,
            'total_withdrawal_amount': 0
        }

    def process_data(self):
        """
        Process the data records.

        This method iterates over the data records, updates account summary,
        checks for suspicious transactions, and updates transaction statistics.
        """
        for record in self.data:
            self._update_account_summary(record)
            self._check_suspicious_transactions(record)
            self._update_transaction_statistics(record)

    def _update_account_summary(self, record: Dict[str, Any]):
        """
        Update the account summary based on the given record.

        Args:
            record (Dict[str, Any]): Data record to be processed.
        """
        amount = record['Amount']
        transaction_type = record['Transaction type']
        if transaction_type == 'deposit':
            self.account_summary['balance'] += amount
            self.account_summary['total_deposits'] += amount
        elif transaction_type == 'withdrawal':
            self.account_summary['balance'] -= amount
            self.account_summary['total_withdrawals'] += amount

    def _check_suspicious_transactions(self, record: Dict[str, Any]):
        """
        Check for suspicious transactions based on predefined criteria.

        Args:
            record (Dict[str, Any]): Data record to be checked.
        """
        amount = record['Amount']
        currency = record['Currency']
        if amount > 10000:
            self._suspicious_transactions.append(record)
        if currency not in ['USD', 'EUR', 'GBP']:
            self._suspicious_transactions.append(record)

    def _update_transaction_statistics(self, record: Dict[str, Any]):
        """
        Update transaction statistics based on the given record.

        Args:
            record (Dict[str, Any]): Data record to be processed.
        """
        transaction_type = record['Transaction type']
        amount = record['Amount']
        self._transaction_statistics['total_transactions'] += 1
        if transaction_type == 'deposit':
            self._transaction_statistics['total_deposit_amount'] += amount
        elif transaction_type == 'withdrawal':
            self._transaction_statistics['total_withdrawal_amount'] += amount

    def get_average_transaction_amount(self):
        """
        Calculate the average transaction amount.

        Returns:
            Tuple[float, float]: Average deposit amount and average withdrawal amount.
        """
        num_deposits = self._transaction_statistics['total_deposit_amount']
        num_withdrawals = self._transaction_statistics['total_withdrawal_amount']
        num_transactions = self._transaction_statistics['total_transactions']

        avg_deposit = num_deposits / num_transactions if num_transactions else 0
        avg_withdrawal = num_withdrawals / num_transactions if num_transactions else 0

        return avg_deposit, avg_withdrawal