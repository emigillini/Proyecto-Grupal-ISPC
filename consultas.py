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

