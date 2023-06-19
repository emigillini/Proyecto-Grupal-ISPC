import mysql.connector


class Ley:
    def __init__(self, numero, descripcion):
        self.numero = numero
        self.descripcion = descripcion

    def __str__(self):
        return f"Número de ley: {self.numero}\nDescripción: {self.descripcion}"

class GestorLeyes:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS leyes (numero TEXT PRIMARY KEY, descripcion TEXT)"
        )

    def insertar_ley(self, numero, descripcion):
        self.cursor.execute("INSERT INTO leyes (numero, descripcion) VALUES (%s, %s)", (numero, descripcion))
        self.connection.commit()
        print("Ley insertada con éxito.")

    def seleccionar_leyes(self):
        self.cursor.execute("SELECT * FROM leyes")
        leyes = self.cursor.fetchall()
        if leyes:
            for ley in leyes:
                print(Ley(*ley))
        else:
            print("No se encontraron leyes.")

    def actualizar_descripcion_ley(self, numero, nueva_descripcion):
        self.cursor.execute("UPDATE leyes SET descripcion = %s WHERE numero = %s", (nueva_descripcion, numero))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Descripción de la ley actualizada con éxito.")
        else:
            print("No se encontró la ley.")

    def eliminar_ley(self, numero):
        self.cursor.execute("DELETE FROM leyes WHERE numero = %s", (numero,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Ley eliminada con éxito.")
        else:
            print("No se encontró la ley.")

# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("1. Insertar una nueva ley")
    print("2. Consultar leyes")
    print("3. Actualizar descripción de una ley")
    print("4. Eliminar una ley")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Ejemplo de uso del programa
gestor = GestorLeyes("localhost:3306", "root", "Emiliano29782978", "world")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        numero = input("Ingrese el número de la ley: ")
        descripcion = input("Ingrese la descripción de la ley: ")
        gestor.insertar_ley(numero, descripcion)

    elif opcion == "2":
        gestor.seleccionar_leyes()

    elif opcion == "3":
        numero = input("Ingrese el número de la ley que desea actualizar: ")
        nueva_descripcion = input("Ingrese la nueva descripción de la ley: ")
        gestor.actualizar_descripcion_ley(numero, nueva_descripcion)

    elif opcion == "4":
        numero = input("Ingrese el número de la ley que desea eliminar: ")
        gestor.eliminar_ley(numero)

    elif opcion == "5":
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


gestor.connection.close()
