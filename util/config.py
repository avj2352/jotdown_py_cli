"""
All about JSON file handling
"""
import json
import jsonpickle
import os
import unittest
from unittest.mock import patch, mock_open
from typing import Optional, List

from models.file_data import FileData
from models.todo import Todo

DB_JSON_FILE: str = ".jotdown-db.json"

"""
initialize mode if file is newly created
"""


# check if file exists, return bool True or False
def create_file_if_not_exists() -> bool:
    if not os.path.exists(DB_JSON_FILE):
        try:
            with open(DB_JSON_FILE, 'w') as f:
                json.dump({}, f)
                return True
        except IOError as err:
            print(f"Error creating file: {err}")
            return False
    else:
        print(f"Reading {DB_JSON_FILE}, parsing data...")
        return True


# check if file contains data
def parse_file() -> Optional[dict]:
    try:
        with open(DB_JSON_FILE, "r") as f:
            # read entire file contents
            data_str = f.read()
            # parse json string into python dict
            data = json.loads(data_str)
            if data_str is None or data_str == "{}":
                return None
            return data
    except FileNotFoundError as e:
        print(f"Error: Reading file {DB_JSON_FILE} not found - {e}.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON data in {DB_JSON_FILE} - {e}.")
        return None


# write todo list to file
def write_todo_list_to_file(data_list: List[Todo]):
    try:
        with open(DB_JSON_FILE, "w") as f:
            # convert dataclass to json_data
            file_data = FileData(todos=data_list)
            json_data = jsonpickle.encode(file_data, unpicklable=False)
            f.write(json_data)
    except FileNotFoundError as e:
        print(f"Error: Writing to file {DB_JSON_FILE} - {e}")
    except Exception as e:
        print(f"Error: converting to json and writing to file {DB_JSON_FILE} - {e}")


"""
TESTING
"""


class TestCreateFileIfNotExists(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    def test_create_file_success(self, _, mock_open):
        # Test case for when the file does not exist
        result = create_file_if_not_exists()

        # Check that the file creation attempt was made
        mock_open.assert_called_once_with(DB_JSON_FILE, 'w')
        handle = mock_open()
        handle.write.assert_called_once_with(json.dumps({}))

        # Assert the return value is True
        self.assertTrue(result)

    @patch('os.path.exists', return_value=True)
    def test_file_exists(self, _):
        # Test case for when the file already exists
        result = create_file_if_not_exists()

        # Assert the function returns True without attempting to create the file
        self.assertTrue(result)

    @patch('builtins.open', side_effect=IOError("Mocked IOError"))
    @patch('os.path.exists', return_value=False)
    def test_create_file_io_error(self, _, mock_open):
        # Test case for IOError during file creation
        result = create_file_if_not_exists()

        # Assert the function returns False on IOError
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
