"""
Clases
"""

class Programmer:
    
    surname: str = None
    
    def __init__(self, name: str, age: int, language: list):
        self.name = name
        self.age = age
        self.language = language
        
    def printer(self):
        print(f"Nombre: {self.name} | Apellido: {self.surname} | Edad: {self.age} | Lenguajes: {self.language}")

my_programmer = Programmer("Mau", 39, ["Python", "Java"])
my_programmer.printer()
my_programmer.surname = "Arellano"
my_programmer.printer()
my_programmer.age = 40
my_programmer.printer()

"""
Desafio extra
"""

# LIFO

class Stack:
    
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
    
    def count(self):
            return len(self.stack)
        
    def printer(self):
        for item in reversed(self.stack):
            print(item)
            
my_stack = Stack()  # Instancia el objeto por medio de una variable
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.printer()
my_stack.pop()
print(my_stack.count())

# FIFO

class Queue:
    
    def __init__(self):
        self.queue = []
        
    def equeue(self, item):
        self.queue.append(item)
        
    def deequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)
    
    def count(self):
            return len(self.queue)
        
    def printer(self):
        for item in self.queue:
            print(item)
            
my_queue = Queue()  # Instancia el objeto por medio de una variable
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print(my_queue.count())
my_queue.printer()
my_queue.deequeue()
print(my_queue.count())