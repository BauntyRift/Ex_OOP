class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

      
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress  and course in lecturer.courses_attached:
            if course in lecturer.grades: 
                lecturer.grades[course] += [grade]    
            else:
                lecturer.grades[course] = [grade]
        else:
            print("Ошибка!")


    def calculate_average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        
        if len(total_grades) > 0:
            average_grade = sum(total_grades) / len(total_grades)
            return average_grade
        else:
            return 0
    

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return

        return self.calculate_average_grade() < other.calculate_average_grade()
         
    

    def __str__(self):
        average_grade = self.calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nПол: {self.gender} \nСредняя оценка за домашние задания: {average_grade} \nКурсы в процессе изучения:{courses_in_progress} \nЗавершенные курсы:{finished_courses}'
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
        self.grades = {}

    def calculate_average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        
        if len(total_grades) > 0:
            average_grade = sum(total_grades) / len(total_grades)
            return average_grade
        else:
            return 0
    

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return

        return self.calculate_average_grade() < other.calculate_average_grade()



    def __str__(self):
        average_grade = self.calculate_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}"


class Reviever(Mentor):
    pass

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res    


#  Student's-----------
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

good_student = Student('Гарри','Ньюман','мужчина')
good_student.courses_in_progress += ['Python']

# Revievers------------ 
cool_reviever = Reviever('Some', 'Buddy')
cool_reviever.courses_attached += ['Python']
 
cool_reviever.rate_hw(best_student, 'Python', 10)
cool_reviever.rate_hw(best_student, 'Python', 9)
cool_reviever.rate_hw(best_student, 'Python', 10)

cool_reviever.rate_hw(good_student, 'Python', 7)
cool_reviever.rate_hw(good_student, 'Python', 10)
cool_reviever.rate_hw(good_student, 'Python', 9)
# Lecturer's-----------
nice_lecturer = Lecturer('Джереми','Дамер')
nice_lecturer.courses_attached += ['Python']

lucky_lecturer = Lecturer('Габриэль','Агрест')
lucky_lecturer.courses_attached += ['Python']


best_student.rate_lecturer(nice_lecturer, 'Python', 10)
best_student.rate_lecturer(nice_lecturer, 'Python', 8)

good_student.rate_lecturer(lucky_lecturer, 'Python', 10)
good_student.rate_lecturer(lucky_lecturer, 'Python', 9)


print(best_student.grades)
print(nice_lecturer.grades)
print(best_student)
print("-")
print(cool_reviever)
print("-")
print(nice_lecturer)
print('---')
print("Средняя оценка good_student > best_student:",good_student > (best_student))
print("Средняя оценка nice_lecturer > lucky_lecturer:",nice_lecturer > (lucky_lecturer))
print("---")


students = [best_student, good_student]
lecturers = [nice_lecturer, lucky_lecturer]
course = "Python"

def calculate_average_grade_for_students(students, course):
    total_grades = []
    count = 0
    for student in students:
        if course in student.finished_courses or course in student.courses_in_progress:
            if course in student.grades:
                total_grades.extend(student.grades[course])
                count += 1
    if count > 0:
        average_grade = sum(total_grades) / len(total_grades)
        return average_grade
    else:
        return 0

def calculate_average_grade_for_lecturers(lecturers, course):
    total_grades = []
    count = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            if course in lecturer.grades:
                total_grades.extend(lecturer.grades[course])
                count += 1
    if count > 0:
        average_grade = sum(total_grades) / len(total_grades)
        return average_grade
    else:
        return 0
    

print(f"Средняя оценка за домашние задания по курсу {course}: {calculate_average_grade_for_students(students, course)}")
print(f"Средняя оценка за лекции всех лекторов по курсу {course}: {calculate_average_grade_for_lecturers(lecturers, course)}")
