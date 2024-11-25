import unittest
import os
import csv
from managingList import managingListClass

class TestSaveToFile(unittest.TestCase):

    def setUp(self):
        self.manager = managingListClass()
        self.test_file = "test_students.csv"
        self.default_students = [
            {"name:": "Alice", "surname:": "Brown", "id:": "125", "date:": "2023-11-01"},
            {"name:": "John", "surname:": "Doe", "id:": "123", "date:": "2023-11-02"},
        ]

        with open(self.test_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name:", "surname:", "id:", "date:"])
            writer.writeheader()
            writer.writerows(self.default_students)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_to_empty_file(self):
        os.remove(self.test_file)
        self.manager.students = self.default_students
        self.manager.saveToFile(self.test_file)

        with open(self.test_file, mode='r', newline='', encoding='utf-8') as file:
            reader = list(csv.DictReader(file))
            self.assertEqual(len(reader)+1, len(self.default_students)) 

    def test_avoid_duplicates(self):
        self.manager.students = [self.default_students[0]]
        self.manager.saveToFile(self.test_file)

        with open(self.test_file, mode='r', newline='', encoding='utf-8') as file:
            reader = list(csv.DictReader(file))
            ids = [row["id:"] for row in reader]
            self.assertEqual(ids.count("125"), 1)

    def test_file_format(self):
        self.manager.students = self.default_students
        self.manager.saveToFile(self.test_file)

        with open(self.test_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.assertEqual(reader.fieldnames, ["name:", "surname:", "id:", "date:"])

if __name__ == "__main__":
    unittest.main()
