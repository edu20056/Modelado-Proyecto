import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle
import os

kivy.require('2.0.0')

# Ruta al archivo donde se guardarán los usuarios
GUARDADO_PATH = "Guardado.txt"

# Función para guardar los datos de un usuario
def guardar_usuario(nombre, carnet):
    with open(GUARDADO_PATH, "a") as file:
        file.write(f"{nombre}/{carnet}\n")

# Función para verificar si el usuario está en el archivo
def verificar_usuario(nombre, carnet):
    if not os.path.exists(GUARDADO_PATH):
        return False
    with open(GUARDADO_PATH, "r") as file:
        usuarios = file.readlines()
        for usuario in usuarios:
            guardado_nombre, guardado_carnet = usuario.strip().split("/")
            if guardado_nombre == nombre and guardado_carnet == carnet:
                return True
    return False

# Pantalla principal con campos de texto para iniciar sesión y botones "Continuar" y "Crear cuenta"
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Usar FloatLayout para posiciones absolutas
        layout = FloatLayout()

        # Establecer el fondo de color #26eaff
        with layout.canvas.before:
            Color(0.149, 0.918, 1.0, 1.0) # Color #26eaff en formato RGB
            Rectangle(pos=(0,0), size=(10000, 10000))  # Usa el tamaño del layout


        # Cuadro de texto para Nombre
        self.name_input = TextInput(
            hint_text="Nombre", 
            font_size=18, 
            size_hint=(0.6, 0.1), 
            pos_hint={"x": 0.2, "y": 0.7}
        )

        # Cuadro de texto para Carné
        self.carnet_input = TextInput(
            hint_text="Carné", 
            font_size=18, 
            size_hint=(0.6, 0.1), 
            pos_hint={"x": 0.2, "y": 0.55}
        )

        # Botón Continuar
        continue_button = Button(
            text="Continuar", 
            font_size=24, 
            size_hint=(0.4, 0.1), 
            pos_hint={"x": 0.3, "y": 0.35},  
            background_color=get_color_from_hex("#5dc3eb")
        )

        # Botón Crear cuenta
        create_account_button = Button(
            text="Crear cuenta", 
            font_size=24, 
            size_hint=(0.4, 0.1), 
            pos_hint={"x": 0.3, "y": 0.20},  
            background_color=get_color_from_hex("#5dc3eb")
        )

        # Botón Olvidé Mi Contreaseña
        create_forgot_pass_button = Button(
            text="Olvidé mi contraseña", 
            font_size=24, 
            size_hint=(0.4, 0.1), 
            pos_hint={"x": 0.3, "y": 0.05},  
            background_color=(0.149, 0.918, 1.0, 1.0)
        )
        # Vincular eventos
        continue_button.bind(on_press=self.login)
        create_account_button.bind(on_press=self.go_to_create_account)

        # Añadir widgets al layout principal
        layout.add_widget(self.name_input)
        layout.add_widget(self.carnet_input)
        layout.add_widget(continue_button)
        layout.add_widget(create_account_button)
        layout.add_widget(create_forgot_pass_button)

        self.add_widget(layout)


    def login(self, instance):
        nombre = self.name_input.text
        carnet = self.carnet_input.text
        if verificar_usuario(nombre, carnet):
            print(f"Bienvenido {nombre}")
            self.manager.current = 'menu_screen'
        else:
            print("Usuario no encontrado o datos incorrectos")

    def go_to_create_account(self, instance):
        self.manager.current = 'create_account_screen'


# Pantalla de creación de cuenta
class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateAccountScreen, self).__init__(**kwargs)
        
        # Usar FloatLayout para control de posiciones
        layout = FloatLayout()

        # Establecer el fondo blanco
        with layout.canvas.before:
            Color(1, 1, 1, 1)  # Color blanco (RGB: 1,1,1, Alpha: 1)
            Rectangle(pos=(0,0), size=(10000, 10000))

        self.name_input = TextInput(
            hint_text="Nombre", 
            font_size=18, 
            size_hint=(0.6, 0.1), 
            pos_hint={"x": 0.2, "y": 0.7}  # Posicionar los elementos
        )
        self.carnet_input = TextInput(
            hint_text="Carné", 
            font_size=18, 
            size_hint=(0.6, 0.1), 
            pos_hint={"x": 0.2, "y": 0.55}
        )

        submit_button = Button(
            text="Enviar", 
            font_size=24, 
            size_hint=(0.4, 0.1), 
            pos_hint={"x": 0.3, "y": 0.35},  # Centrar el botón
            background_color=get_color_from_hex("#F44336")  # Rojo
        )
        submit_button.bind(on_press=self.submit_account)

        layout.add_widget(self.name_input)
        layout.add_widget(self.carnet_input)
        layout.add_widget(submit_button)

        self.add_widget(layout)

    def submit_account(self, instance):
        nombre = self.name_input.text
        carnet = self.carnet_input.text
        guardar_usuario(nombre, carnet)
        print(f"Usuario guardado: {nombre}/{carnet}")
        self.manager.current = 'main_screen'

# Pantalla con las opciones "Arrendar casa", "Perfil", "Buscar casa"
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # Establecer el fondo blanco
        with layout.canvas.before:
            Color(1, 1, 1, 1)  # Color blanco (RGB: 1,1,1, Alpha: 1)
            Rectangle(pos=(0,0), size=(10000, 10000))

        rent_button = Button(
            text="Arrendar casa", 
            font_size=24, 
            size_hint=(0.6, 0.1), 
            pos_hint={"x": 0.2, "y": 0.7},  # Control de posición
            background_color=get_color_from_hex("#FF9800")  # Naranja
        )
        profile_button = Button(
            text="Perfil", 
            font_size=24, 
            size_hint=(0.6, 0.1), 
            pos_hint={"x": 0.2, "y": 0.55},  # Control de posición
            background_color=get_color_from_hex("#03A9F4")  # Azul claro
        )
        search_button = Button(
            text="Buscar casa", 
            font_size=24, 
            size_hint=(0.6, 0.1), 
            pos_hint={"x": 0.2, "y": 0.4},  # Control de posición
            background_color=get_color_from_hex("#8BC34A")  # Verde claro
        )

        layout.add_widget(rent_button)
        layout.add_widget(profile_button)
        layout.add_widget(search_button)

        self.add_widget(layout)

# Administrador de pantallas
class MyScreenManager(ScreenManager):
    pass

# Clase principal de la aplicación
class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(CreateAccountScreen(name='create_account_screen'))
        sm.add_widget(MenuScreen(name='menu_screen'))

        return sm

if __name__ == "__main__":
    MyApp().run()
