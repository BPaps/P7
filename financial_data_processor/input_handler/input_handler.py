import csv
import json
from typing import List, Dict

class InputHandler:
    """
    Class to handle input data from CSV or JSON files.
    """

    def __init__(self, file_path: str):
        """
        Initialize InputHandler with the file path.
        
        Args:
            file_path (str): The path to the input file.
        """
        self.__file_path = file_path

    @property
    def file_path(self) -> str:
        """
        Get the file path.

        Returns:
            str: The file path.
        """
        return self.__file_path

    def get_file_format(self) -> str:
        """
        Get the file format of the input file.

        Returns:
            str: The file format (e.g., 'csv', 'json').
        """
        return self.__file_path.split('.')[-1]

    def read_input_data(self) -> List[Dict]:
        """
        Read input data from the file.
        
        Returns:
            list: A list of dictionaries containing the input data.
        """
        data = []
        file_format = self.get_file_format()
        if file_format == 'csv':
            data = self.read_csv_data()
        elif file_format == 'json':
            data = self.read_json_data()
        return data

    def read_csv_data(self) -> List[Dict]:
        """
        Read data from a CSV file.
        
        Returns:
            list: A list of dictionaries containing the CSV data.
        
        Raises:
            FileNotFoundError: If the file does not exist.
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

    def read_json_data(self) -> List[Dict]:
        """
        Read data from a JSON file.
        
        Returns:
            list: A list of dictionaries containing the JSON data.
        
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(self.__file_path, 'r') as input_file:
                input_data = json.load(input_file)
            return input_data
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")
