"""Práctica arboles usando min heap con nodos, presentada por:
Angie Diaz Abaunza
Mateo Molina Alvarez"""

class Paciente:
    def __init__(self, numero, genero, nombre, edad, triaje):
        self.numero = numero
        self.genero = genero
        self.nombre = nombre
        self.edad = edad
        self.triaje = triaje

    def __repr__(self):
        return f"Paciente({self.nombre}, Triaje: {self.triaje})"

class Node:
    def __init__(self, paciente):
        self.paciente = paciente
        self.left = None
        self.right = None

class MinHeap:
    def __init__(self): 
        self.nodes = []

    def parent(self, pos):
        return (pos - 1) // 2

    def leftChild(self, pos):
        return 2 * pos + 1

    def rightChild(self, pos):
        return 2 * pos + 2

    def isLeaf(self, pos):
        return self.leftChild(pos) >= len(self.nodes) and self.rightChild(pos) >= len(self.nodes)

    def swap(self, pos1, pos2):
        self.nodes[pos1], self.nodes[pos2] = self.nodes[pos2], self.nodes[pos1]

    def insert(self, paciente):
        self.nodes.append(paciente)
        current = len(self.nodes) - 1
        
        while current > 0:
            parent = self.parent(current)
            if self.nodes[current].triaje < self.nodes[parent].triaje:
                self.swap(current, parent)
                current = parent 
            else:
                break 

    def heapify_down(self, pos):
        smallest = pos 
        left = self.leftChild(pos) 
        right = self.rightChild(pos)
        
        if left < len(self.nodes) and self.nodes[left].triaje < self.nodes[smallest].triaje:
            smallest = left
        
        if right < len(self.nodes) and self.nodes[right].triaje < self.nodes[smallest].triaje:
            smallest = right
        
        if smallest != pos:
            self.swap(pos, smallest)
            self.heapify_down(smallest)

    def heapify_up(self, pos):
        current = pos
        while current > 0:
            parent = self.parent(current)
            if self.nodes[current].triaje < self.nodes[parent].triaje:
                self.swap(current, parent)
                current = parent
            else:
                break

    def consultar_proximo_paciente(self):
        if len(self.nodes) > 0:
            return self.nodes[0]
        else:
            return None

    def atender_siguiente(self):
        if len(self.nodes) == 0:
            return None

        if len(self.nodes) == 1:
            return self.nodes.pop()

        root = self.nodes[0]
        self.nodes[0] = self.nodes.pop()
        self.heapify_down(0) 
        return root 

    def eliminar_paciente(self, identifier):
        index = -1 
        for i in range(len(self.nodes)):
            if self.nodes[i].numero == identifier or self.nodes[i].nombre == identifier:
                index = i
                break
        
        if index == -1:
            return False
        
        self.swap(index, len(self.nodes) - 1)
        eliminado = self.nodes.pop()
        
        if index < len(self.nodes): 
            self.heapify_down(index)
            self.heapify_up(index)
        
        return eliminado

    def consultar_pacientes_espera(self):
        return self.nodes

    def consultar_pacientes_por_triaje(self, triaje):
        return [paciente for paciente in self.nodes if paciente.triaje == triaje]

    def printHeap(self):
        for node in self.nodes: 
            print(node)

def main():
    heap = MinHeap()
    while True:
        print("\nMenu de Opciones:")
        print("1. Registrar paciente")
        print("2. Consultar próximo paciente a atención")
        print("3. Atender siguiente paciente")
        print("4. Consultar pacientes en espera")
        print("5. Consultar pacientes en espera por triaje")
        print("6. Eliminar paciente")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            numero = int(input("Número de paciente: "))
            genero = input("Género del paciente (M/F): ")
            nombre = input("Nombre del paciente: ")
            edad = int(input("Edad del paciente: "))
            triaje = int(input("Triaje del paciente (1-5): "))
            paciente = Paciente(numero, genero, nombre, edad, triaje)
            heap.insert(paciente)
            print(f"Paciente {nombre} registrado con éxito.")
        
        elif opcion == "2":
            proximo = heap.consultar_proximo_paciente()
            if proximo:
                print(f"Próximo paciente a atención: {proximo}")
            else:
                print("No hay pacientes en espera.")
        
        elif opcion == "3":
            atendido = heap.atender_siguiente()
            if atendido:
                print(f"Paciente atendido: {atendido}")
            else:
                print("No hay pacientes en espera.")
        
        elif opcion == "4":
            pacientes = heap.consultar_pacientes_espera()
            if pacientes:
                print("Pacientes en espera:")
                for paciente in pacientes:
                    print(paciente)
            else:
                print("No hay pacientes en espera.")
        
        elif opcion == "5":
            triaje = int(input("Ingrese el triaje a consultar (1-5): "))
            pacientes = heap.consultar_pacientes_por_triaje(triaje)
            if pacientes:
                print(f"Pacientes en espera con triaje {triaje}:")
                for paciente in pacientes:
                    print(paciente)
            else:
                print(f"No hay pacientes en espera con triaje {triaje}.")
        
        elif opcion == "6":
            identifier = input("Ingrese el nombre o ID del paciente a eliminar: ")
            if identifier.isdigit():
                identifier = int(identifier)
            eliminado = heap.eliminar_paciente(identifier)
            if eliminado:
                print(f"Paciente eliminado: {eliminado}")
            else:
                print("Paciente no encontrado.")
        
        elif opcion == "7":
            print("Saliendo del sistema.")
            break
        
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()