import flet as ft
from auth.repository.user_repository import AuthController

class LoginScreen:
    def __init__(self):
        self.auth = AuthController()

    def register_screen(self, page: ft.Page):

        email = ft.TextField(label="Correo", width=300)
        password = ft.TextField(label="Contraseña", password=True, width=300)

        def registrar(e):
            ok, msg = self.auth.registrar(email.value, password.value)
            
            page.snack_bar = ft.SnackBar(
                content=ft.Text(msg, color="white"),
                bgcolor="green" if ok else "red"
            )
            page.snack_bar.open = True
            page.update()

            if ok:
                page.go("/")

        return ft.View(
            route="/register",
            controls=[
                ft.Column(
                    [
                        ft.Text("Crear cuenta", size=30),
                        email,
                        password,
                        ft.ElevatedButton("Registrar", on_click=registrar),
                        ft.TextButton("Volver al login", on_click=lambda e: page.go("/"))
                    ],
                    alignment="center",
                    horizontal_alignment="center",
                )
            ],
        )

    def login_screen(self, page: ft.Page):

        email = ft.TextField(label="Correo", width=300)
        password = ft.TextField(label="Contraseña", password=True, width=300)

        def entrar(e):
            ok, msg = self.auth.login(email.value, password.value)

            page.snack_bar = ft.SnackBar(
                content=ft.Text(msg, color="white"),
                bgcolor="green" if ok else "red"
            )
            page.snack_bar.open = True
            page.update()

            if ok:
                page.go("/home")

        return ft.View(
            route="/",
            controls=[
                ft.Column(
                    [
                        ft.Text("Iniciar sesión", size=30),
                        email,
                        password,
                        ft.ElevatedButton("Entrar", on_click=entrar),
                        ft.TextButton("Registrarme", on_click=lambda e: page.go("/register"))
                    ],
                    alignment="center",
                    horizontal_alignment="center",
                )
            ],
        )

    def home_screen(self, page: ft.Page):
        return ft.View(
            route="/home",
            controls=[ft.Text("Bienvenido al sistema", size=40)]
        )
