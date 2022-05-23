# Уважаемые проверяющие!
# Прошу прощения!

# К настоящему моменту успел сделать лишь 2 из 4-х заданий по ООП!
# (при этом, сомневаюсь в правильности даже в этих 2-х)
# ООП идёт с большим трудом, особенно тяжело дается синтаксис!
# Направляю в целях выиграть время для доработки данного ДЗ по ООП.


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

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
        self.grades = {}


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
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']


best_student2 = Student('Ruoy2', 'Eman2', 'your_gender2')
best_student2.courses_in_progress += ['Git']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']


hard_reviewer = Reviewer('Some2', 'Buddy2')
hard_reviewer.courses_attached += ['Git']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Git', 8)


hard_reviewer.rate_hw(best_student2, 'Git', 5)
hard_reviewer.rate_hw(best_student2, 'Git', 8)

print(f'У студента {best_student.name} {best_student.surname} следующие оценки по курсу {best_student.grades}')

print(f'У студента {best_student2.name} {best_student2.surname} следующие оценки по курсу {best_student2.grades}')


best_lecturer = Lecturer('Some1', 'Buddy1')
best_lecturer.courses_attached += ['Git']

hard_student = Student('Ruoy1', 'Eman1', 'your_gender1')
hard_student.courses_in_progress += ['Git']

hard_student.rate_lect(best_lecturer,'Git', 7)
hard_student.rate_lect(best_lecturer,'Git', 10)
hard_student.rate_lect(best_lecturer,'Git', 8)


print(f'У лектора {best_lecturer.name} {best_lecturer.surname} студенты проставили следующие оценки по курсу {best_lecturer.grades}')