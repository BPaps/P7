import csv
import json

class InputHandler:
    """
    Class for handling input data.
    """

    def __init__(self, file_path: str):
        """
        Initialize InputHandler with the file path.
        """
        self.__file_path = file_path

    @property
    def file_path(self):
        """
        Get the file path.
        """
        return self.__file_path

    def get_file_format(self) -> str:
        """
        Get the file format.
        """
        return self.__file_path.split('.')[-1]

    def read_input_data(self) -> list:
        """
        Read input data.
        """
        data = []
        file_format = self.get_file_format()
        if file_format == 'csv':
            data = self.read_csv_data()
        elif file_format == 'json':
            data = self.read_json_data()
        return data

    def read_csv_data(self) -> list:
        """
        Read data from a CSV file.
        """
        input_data = []
        try:
            with open(self.__file_path, 'r') as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    input_data.append(row)
            return input_data
        
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

    def read_json_data(self) -> list:
        """
        Read data from a JSON file.
        """
        try:
            with open(self.__file_path, 'r') as input_file:
                input_data = json.load(input_file)
            return input_data
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

    def data_validation(self, data: list) -> list:
        """
        Validate input data.
        """
        valid_data = []
        for record in data:
            if self.validate_amount(record['Amount']) and self.validate_transaction_type(record['Transaction type']):
                valid_data.append(record)
        return valid_data

    def validate_amount(self, amount: str) -> bool:
        """
        Validate the amount field.
        """
        try:
            amount_float = float(amount)
            if amount_float >= 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_transaction_type(self, transaction_type: str) -> bool:
        """
        Validate the transaction type field.
        """
        valid_types = ['deposit', 'withdrawal', 'transfer']
        if transaction_type.lower() in valid_types:
            return True
        else:
            return False
