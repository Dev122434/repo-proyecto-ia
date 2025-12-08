from auth.login import LoginScreen
import flet as ft

def main(page: ft.Page):
    login = LoginScreen(page)
    login.login()
ft.app(main)