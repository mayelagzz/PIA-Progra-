listaEstudiantes = []

try:
    with open("listaEstudiantes.txt","r") as file:
        for line in file:
            listaEstudiantes.append(line)
except:
    print("")

class Estudiantes(object):
    def __init__ (self, nombre, apellido, matricula):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula 
        
    def entregarDatos(self):
        datos = self.nombre +" "+ self.apellido +" "+ str(self.matricula)
        return datos

def registrarEstudiante():
    print("")
    print("Registro del Estudiante")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    matricula = int(input("Ingrese el numero de matricula: "))
    objAlumno = Estudiantes(nombre, apellido, matricula)
    listaEstudiantes.append(objAlumno)
    with open("listaEstudiantes.txt","a") as file:
        dat = objAlumno.entregarDatos()
        file.write(dat)

def listadoEstudiantes():
    print("")
    print("Listado de Estudiantes:")
    for objAlumno in listaEstudiantes:
        print(objAlumno)

def salir():
    print("")
    print("Saliendo del programa! ...")
    print("")
    exit()

def main():
    while True:
        print("")
        print("          ¡B I E N V E N I D O!             ")
        print("--------------------------------------------")
        print("Seleccione una de las siguientes opciones: ")
        print("")
        print("1.-Registrar al Estudiante")
        print("2.-Mostrar el listado de Estudiantes")
        print("3.-Salir")

        print("")
        opcion = int(input("Opcion: "))
        print("")

        if opcion == 1:
            registrarEstudiante()
        elif opcion == 2:
            listadoEstudiantes()  
        elif opcion == 3:
            salir()
        else:
            print("")
            print("OPCION INCORRECTA ... SELECCIONE UNA OPCION VALIDA")
            print("")
if __name__ == "__main__":
    main()