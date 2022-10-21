class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def ave_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.ave_grade() < other.ave_grade()

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.ave_grade()}\n'
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                  f'Средняя оценка за лекции: {self.average_grade()}')
        return result

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return result

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

notbest_student = Student('John', 'Piters', 'male')
notbest_student.courses_in_progress += ['Python', 'Git']
notbest_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Lecturer', 'Buddy')
cool_lecturer.courses_attached += ['Python']

notcool_lecturer = Lecturer('Dic', 'Suver')
notcool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Bob', 'Reviewer')
cool_reviewer.courses_attached += ['Python']

notcool_reviewer = Reviewer('Maik', 'Reviewers')
notcool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)

cool_reviewer.rate_hw(notbest_student, 'Python', 8)
cool_reviewer.rate_hw(notbest_student, 'Python', 7)

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
notbest_student.rate_lecturer(notcool_lecturer, 'Python', 7)

student_list = [best_student, notbest_student]
lecturer_list = [cool_lecturer, notcool_lecturer]

student_grade_list = []
def average_grade_student(student_list, course):
    for student in student_list:
        for key, value in student.grades.items():
            if key is course:
                student_grade_list.extend(value)
    result = sum(student_grade_list) / len(student_grade_list)
    print(f'Средний бал по всем студентам курса {course}: {result}')

lecturer_grade_list = []
def average_grade_lecturer(lecturer_list, course):
    for lecturer in lecturer_list:
        for key, value in lecturer.grades.items():
            if key is course:
                lecturer_grade_list.extend(value)
    result = sum(lecturer_grade_list) / len(lecturer_grade_list)
    print(f'Средний бал за лекции всех лекторов курса {course}: {result}')

print(best_student)
print(notbest_student)
print(cool_lecturer)
print(notcool_lecturer)
print(cool_reviewer)
print(notcool_reviewer)

average_grade_student(student_list, 'Python')
average_grade_lecturer(lecturer_list, 'Python')
