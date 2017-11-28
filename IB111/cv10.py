class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2*self.x +2*self.y

    def __str__(self):
        return 'Rectangle a=' + str(self.x) + ' b=' + str(self.y)

    def paint(self, symbol):
        for _ in range(self.x):
            for _ in range(self.y):
                print(symbol, end='')
            print()

# r = Rectangle(10, 20)
# print(r.area())
# print(r.perimeter())
# print(r)
# # r.paint('#')


class Student:
    def __init__(self, name, uco):
        self.name = name
        self.uco = uco
        self.points = {}

    def add_points(self, course, points):
        self.points[course] = points


class Course:
    def __init__(self, code, credit):
        self.code = code
        self.students = []
        self.credit = credit

    def add_student(self, student):
        self.students.append(student)

    def add_points_to_student(self, student, points):
        student.add_points(self, points)

    def print_students(self):
        for i in range(len(self.students)):
            print(self.students[i].name, self.students[i].points[self])

    def sort_students(self, how):
        if how == 'byname':
            self.students = sorted(self.students, key=lambda student: student.name)
        elif how == 'byuco':
            self.students = sorted(self.students, key=lambda student: student.uco)
        elif how == 'bypoints':
            self.students = sorted(self.students, key=lambda student: student.points)


def check_student(student, credit):
    actual_credit = 0
    for course in student.points:
        if student.points[course] >= 50:
            actual_credit += course.credit
    return actual_credit >= credit


programko = Course(123, 5)
jurko = Student('Benicek', 410089)
danka = Student('Grofova', 410080)
programko.add_student(danka)
programko.add_student(jurko)
programko.add_points_to_student(jurko, 10)
programko.add_points_to_student(danka, 55)
programko.sort_students('byuco')
programko.print_students()

print(check_student(danka, 2))
print(check_student(jurko, 2))

