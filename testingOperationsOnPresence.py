import unittest
import os
import csv
# TODO: F401 [*] `unittest.mock.patch` imported but unused, help: Remove unused import: `unittest.mock.patch`
# Issue URL: https://github.com/BigBatman03/testingAttendanceList/issues/3
from unittest.mock import patch
from check_attendance import CheckAttendanceClass
from managingList import managingListClass

class TestAttendance(unittest.TestCase):

    def setUp(self):
        self.attendance_checker = CheckAttendanceClass()
        self.managing_list = managingListClass()
        self.managing_list.addStudent("John", "Doe", "123", "2023-01-01")
        self.managing_list.addStudent("Jane", "Smith", "124", "2023-02-01")
        self.attendance_checker.students = self.managing_list.students
    
    def test_add_attendance(self):
        self.attendance_checker.addAttendance("John", "Doe", "123", "Yes")
        self.attendance_checker.addAttendance("Jane", "Smith", "124", "No")
     
        self.assertEqual(len(self.attendance_checker.attendance_list), 2)
        self.assertEqual(self.attendance_checker.attendance_list[0]["name:"], "John")
        self.assertEqual(self.attendance_checker.attendance_list[0]["attendance:"], "Yes")
        self.assertEqual(self.attendance_checker.attendance_list[1]["name:"], "Jane")
        self.assertEqual(self.attendance_checker.attendance_list[1]["attendance:"], "No")

    def test_save_attendance(self):
        self.attendance_checker.addAttendance("John", "Doe", "123", "Yes")
        self.attendance_checker.addAttendance("Jane", "Smith", "124", "No")
        filename = "test_attendance.csv"
        self.attendance_checker.saveAttendance(filename)

        self.assertTrue(os.path.isfile(filename))

        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["name:"], "John")
            self.assertEqual(rows[0]["surname:"], "Doe")
            self.assertEqual(rows[0]["id:"], "123")
            self.assertEqual(rows[0]["attendance:"], "Yes")
            self.assertEqual(rows[1]["name:"], "Jane")
            self.assertEqual(rows[1]["surname:"], "Smith")
            self.assertEqual(rows[1]["id:"], "124")
            self.assertEqual(rows[1]["attendance:"], "No")
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
