import flet as ft
class LoginScreen:

    def __init__(self, page: ft.Page):
        self.page = page

    def login(self):
        self.page.title = "Login Moderno"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window_width = 400
        self.page.window_height = 500
        self.page.window_resizable = False
        self.page.bgcolor = ft.Colors.BLUE_GREY_50

        def validar_login(e):
            # Reiniciar errores
            txt_user.error_text = None
            txt_pass.error_text = None
        
            if not txt_user.value:
                txt_user.error_text = "Por favor ingrese su usuario"
                self.page.update()
            elif not txt_pass.value:
                txt_pass.error_text = "Por favor ingrese su contraseña"
                self.page.update()
            else:
                print(f"Login intento: {txt_user.value}")
                self.page.snack_bar = ft.SnackBar(
                content=ft.Text("¡Iniciando sesión con éxito!", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.GREEN
            )
            self.page.snack_bar.open = True
            self.page.update()
    
    # Campo de Usuario
        txt_user = ft.TextField(    
            label="Nombre de usuario",
            prefix_icon=ft.Icons.PERSON,
            border_radius=10,
            keyboard_type=ft.KeyboardType.EMAIL,
        )

        txt_pass = ft.TextField(
            label="Contraseña",
            prefix_icon=ft.Icons.LOCK,
            password=True,
            can_reveal_password=True, # Permite ver la contraseña con el ojito
            border_radius=10,
        )

        btn_login = ft.ElevatedButton(
            text="INGRESAR",
            width=300,
            height=45,
            style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE_600,
            shape=ft.RoundedRectangleBorder(radius=10),
            ),
            on_click=validar_login
        )

        logo_icon = ft.Icon(
            name=ft.Icons.ADMIN_PANEL_SETTINGS_ROUNDED,
            size=60,
            color=ft.Colors.BLUE_600
        )
    
        lbl_title = ft.Text(
            value="Bienvenido",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_GREY_900
        )

        login_container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=20), # Espaciador
                    logo_icon,
                    lbl_title,
                    ft.Text("Inicia sesión para continuar", color=ft.Colors.GREY),
                    ft.Container(height=20), # Espaciador
                    txt_user,
                    txt_pass,
                    ft.Container(height=10), # Espaciador
                    btn_login,
                    ft.Container(height=10),
                    ft.TextButton(text="¿Olvidaste tu contraseña?", style=ft.ButtonStyle(color=ft.Colors.GREY))
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=350,
            padding=30,
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.BLUE_GREY_100,
            )
        )
        self.page.add(login_container)