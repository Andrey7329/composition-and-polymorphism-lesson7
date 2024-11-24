import json

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some sound"

    def eat(self):
        return f"{self.name} is eating."

# Подкласс Bird
class Bird(Animal):
    def make_sound(self):
        return "Чирик!"

# Подкласс Mammal
class Mammal(Animal):
    def make_sound(self):
        return "Рычит!"

# Подкласс Reptile
class Reptile(Animal):
    def make_sound(self):
        return "Шипит!"

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")

# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal} добавлено в зоопарк")

    def add_employee(self, newemployee):
        self.employees.append(newemployee)
        print(f"Сотрудник {newemployee} добавлен в зоопарк")

    def save_to_file(self, filename):
        data = {
            "animals": [{"name": animal.name, "age": animal.age, "type": animal.__class__.__name__} for animal in self.animals],
            "employees": [{"name": employee.name, "role": employee.role} for employee in self.employees]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for animal_data in data['animals']:
                if animal_data['type'] == 'Bird':
                    animal = Bird(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == 'Mammal':
                    animal = Mammal(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == 'Reptile':
                    animal = Reptile(animal_data['name'], animal_data['age'])
                self.add_animal(animal)

            for employee_data in data['employees']:
                if employee_data['role'] == 'ZooKeeper':
                    employee = ZooKeeper(employee_data['name'])
                elif employee_data['role'] == 'Veterinarian':
                    employee = Veterinarian(employee_data['name'])
                self.add_employee(employee)

# Класс для сотрудников зоопарка
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Подкласс ZooKeeper
class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

# Подкласс Veterinarian
class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


# Пример использования
if __name__ == "__main__":
    zoo = Zoo()

# Добавление животных
zoo.add_animal(Bird("Попугай", 2))
zoo.add_animal(Mammal("Лев", 5))
zoo.add_animal(Reptile("Змея", 3))

# Добавление сотрудников
zoo.add_employee(ZooKeeper("Джон"))
zoo.add_employee(Veterinarian("Доктор Смит"))

# Вызов функции полиморфизма
animal_sound(zoo.animals)

# Сохранение состояния зоопарка в файл
zoo.save_to_file("zoo_data.json")

# Загрузка состояния зоопарка из файла
new_zoo = Zoo()
new_zoo.load_from_file("zoo_data.json")
animal_sound(new_zoo.animals)