"""
Herencia y polimorfismo
"""

class Animal:
    
    def __init__(self, name: str):      # Este metodo inicilizador es heredado en todas las subclases
        self.name = name
    
    def sound(self):
        print("Animal")
    
class Dog(Animal):      # Al poner "Animal" como parament
    
    def sound(self):
        print("Guau")

class Cat(Animal):
    
    def sound(self):
        print("Miau")
        
def print_sound(animal: Animal):
    animal.sound()
    
my_dog = Dog("Perro")
print_sound(my_dog)
        
# my_animal = Animal("Animal")
# my_animal.sound()
# my_dog = Dog("Perro")
# my_dog.sound()
# my_cat = Cat("Gato")
# my_cat.sound()

"""
Desafio extra
"""
# Definición de la clase Employee, que será la clase base
class Employee:
    
    # Constructor de la clase Employee
    # Toma como argumentos un ID (int) y un nombre (str)
    # Se inicializa también una lista vacía para almacenar otros empleados a cargo
    def __init__(self, id: int, name: str) -> None:
        self.id = id  # Asigna el ID al empleado
        self.name = name  # Asigna el nombre al empleado
        self.employee = []  # Lista para almacenar los empleados que estarán a cargo
    
    # Método para añadir un empleado a la lista
    def add(self, employee):
        self.employee.append(employee)  # Añade el empleado a la lista
    
    # Método para imprimir los nombres de los empleados en la lista
    def print_employees(self):
        for employee in self.employee:  # Itera sobre la lista de empleados
            print(employee.name)  # Imprime el nombre de cada empleado

# Clase Manager, que hereda de Employee
class Manager(Employee):
    
    # Método para coordinar proyectos (solo imprime un mensaje)
    def coordinate_projects(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa.")

# Clase ProjectManager, que hereda de Employee
class ProjectManager(Employee):
    
    # Constructor que toma un ID, un nombre y un proyecto
    # Usa el constructor de la clase base Employee para ID y nombre
    def __init__(self, id: int, name: str, project: str) -> None:
        super().__init__(id, name)  # Llama al constructor de Employee
        self.project = project  # Asigna el proyecto al ProjectManager
    
    # Método para coordinar un proyecto específico (imprime un mensaje)
    def coordinate_project(self):
        print(f"{self.name} está coordinando su proyecto.")

# Clase Programmer, que hereda de Employee
class Programmer(Employee):
    
    # Constructor que toma un ID, un nombre y un lenguaje de programación
    def __init__(self, id: int, name: str, language: str) -> None:
        super().__init__(id, name)  # Llama al constructor de Employee
        self.language = language  # Asigna el lenguaje de programación al programador
        
    # Método para simular la acción de programar (imprime un mensaje)
    def code(self):
        print(f"{self.name} está programando en {self.language}.")
        
    # Sobrescribe el método add de Employee para evitar que un programador añada empleados
    def add(self, employee: Employee):
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")

# Creación de instancias de Manager, ProjectManager y Programmer
my_manager = Manager(1, "Mauricio")
my_project_manager = ProjectManager(2, "Arellano", "Proyecto 1")
my_project_manager2 = ProjectManager(3, "Bayardo", "Proyecto 2")
my_programmer = Programmer(4, "Mau", "Python")
my_programmer2 = Programmer(5, "Mau2", "Java")
my_programmer3 = Programmer(6, "Mau3", "PHP")
my_programmer4 = Programmer(7, "Mau4", "Javascript")

# Añadiendo Project Managers bajo la supervisión del Manager
my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

# Añadiendo programadores bajo la supervisión de Project Managers
my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

# Intentando añadir un programador a otro programador (se mostrará un mensaje de advertencia)
my_programmer.add(my_programmer2)

# Ejecutando algunas acciones
my_programmer.code()  # El programador programa
my_project_manager.coordinate_project()  # El Project Manager coordina su proyecto
my_manager.coordinate_projects()  # El Manager coordina todos los proyectos
my_manager.print_employees()  # El Manager imprime los empleados bajo su supervisión
my_project_manager.print_employees()  # El Project Manager imprime los empleados bajo su supervisión
my_programmer.print_employees()  # El Programador intenta imprimir empleados (aunque no tiene a nadie a cargo)

