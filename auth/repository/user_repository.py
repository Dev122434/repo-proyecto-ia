from auth.entities.user import User
from sqlmodel import create_engine, SQLModel, Session, select
import hashlib
# Configuración de la Base de Datos
sqlite_file_name = "user.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# check_same_thread=False es vital para GUIs como Flet
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# Crea las tablas si no existen
SQLModel.metadata.create_all(engine)

# --- 2. Controlador de Autenticación ---
class AuthController:
    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def registrar_user(self, email, password):
        with Session(engine) as session:
            # 1. Verificar si ya existe
            statement = select(User).where(User.email == email)
            results = session.exec(statement)
            if results.first():
                return False, "El User ya existe"
            
            # 2. Crear nuevo User
            User = User(
                email=email, 
                password=self._hash_password(password)
            )
            
            session.add(User)
            session.commit()
            return True, "User creado exitosamente"

    def verificar_user(self, email, password):
        with Session(engine) as session:
            # Buscar User por nombre
            statement = select(User).where(User.email == email)
            User = session.exec(statement).first()
            
            # Verificar si existe y si la contraseña coincide
            if User and User.password == self._hash_password(password):
                return True, f"Bienvenido, {User.email}"
            else:
                return False, "Email o contraseña incorrectos"