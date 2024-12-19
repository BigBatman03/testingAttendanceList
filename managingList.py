import csv
import os
# import pandas as pd
from setuptools.command.build_ext import if_dl


class managingListClass:

    def __init__(self):
        self.students = []

    def addStudent(self, name, surname, id, date):
        student = {
            "name:": name,
            "surname:": surname,
            "id:": id,
            "date:": date
        }
        self.students.append(student)
        print(f"\ndodano studenta: {name} {surname}, numer studenta: {id}")

    def checkIfCreated(self, filename):
        try:
            if os.path.isfile(filename):
                print(f"plik {filename} istnieje")
            else:
                fieldnames = ["name:", "surname:", "id:", "date:"]
                with open(filename, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                print(
                    f"Nie znaleziono bazy uczniów. \nPusty plik {filename} został utworzony.")
        except Exception as e:
            print(f"Błąd podczas tworzenia pliku: {e}")

    def importFromFile(self, fileName):
        if os.path.isfile(fileName):
            tempStudentList = []
            with open(fileName, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for student in reader:
                    tempStudentList.append(student)
                self.students = tempStudentList

            x = len(self.students)
            print(f"wczytano {x} studentow z listy")
        else:
            print(f"Plik nie istinieje")
        return self.students

    def importFromFile(self, filename):
        # Wczytuje listę studentów z pliku
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            return []

    def saveToFile(self, filename):
        # Wczytuje obecnych studentów z pliku, jeśli istnieją
        tempStudents = self.importFromFile(filename)

        # Tworzymy zbiór z ID obecnych studentów, aby łatwo sprawdzić duplikaty
        existing_ids = {student["id:"] for student in tempStudents}

        # Otwieramy plik do dopisywania nowych studentów
        fieldnames = ["name:", "surname:", "id:", "date:"]
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Przechodzimy przez listę `self.students` i zapisujemy tylko nowe
            # rekordy
            new_students = [
                student for student in self.students if student["id:"] not in existing_ids]

            if new_students:  # Sprawdzamy, czy są nowi studenci do zapisania
                writer.writerows(new_students)
                print(f"Saved {len(new_students)} new students to: {filename}")
            else:
                print("No new students to save.")

    def updateFile(self, filename):
        # Otwieramy plik w trybie 'w', co wyczyści plik i zapisuje nagłówek
        fieldnames = ["name:", "surname:", "id:", "date:"]
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

        # Zapisujemy wszystkich obecnych studentów z `self.students`
        for student in self.students:
            writer.writerow(student)
        print(f"Updated student list exported to: {filename}")

    # def deleteStudent(self, idToDelete, filename):
    #     try:
    #             df = pd.read_csv(filename)
    #             df = df[df["id:"] != int(idToDelete)]
    #             print(f"usuniecie : \n{df}")
    #             df.to_csv(filename, index=False)
    #     except Exception as e:
    #         print(Exception)
