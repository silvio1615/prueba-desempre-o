import feature
import files
running=True
while running:
    feature.menu()
    option= input("select an opcion: ")
    if option == "1":
        feature.add_student()
    elif option == "2":
        feature.student_consult()
    elif option == "3":
        busqueda = input("Ingrese un id o nombre del estudiante a buscar")
        feature.search_student(busqueda,feature.date_student)
    #elif option == "4":
       
    elif option == "5":
       files.guardar_csv(feature.date_student,"student.csv")
    elif option == "6":
       Name = input("ingrese el nombre del estudiante: ")
       feature.eliminar_student(Name,feature.date_student)
    elif option == "7":
     print("exit system ")
     break
    else:
       print("Invalid option. Please try again.")

            
