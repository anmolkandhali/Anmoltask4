class StudentRecord:
    def __init__(self, student_name):
        self.student_name = student_name
        self.marks = []

    def insert_mark(self, mark):
        self.marks.append(mark)

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def convert_to_letter(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_summary(self):
        print(f"report for {self.student_name}:")
        print(f"Grades: {self.marks}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Letter Grade: {self.convert_to_letter()}")
        print()

record1 = StudentRecord("Kishan")
record2 = StudentRecord("Teja")

for mark in [85, 75, 65]:
    record1.insert_mark(mark)

for mark in [95, 85, 75]:
    record2.insert_mark(mark)

record1.display_summary()
record2.display_summary()