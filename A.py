import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
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

# Pantalla principal con botones "Iniciar sesión" y "Crear cuenta"
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        login_button = Button(text="Iniciar sesión", font_size=24, size_hint=(1, 0.3))
        create_account_button = Button(text="Crear cuenta", font_size=24, size_hint=(1, 0.3))

        login_button.bind(on_press=self.go_to_login)
        create_account_button.bind(on_press=self.go_to_create_account)

        layout.add_widget(login_button)
        layout.add_widget(create_account_button)

        self.add_widget(layout)

    def go_to_login(self, instance):
        self.manager.current = 'login_screen'

    def go_to_create_account(self, instance):
        self.manager.current = 'create_account_screen'

# Pantalla de creación de cuenta
class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateAccountScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.name_input = TextInput(hint_text="Nombre", font_size=18, size_hint=(1, 0.2), multiline=False)
        self.carnet_input = TextInput(hint_text="Carné", font_size=18, size_hint=(1, 0.2), multiline=False)

        submit_button = Button(text="Enviar", font_size=24, size_hint=(1, 0.3))
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

# Pantalla de inicio de sesión
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.name_input = TextInput(hint_text="Nombre", font_size=18, size_hint=(1, 0.2), multiline=False)
        self.carnet_input = TextInput(hint_text="Carné", font_size=18, size_hint=(1, 0.2), multiline=False)

        login_button = Button(text="Iniciar sesión", font_size=24, size_hint=(1, 0.3))
        login_button.bind(on_press=self.login)

        layout.add_widget(self.name_input)
        layout.add_widget(self.carnet_input)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def login(self, instance):
        nombre = self.name_input.text
        carnet = self.carnet_input.text
        if verificar_usuario(nombre, carnet):
            print(f"Bienvenido {nombre}")
            self.manager.current = 'menu_screen'
        else:
            print("Usuario no encontrado o datos incorrectos")

# Pantalla con las opciones "Arrendar casa", "Perfil", "Buscar casa"
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        rent_button = Button(text="Arrendar casa", font_size=24, size_hint=(1, 0.3))
        profile_button = Button(text="Perfil", font_size=24, size_hint=(1, 0.3))
        search_button = Button(text="Buscar casa", font_size=24, size_hint=(1, 0.3))

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
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(MenuScreen(name='menu_screen'))

        return sm

if __name__ == "__main__":
    MyApp().run()
