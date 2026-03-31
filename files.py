import csv

def guardar_csv(student, ruta):
    """
    Guarda el student en un archivo CSV.
    
    Args:
        student: lista de studiantes a guardar
        ruta: ruta del archivo CSV destino
    """
    if not student:
        print(" No hay nada que guardar.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "age","course","state"])
            # Escribe la fila de encabezados
            writer.writeheader()
            # Escribe todos los productos
            writer.writerows(student)
        print(f"save the student in : {ruta}")
    except Exception as e:
        print(f" Error al guardar: {e}")
