class Student:
    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, grade, course):
        if course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
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

    def __str__(self):
        average_grade = self.calculate_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {average_grade}"


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
      
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"          
          
# Пример использования
best_student = Student('Ruoy', 'Eman', 'your_gender', 19)
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Саша', 'Бражник', ['Python'])

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_lecturer = Lecturer('John', 'Doe', ['Python'])
best_lecturer.grades['Python'] = [9, 8, 7]


print(best_lecturer.grades)
print(best_student.grades)
print(cool_reviewer)
print(best_lecturer)