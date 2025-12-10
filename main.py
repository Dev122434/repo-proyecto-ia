from auth.login import LoginScreen
import flet as ft
login = LoginScreen()

def main(page: ft.Page):

    def route_change(route):
        if page.route == "/":
            page.views.clear()
            page.views.append(login.login_screen(page))

        elif page.route == "/register":
            page.views.clear()
            page.views.append(login.register_screen(page))

        elif page.route == "/home":
            page.views.clear()
            page.views.append(login.home_screen(page))

        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)