import unittest
import os
import csv
from managingList import managingListClass

class TestStudentOperations(unittest.TestCase):

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

    def test_add_student(self):
        self.manager.addStudent("Jane", "Smith", "126", "2023-11-03")
        self.assertEqual(len(self.manager.students), 1)
        self.assertEqual(self.manager.students[0]["name:"], "Jane")
        self.assertEqual(self.manager.students[0]["id:"], "126")

    def test_add_student_with_duplicate_id(self):
        self.manager.students = self.default_students
        self.manager.addStudent("Jane", "Smith", "126", "2023-11-03")
        self.assertEqual(len(self.manager.students), len(self.default_students))
    
if __name__ == "__main__":
    unittest.main()