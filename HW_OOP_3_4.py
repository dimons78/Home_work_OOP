
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


    def midd(self, dict_):
        dict_middle = dict()
        for i in dict_:
            sum_elem = 0
            for j in dict_[i]:
                sum_elem += j
            if len(dict_[i]) == 0:
                dict_middle[i] = 'Нет оценок'
            else:
                dict_middle[i] = sum_elem / len(dict_[i])
        return dict_middle

    # def __str__(self):
    #     res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
    #           f'{self.midd(self.grades)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
    #           f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
    #     return res

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}')
        for i, j in self.midd(self.grades).items():
            print(f'Средняя оценка за домашние задания по курсу {i} составляет: {j}')
        print(f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
              f'Завершенные курсы: {", ".join(self.finished_courses)}')
        res = ''
        return res


    def __lt__(self, other):
        j_sum_self, num_self = 0, 0
        j_sum_other, num_other = 0, 0
        if not isinstance(other, Student):
            print('Not')
            return
        for i, j in self.midd(self.grades).items():
            # print(f'Средняя оценка за ДЗ по курсу {i} составляет: {j}')
            for i_, j_ in self.midd(other.grades).items():
                # print(f'Средняя оценка за ДЗ по курсу {i_} составляет: {j_}')
                if i == i_:
                    if j > j_:
                        print(f'У студента {self.name} {self.surname} по курсу {i} cредняя оценка за ДЗ ({j}) выше, чем'
                            f' у студента {other.name} {other.surname} ({j_})')
                    elif j < j_:
                        print(f'У студента {self.name} {self.surname} по курсу {i} cредняя оценка за ДЗ ({j}) ниже, чем'
                            f' у студента {other.name} {other.surname} ({j_})')
                    else:
                        print(f'Cредняя оценка по курсу {i} у студентов одинакова ({j})')
        res = ''
        return res



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def midd(self, dict_):
        dict_middle = dict()
        for i in dict_:
            sum_elem = 0
            for j in dict_[i]:
                sum_elem += j
            if len(dict_[i]) == 0:
                dict_middle[i] = 'Нет оценок'
            else:
                dict_middle[i] = sum_elem / len(dict_[i])
        return dict_middle

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        for i, j in self.midd(self.grades).items():
            print(f'Средняя оценка за лекции по курсу {i} составляет: {j}')
        res = ''
        return res

    def __lt__(self, other):
        j_sum_self, num_self = 0, 0
        j_sum_other, num_other = 0, 0
        if not isinstance(other, Lecturer):
            print('Not')
            return
        for i, j in self.midd(self.grades).items():
            # print(f'Средняя оценка за лекции по курсу {i} составляет: {j}')
            for i_, j_ in self.midd(other.grades).items():
                # print(f'Средняя оценка за лекции по курсу {i_} составляет: {j_}')
                if i == i_:
                    if j > j_:
                        print(f'У лектора {self.name} {self.surname} по курсу {i} cредняя оценка за лекции ({j}) выше, чем'
                              f' у лектора {other.name} {other.surname} ({j_})')
                    elif j < j_:
                        print(f'У лектора {self.name} {self.surname} по курсу {i} cредняя оценка за лекции ({j}) ниже, чем'
                              f' у лектора {other.name} {other.surname} ({j_})')
                    else:
                        print(f'Cредняя оценка по курсу {i} у лекторов одинакова ({j})')
        res = ''
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'








best_student = Student('Ruoy', 'Eman', 'boy')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование', 'C++']


best_student2 = Student('Ruoy2', 'Eman2', 'boy')
best_student2.courses_in_progress += ['Git']
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['Введение в программирование']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']

hard_reviewer = Reviewer('Some2', 'Buddy2')
hard_reviewer.courses_attached += ['Git']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(best_student, 'Git', 7)
cool_reviewer.rate_hw(best_student, 'Git', 10)

cool_reviewer.rate_hw(best_student2, 'Python', 9)
cool_reviewer.rate_hw(best_student2, 'Python', 8)
cool_reviewer.rate_hw(best_student2, 'Python', 8)
cool_reviewer.rate_hw(best_student2, 'Git', 8)
cool_reviewer.rate_hw(best_student2, 'Git', 9)
cool_reviewer.rate_hw(best_student2, 'Git', 7)
cool_reviewer.rate_hw(best_student2, 'Git', 7)

hard_reviewer.rate_hw(best_student, 'Git', 9)
hard_reviewer.rate_hw(best_student, 'Git', 5)
hard_reviewer.rate_hw(best_student, 'Git', 8)
hard_reviewer.rate_hw(best_student, 'Git', 9)
hard_reviewer.rate_hw(best_student, 'Git', 8)

hard_reviewer.rate_hw(best_student2, 'Git', 8)
hard_reviewer.rate_hw(best_student2, 'Git', 9)
hard_reviewer.rate_hw(best_student2, 'Git', 9)

print(f'У студента {best_student.name} {best_student.surname} следующие оценки по курсу {best_student.grades}')

print(f'У студента {best_student2.name} {best_student2.surname} следующие оценки по курсу {best_student2.grades}')


best_lecturer = Lecturer('Some1', 'Buddy1')
best_lecturer.courses_attached += ['Git']

hard_student = Student('Ruoy1', 'Eman1', 'your_gender1')
hard_student.courses_in_progress += ['Git','Python']

hard_student.rate_lect(best_lecturer,'Git', 7)
hard_student.rate_lect(best_lecturer,'Git', 10)
hard_student.rate_lect(best_lecturer,'Git', 8)


hard_student2 = Student('Ruoy2', 'Eman2', 'your_gender1')
hard_student2.courses_in_progress += ['C++']

hard_student2.rate_lect(best_lecturer,'C++', 3)
hard_student2.rate_lect(best_lecturer,'C++', 7)
hard_student2.rate_lect(best_lecturer,'C++', 4)


print(f'У лектора {best_lecturer.name} {best_lecturer.surname} студенты '
      f'проставили следующие оценки по курсу {best_lecturer.grades}')
print()
print('У проверяющих - reviewer выводим информацию в следующем виде:')
print(cool_reviewer)
print()
print(hard_reviewer)



best_lecturer.courses_attached += ['Python']
hard_student.rate_lect(best_lecturer,'Git', 6)
hard_student.rate_lect(best_lecturer,'Git', 10)
hard_student.rate_lect(best_lecturer,'Git', 3)
hard_student.rate_lect(best_lecturer,'Python', 4)
hard_student.rate_lect(best_lecturer,'Python', 4)
hard_student.rate_lect(best_lecturer,'Python', 6)
hard_student.rate_lect(best_lecturer,'Python', 7)



some_lecturer = Lecturer('Some32', 'Buddy32')
some_lecturer.courses_attached += ['Python']
hard_student.rate_lect(some_lecturer,'Git', 7)
hard_student.rate_lect(some_lecturer,'Git', 9)
hard_student.rate_lect(some_lecturer,'Git', 8)
hard_student.rate_lect(some_lecturer,'Python', 5)
hard_student.rate_lect(some_lecturer,'Python', 1)
hard_student.rate_lect(some_lecturer,'Python', 1)
hard_student.rate_lect(some_lecturer,'Python', 9)


print()
print('У лекторов:')
print(f'У лектора {some_lecturer.name} {some_lecturer.surname} студенты '
      f'проставили следующие оценки по курсу {some_lecturer.grades}')
print(some_lecturer)

print()
print('А у студентов так:')
print(f'У студента {best_student.name} {best_student.surname} следующие оценки по курсу {best_student.grades}')
print()
print(best_student)
print()

print(f'У студента {best_student2.name} {best_student2.surname} следующие оценки по курсу {best_student2.grades}')
print()
print(best_student2)


print()
print('Сравниваем лекторов по средней оценке за лекции:')

print(some_lecturer < best_lecturer)

# print(some_lecturer > best_lecturer)
# print(some_lecturer == best_lecturer)

# print()
# print(best_student.__dict__)
# print()
# print(best_student2.__dict__)
# print()
# print(cool_reviewer.__dict__)
# print()
# print(hard_reviewer.__dict__)
# print()
# print(hard_student.__dict__)
# print()
# print(hard_student2.__dict__)
# print()
# print(best_lecturer.__dict__)
# print()
# print(some_lecturer.__dict__)
# print(best_lecturer)

print()
print('Сравниваем студентов по средней оценке за домашние задания:')
print()
print(best_student < best_student2)

# функция	для подсчета средней оценки за домашние задания по всем студентам
# в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса)
def middle_HW(list_student, course):
    i_sum, num_i = 0, 0
    for i in list_student:
        print(i.grades)
        for i_, j_ in i.grades.items():
            # print(i_)
            # print(course)
            # print(j_)
            if i_ == course:
                # print(sum(j_))
                i_sum += sum(j_)
                num_i += len(j_)
                # print(sum(j_))
    if num_i == 0:
        print('Нет данных для расчета средней оценки за ДЗ\n')
    else:
        print(f'Средняя оценка за ДЗ по всем студентам в рамках курса "{course}": {i_sum/num_i}\n')


list_student = [best_student, best_student2]
middle_HW(list_student, 'Git')


# функция для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса)
def middle_lect(list_lect, course):
    i_sum, num_i = 0, 0
    for i in list_lect:
        print(i.grades)
        for i_, j_ in i.grades.items():
            # print(i_)
            # print(course)
            # print(j_)
            if i_ == course:
                # print(sum(j_))
                i_sum += sum(j_)
                num_i += len(j_)
                # print(sum(j_))
    if num_i == 0:
        print('Нет данных для расчета средней оценки за лекции\n')
    else:
        print(f'Средняя оценка за лекции всех лекторов в рамках курса "{course}": {i_sum/num_i}\n')


list_lect = [some_lecturer, best_lecturer]
middle_lect(list_lect, 'C++')

