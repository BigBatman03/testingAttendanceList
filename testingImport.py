import unittest
import os
import csv
from managingList import managingListClass

class TestManagingListImportFromFile(unittest.TestCase):
# TODO: test
    def setUp(self):
        self.manager = managingListClass()
        self.test_file = "test_students.csv"
        self.sample_data = [
            {"name:": "Alice", "surname:": "Smith", "id:": "1", "date:": "2023-01-01"},
            {"name:": "Bob", "surname:": "Brown", "id:": "2", "date:": "2023-01-02"}
        ]

        with open(self.test_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name:", "surname:", "id:", "date:"])
            writer.writeheader()
            writer.writerows(self.sample_data)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_import_from_file(self):
        result = self.manager.importFromFile(self.test_file)
        self.assertEqual(len(result), len(self.sample_data)) 
        self.assertEqual(result, self.sample_data) 

    def test_import_file_not_exists(self):
        non_existent_file = "non_existent_file.csv"
        result = self.manager.importFromFile(non_existent_file)
        self.assertEqual(result, [])
        

if __name__ == '__main__':
    unittest.main()
