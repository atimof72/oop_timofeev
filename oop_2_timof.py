class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def evaluat_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grade:
                lecturer.grade[course] += [grade]
            else:
                lecturer.grade[course] = [grade]
        else:
            return 'Ошибка. Что-то пошло не правильно.'

    def median_score(self):
        grade_list = []
        for verif in self.grades.values():
            for median_score in verif:
                grade_list.append(median_score)
        res = round(sum(grade_list) / len(grade_list), 2)
        return res

    # Магический метод оператора сравнения меньше <:
    def __lt__(self, other):
        return self.median_score() < other.median_score()

    # Магический метод __str__() — про объект класса для пользователей, по случаю здесь, для функции str.
    # А также применил join, ибо не знал как лучше иначе, a c join уже знаком.
    def __str__(self):
        res = f'Студент\n' \
              f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за ДЗ: {self.median_score()}\n' \
              f'Изучаемые курсы: {", ".join(self.courses_in_progress)} \n' \
              f'Пройденные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grade = {}

    def median_score(self):
        grade_list = []
        for verif in self.grade.values():
            for median_score in verif:
                grade_list.append(median_score)
        res = round(sum(grade_list) / len(grade_list), 2)
        return res

    # И опять магия, куда без неё)):
    def __lt__(self, other):
        return self.median_score() < other.median_score()

    def __str__(self):
        res = f'Преподаватель\n' \
              f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.median_score()}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка. Упс, что-то пошло не так.'

    def __str__(self):
        res = f'\nПроверяющий\n' \
              f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


def median_score_students(students_list, course_name):
    counter = 0
    score_sum = 0
    for student in students_list:
        if course_name in student.grades:
            counter += len(student.grades[course_name])
            score_sum += sum(student.grades[course_name])
    res = round((score_sum / counter), 2)
    return res


def median_score_lecturers(lecturers_list, course_name):
    counter = 0
    score_sum = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.grade:
            counter += len(lecturer.grade[course_name])
            score_sum += sum(lecturer.grade[course_name])
    res = round((score_sum / counter), 2)
    return res


student_succes = Student('Юлия', 'Тимофеева', 'female')
student_success_other = Student('Алексей', 'Тимофеев', 'male')
student_succes.courses_in_progress += ['Python', 'JavaScript']
student_succes.finished_courses += ['Git']
student_success_other.courses_in_progress += ['Python', 'JavaScript']
student_success_other.finished_courses += ['Git']

some_reviewer = Reviewer('Сергей', 'Петров')
other_review = Reviewer('Жанна', 'Стюардесова')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(student_succes, 'Python', 9)
some_reviewer.rate_hw(student_succes, 'Python', 8)
other_review.courses_attached += ['JavaScript', 'Python']
other_review.rate_hw(student_success_other, 'JavaScript', 7)
other_review.rate_hw(student_success_other, 'JavaScript', 8)

# control my code
# print(student_succes.grades, '\n')
# print(student_success_other.grades, '\n')

some_lecturer = Lecturer('Суши', 'Хатимович')
other_lecturer = Lecturer('Пицца', 'Жирная')
some_lecturer.courses_attached += ['JavaScript', 'Python']
other_lecturer.courses_attached += ['JavaScript', 'Python']
student_succes.evaluat_lecturers(some_lecturer, 'JavaScript', 5)
student_succes.evaluat_lecturers(some_lecturer, 'Python', 8)
student_succes.evaluat_lecturers(other_lecturer, 'JavaScript', 8)
student_succes.evaluat_lecturers(other_lecturer, 'Python', 7)
# control my code
# print(some_lecturer.grade, '\n')
# print(other_lecturer.grade, '\n')

print(some_reviewer, '\n')
print(some_lecturer, '\n')
print(student_succes, '\n')

# print(f'Проверющий:\n{some_reviewer}')
print(f'Есть другой проверяющий: {other_review}')
# print(other_lecturer, '\n')

print(f'\nЕсть другие студенты:\n{student_success_other} \n')

# control my code
# print(student_succes < student_success_other, '\n')
# print(some_lecturer < other_lecturer, '\n')

lecturers_list = [some_lecturer, other_lecturer]
students_list = [student_succes, student_success_other]

# control my code
# print(student_succes < student_success_other, '\n')
# print(some_lecturer < other_lecturer, '\n')

# control my code
# print(median_score_students(students_list, 'Python'))
# print(median_score_lecturers(lecturers_list, 'JavaScript'))

# намучался, конечно, но теперь код без явных ошибок
