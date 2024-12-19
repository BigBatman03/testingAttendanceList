from operator import attrgetter
import csv


from managingList import managingListClass


class AttendanceDataClass:

    def __init__(self):
        """
        :param student_list: list of dictionaries with student data
        """
        self.students = []
        self.date_text = ""
        self.attendance_list = []

    def editPresence(self, filenameDate):
        imp = managingListClass()
        self.attendance_list = imp.importFromFile(filenameDate)
        for student in self.attendance_list:
            name = student["name:"]
            surname = student["surname:"]
            attendance = student["attendance:"]
            print(f"{name} {surname} - czy był obecny: ({attendance})")
            isPresentOrNo = False
            while isPresentOrNo == False:
                attendance = input("czy był obecny? y/n: ")
                if attendance == "y":
                    attendance = "Yes"
                    isPresentOrNo = True
                elif attendance == "n":
                    attendance = "No"
                    isPresentOrNo = True
                student["attendance:"] = attendance
        self.updateFile(filenameDate)

    def updateFile(self, fileNameDate):
        # Otwieramy plik w trybie 'w', co wyczyści plik i zapisuje nagłówek
        fieldnames = ["name:", "surname:", "id:", "attendance:"]
        with open(fileNameDate, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        # Zapisujemy wszystkich obecnych studentów z `self.students`
            for student in self.attendance_list:
                writer.writerow(student)
        print(f"Updated student list exported to: {fileNameDate}")
