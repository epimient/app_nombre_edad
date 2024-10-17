from models.model import Database
from views.main_view import MainView
import tkinter as tk
import customtkinter as ctk

class MainController:
    def __init__(self, ventana):
        self.db = Database()
        self.view = MainView(ventana)
    
        # Asociar botones con sus métodos
        self.view.boton_guardar.configure(command=self.guardar_datos)
        self.view.boton_mostrar.configure(command=self.mostrar_datos)
        self.view.boton_actualizar.configure(command=self.actualizar_datos)
        self.view.boton_borrar.configure(command=self.borrar_datos)
        
        # Asociar evento de selección en la tabla
        self.view.tabla.bind("<<TreeviewSelect>>", self.on_seleccion)
        
    def guardar_datos(self):
        nombre = self.view.entry_nombre.get()
        edad = self.view.entry_edad.get()

        if nombre and edad:
            if edad.isdigit():
                self.db.insertar_usuario(nombre, int(edad))
                self.view.entry_nombre.delete(0, ctk.END)
                self.view.entry_edad.delete(0, ctk.END)
                self.mostrar_datos()
            else:
                print("La edad debe ser un número.")
        else:
            print("Por favor, completa todos los campos.")

    def mostrar_datos(self):
        # Limpiar la tabla
        for item in self.view.tabla.get_children():
            self.view.tabla.delete(item)

        # Obtener datos de la base de datos
        usuarios = self.db.obtener_usuarios()
        for usuario in usuarios:
            self.view.tabla.insert("", tk.END, values=usuario)

    def actualizar_datos(self):
        seleccion = self.view.tabla.selection()

        if seleccion:
            item = self.view.tabla.item(seleccion)
            registro_id, _, _ = item['values']

            nuevo_nombre = self.view.entry_nombre.get()
            nueva_edad = self.view.entry_edad.get()

            if nuevo_nombre and nueva_edad:
                if nueva_edad.isdigit():
                    self.db.actualizar_usuario(registro_id, nuevo_nombre, int(nueva_edad))
                    self.view.entry_nombre.delete(0, ctk.END)
                    self.view.entry_edad.delete(0, ctk.END)
                    self.mostrar_datos()
                else:
                    print("La edad debe ser un número.")
            else:
                print("Por favor, completa los campos para actualizar.")
        else:
            print("No hay ningún registro seleccionado para actualizar.")

    def borrar_datos(self):
        seleccion = self.view.tabla.selection()

        if seleccion:
            item = self.view.tabla.item(seleccion)
            registro_id, _, _ = item['values']

            self.db.borrar_usuario(registro_id)
            self.mostrar_datos()
        else:
            print("No hay ningún registro seleccionado para eliminar.")

    def on_seleccion(self, event):
        seleccion = self.view.tabla.selection()
        if seleccion:
            item = self.view.tabla.item(seleccion)
            registro = item['values']
            if registro:
                _, nombre, edad = registro
                self.view.entry_nombre.delete(0, ctk.END)
                self.view.entry_nombre.insert(0, nombre)
                self.view.entry_edad.delete(0, ctk.END)
                self.view.entry_edad.insert(0, edad)