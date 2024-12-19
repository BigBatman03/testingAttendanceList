from ctypes import c_char_p
from datetime import datetime

import os
import csv

from managingList import managingListClass


class CheckAttendanceClass:
    def __init__(self):
        self.students = []
        self.date_text = ""
        self.attendance_list = []

    def saveAttendance(self, filename):
        fieldnames = ["name:", "surname:", "id:", "attendance:"]
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in self.attendance_list:
                writer.writerow(student)
        print(f"Saved attendance list to: {filename}")

    def addAttendance(self, name, surname, ids, attendance):
        student_attendance = {
            "name:": name,
            "surname:": surname,
            "id:": ids,
            "attendance:": attendance
        }
        self.attendance_list.append(student_attendance)
        print(
            f"Dodano obecność studenta: {name} {surname}, id studenta: {ids}")

    def addAndSavePresence(self, filename):
        while True:
            imp = managingListClass()
            self.students = imp.importFromFile(filename)
            print("1.Obecność")
            print("2.Zapis obecności do pliku")
            print("3.Wróć")
            choice = input("")
            if choice == "1":
                isDateGood = False
                while isDateGood == False:
                    self.date_text = input(
                        "Podaj date obecności: (yyyy.mm.dd)")
                    try:
                        isDateGood = True
                        date = datetime.strptime(
                            self.date_text, "%Y.%m.%d").date()
                    except ValueError:
                        isDateGood = False
                        print("Podano bledna wartosc!")
                    savefile = self.date_text
                    if os.path.isfile(f"Obecność_{savefile}.csv"):
                        isDateGood = False
                        print(
                            "Na ten dzień była już sprawdzona obecność. Edytuj obecność lub usuń plik z obecnością")
                    else:
                        isDateGood = True
                for student in self.students:
                    name = student["name:"]
                    surname = student["surname:"]
                    ids = student["id:"]
                    print(f"Czy {name} {surname} był obecny?")
                    isPresentOrNo = False
                    while isPresentOrNo == False:
                        attendance = input("y/n:")
                        if attendance == "y":
                            attendance = "Yes"
                            isPresentOrNo = True
                        elif attendance == "n":
                            attendance = "No"
                            isPresentOrNo = True
                    self.addAttendance(name, surname, ids, attendance)
            elif choice == "2":
                savefile = self.date_text
                if savefile == "":
                    print("Nie sprawdzono żadnej obecności")
                else:
                    self.saveAttendance(f"Obecność_{savefile}.csv")
            elif choice == "3":
                os.system("python AttendanceList.py")
            else:
                print("Zły wybór, spróbuj ponownie")
