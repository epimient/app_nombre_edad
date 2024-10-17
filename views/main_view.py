# view/main_view.py

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class MainView:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Aplicación CRUD - CustomTkinter")
        self.ventana.geometry("600x700")  # Ajuste para acomodar la nueva disposición
        
        # Establecer el tamaño mínimo y máximo de la ventana
        self.ventana.minsize(600, 700)  # Tamaño mínimo: 600x700
        self.ventana.maxsize(600, 700)  # Tamaño máximo: 600x700

        # Configurar el modo oscuro y tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Frame principal para organizar los subframes
        self.frame_principal = ctk.CTkFrame(self.ventana)
        self.frame_principal.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Configurar el grid del frame_principal con 3 columnas
        self.frame_principal.grid_columnconfigure(0, weight=1)  # Espacio flexible a la izquierda
        self.frame_principal.grid_columnconfigure(1, weight=0)  # Columnas de contenido
        self.frame_principal.grid_columnconfigure(2, weight=1)  # Espacio flexible a la derecha

        # --- Frame para Entradas ---
        self.frame_entradas = ctk.CTkFrame(self.frame_principal)
        self.frame_entradas.grid(row=0, column=0, sticky="nw")  # Columna 0 (izquierda)

        # Etiqueta y campo de texto para el nombre
        self.label_nombre = ctk.CTkLabel(self.frame_entradas, text="Nombre:", font=("Arial", 16))
        self.label_nombre.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.entry_nombre = ctk.CTkEntry(self.frame_entradas, placeholder_text="Escribe tu nombre", width=250)
        self.entry_nombre.grid(row=1, column=0, pady=(0, 20), sticky="w")

        # Etiqueta y campo de texto para la edad
        self.label_edad = ctk.CTkLabel(self.frame_entradas, text="Edad:", font=("Arial", 16))
        self.label_edad.grid(row=2, column=0, pady=(0, 10), sticky="w")

        self.entry_edad = ctk.CTkEntry(self.frame_entradas, placeholder_text="Escribe tu edad", width=250)
        self.entry_edad.grid(row=3, column=0, pady=(0, 20), sticky="w")

        # --- Frame para Acciones ---
        self.frame_acciones = ctk.CTkFrame(self.frame_principal)
        self.frame_acciones.grid(row=0, column=1, padx=1, sticky="n")  # Columna 1 (centro) con padding lateral

        # Etiqueta para el Frame de Acciones
        self.label_acciones = ctk.CTkLabel(self.frame_acciones, text="Acciones", font=("Arial", 16))
        self.label_acciones.pack(pady=(0, 10))
        
        # Botones dentro del Frame de Acciones
        self.boton_guardar = ctk.CTkButton(self.frame_acciones, text="Guardar", width=200, corner_radius=32, border_color="#b8dcff", border_width=2)
        self.boton_guardar.pack(pady=10)

        self.boton_mostrar = ctk.CTkButton(self.frame_acciones, text="Mostrar Registros", width=200, corner_radius=32, border_color="#b8dcff", border_width=2)
        self.boton_mostrar.pack(pady=10)

        self.boton_actualizar = ctk.CTkButton(self.frame_acciones, text="Actualizar Registro", width=200, corner_radius=32, border_color="#b8dcff", border_width=2)
        self.boton_actualizar.pack(pady=10)

        self.boton_borrar = ctk.CTkButton(self.frame_acciones, text="Eliminar Registro", width=200, corner_radius=32, border_color="#b8dcff", border_width=2)
        self.boton_borrar.pack(pady=10)

        # --- Tabla de Datos ---

        # Frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.ventana)
        self.frame_tabla.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Scrollbar para la tabla
        self.scrollbar = ttk.Scrollbar(self.frame_tabla)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Definir columnas
        columnas = ("ID", "Nombre", "Edad")

        # Crear Treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings", yscrollcommand=self.scrollbar.set)

        # Definir encabezados
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor=tk.CENTER, width=150)

        self.tabla.pack(fill=tk.BOTH, expand=True)

        # Configurar la scrollbar
        self.scrollbar.config(command=self.tabla.yview)

        # Estilo de la tabla
        estilo = ttk.Style()
        estilo.theme_use("clam")  # Puedes elegir otros temas como "default", "classic", etc.
        estilo.configure("Treeview",
                         background="#2b2b2b",
                         foreground="white",
                         rowheight=25,
                         fieldbackground="#2b2b2b",
                         font=("Arial", 12))
        estilo.map("Treeview", background=[('selected', '#347083')])

        estilo.configure("Treeview.Heading",
                         background="#1f1f1f",
                         foreground="white",
                         font=("Arial", 14, "bold"))
