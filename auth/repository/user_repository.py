from sqlmodel import SQLModel, Session, create_engine, select
from auth.entities.user import User
import hashlib

sqlite_file_name = "user.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine)

class AuthController():

    def _hash(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()

    def registrar(self, email: str, password: str):
        with Session(engine) as session:
            q = select(User).where(User.email == email)
            if session.exec(q).first():
                return False, "El usuario ya existe"

            user_obj = User(email=email, password=self._hash(password))
            session.add(user_obj)
            session.commit()

            return True, "Usuario registrado correctamente"

    def login(self, email: str, password: str):
        with Session(engine) as session:
            q = select(User).where(User.email == email)
            user = session.exec(q).first()

            if user and user.password == self._hash(password):
                return True, "Inicio de sesión exitoso"
            return False, "Credenciales incorrectas"
