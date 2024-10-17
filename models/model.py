import sqlite3

class Database:
    def __init__(self, db_name='mi_base_de_datos.db' ):
        # Conexión a la base de datos
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
    def crear_tabla(self):
        # Creación de la tabla (si no existe)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT,
                            edad INTEGER
                            )''')
        self.conn.commit()
    
    def insertar_usuario(self, nombre, edad):
        self.cursor.execute('''
            INSERT INTO usuarios (nombre, edad) VALUES (?, ?)
        ''', (nombre, edad))
        self.conn.commit()

    def obtener_usuarios(self):
        self.cursor.execute('SELECT * FROM usuarios')
        return self.cursor.fetchall()

    def actualizar_usuario(self, usuario_id, nombre, edad):
        self.cursor.execute('''
            UPDATE usuarios SET nombre = ?, edad = ? WHERE id = ?
        ''', (nombre, edad, usuario_id))
        self.conn.commit()

    def borrar_usuario(self, usuario_id):
        self.cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
        self.conn.commit()

    def cerrar_conexion(self):
        self.conn.close()