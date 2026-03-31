
date_student = []


def add_student():
    ask1 = True
    while ask1:
        try:
            id = int(input("Enter student id: "))
            if id < 0:
                print("Error:please enter a positive value")
            else:
                ask1 = False
        except ValueError:
            print("Error: plesea enter a valid enteger")

    name = input("Enter student name: ")
    ask = True
    while ask:
        try:
            age = int(input("Enter student age: "))
            if age < 0:
                print("Error: please enter a positive value")
            else:
                ask = False
        except ValueError:
            print("Error:plese enter a valid enteger")

    course = input("Enter the student course: ")
    state = input("Enter the student state activo / inactivo: ")

    date = {
        "id": id,
        "name": name,
        "age": age,
        "course": course,
        "state": state
    }
    date_student.append(date)
    return date


def student_consult():
    if not date_student:
        print("no hay estudiantes registrados")
        
    for date in date_student:
        print(f"id:{date['id']}|name:{date['name']}|age:{date['age']}|course:{date['course']}|state:{date['state']}")


def search_student(busqueda, date_student):
    if not date_student:
        print("no existe")
        return True
   
    for date in date_student:
        if date["name"] == busqueda or str(date["id"]) == busqueda:
            print(
                f"id:{date['id']}|name:{date['name']}|age:{date['age']}|course:{date['course']}|state:{date['state']}")
            return False
def actualizar_info(date_student,new_name,new_id):
        new_name=input("ingrese el nuevo estudiante:  ")
        new_id= input("ingrese el nuevo id : ")
        actualizar_info1 = search_student(date_student, new_id,new_name)
        if actualizar_info1:
            # Solo actualiza los campos que el usuario proporcionó
            if new_name is not None:
                actualizar_info1["name"] = new_name
            if new_id is not None:
                actualizar_info1["id"] = new_id
            return True
        return False

def eliminar_student(name, date_student):
    for date in date_student:
        if date['name'] == name:
            date_student.remove(date)
            print("cliente eliminado")


def menu():
    """Muestra el menú principal de opciones del sistema."""
    print("\n=== SISTEMA ESCOLAR PRO ===")
    print("1. add student | 2. show student | 3. search ")
    print("4. Update student| 5. Save CSV | 6. Delete student | 7. Exit")
