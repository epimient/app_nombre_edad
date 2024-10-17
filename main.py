import customtkinter as ctk
from controllers.main_controller import MainController

def main():
    ventana = ctk.CTk()
    app = MainController(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()