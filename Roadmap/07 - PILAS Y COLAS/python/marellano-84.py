"""
Pilas y colas
"""

# Pilas/Stack (LIFO - Last In First Out)

stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# pop
stack_item = stack[len(stack) - 1]  # Metodo manual para sacar de la lista el ultimo elemento de la lista
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())  # El metodo pop desapila el ultimo elemento de la lista
print(stack)

# Cola/Queue (FIFO - First In First Out)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

# dequeue
queue_item = queue[0]  # Metodo manual para sacar de la lista el primer elemento de la lista
del queue[0]
print(queue_item)

print(queue.pop(0))     # Indicamos al metodo "pop" el indice del primer elemento en la lista 

print(queue)


"""
Desafio extra
"""

# Simulación de una web

def web_navigation():
    
    stack = []  # Pila de navegación
    forward_stack = []  # Pila para URLs hacia adelante
    
    while True:
        action = input("Añade una URL o interactua con palabras 'adelante/atras/salir': ")
        
        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            if len(forward_stack) > 0:
                next_url = forward_stack.pop()  # Recupera la última URL de la pila "forward"
                stack.append(next_url)
            else:
                print("No hay paginas adelante.")                      
        elif action == "atras":
            if len(stack) > 1:  # Debe haber al menos dos URLs para ir hacia atrás
                last_url = stack.pop()
                forward_stack.append(last_url)  # Mueve la URL actual a la pila de "adelante"
        else:
            stack.append(action)
            forward_stack.clear()  # Se vacía la pila de "adelante" al visitar una nueva URL
            
        if len(stack) > 0:    
            print(f"Has navegado a la web: {stack[len(stack) - 1]}")
        else:
            print("Estas en la pagina inicial.")
web_navigation()

def shared_printer():
    
    queue = []
    
    while True:
        
        action = input("Añade un documento o seleccion imprimir/salir: ")
        
        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
            # else:
            #     print("La cola de impresión está vacia.")
        else:
            queue.append(action)
            
        if len(queue) > 0:
            print(f"Cola de impresión: {queue}")
        else:
            print("La cola de impresión está vacia.")
        
shared_printer()