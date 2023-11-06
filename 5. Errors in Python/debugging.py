class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        avg_marks = sum(self.marks) / len(self.marks)
        print("avg_marks: ", avg_marks)

    def change_marks(self, index, new_mark):
        self.marks[index] = new_mark
        print("Marks Updated")


if __name__ == "__main__":
    student_one = Student("Om Priya", [100, 100, 100, 100, 100])
    student_one.get_avg()
    student_one.change_marks(2, 96)
