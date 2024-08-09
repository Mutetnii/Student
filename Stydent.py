class Student:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    # Методы для установки и получения значений свойств
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade

    def get_average_grade(self):
        return self.average_grade

    # Метод для вывода информации о студенте
    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.average_grade}")

    # Метод для оценки студента на основе среднего балла
    def evaluate(self):
        if self.average_grade > 8:
            return "Отлично"
        elif 6 <= self.average_grade <= 8:
            return "Хорошо"
        elif 4 <= self.average_grade < 6:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

# Создание нескольких объектов класса "Студент"
student1 = Student("Вика", 20, 9.2)
student2 = Student("Иван", 21, 7.5)
student3 = Student("Саша", 22, 5.8)

# Демонстрация использования объектов
students = [student1, student2, student3]

for student in students:
    student.display_info()
    print(f"Оценка: {student.evaluate()}")
    print()

# Добавление дополнительных методов и свойств
class Student:
    def __init__(self, name, age, average_grade, major):
        self.name = name
        self.age = age
        self.average_grade = average_grade
        self.major = major  # Новое свойство - специальность

    # Методы для установки и получения значений свойств
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade

    def get_average_grade(self):
        return self.average_grade

    def set_major(self, major):
        self.major = major

    def get_major(self):
        return self.major

    # Метод для вывода информации о студенте
    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.average_grade}, Предмет: {self.major}")

    # Метод для оценки студента на основе среднего балла
    def evaluate(self):
        if self.average_grade > 8:
            return "Отлично"
        elif 6 <= self.average_grade <= 8:
            return "Хорошо"
        elif 4 <= self.average_grade < 6:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

# Создание нескольких объектов класса "Студент" с новой специальностью
student1 = Student("Вика", 20, 9.2, "Информатика")
student2 = Student("Иван", 21, 7.5, "Математика")
student3 = Student("Саша", 22, 5.8, "Физика")

# Демонстрация использования объектов
students = [student1, student2, student3]

for student in students:
    student.display_info()
    print(f"Оценка: {student.evaluate()}")
    print()


