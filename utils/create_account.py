import os
import sqlite3
from getpass import getpass
from utils import password_hashing

DB_PATH = "./data/users.db"


def create():
    email = input("Digite seu email: ").strip()
    # getpass não mostra a senha no terminal enquanto ela é digitada
    senha = getpass("Digite sua senha: ")

    if register(email, senha):
        print("Usuário registrado com sucesso!")
    else:
        print("Erro: email já está registrado.")


def register(email: str, senha: str, db_path: str = DB_PATH) -> bool:
    create_database(db_path)
    # Criptografa a senha
    hashed_password = password_hashing.hash(senha)

    conn = sqlite3.connect(db_path)
    try:
        conn.execute("INSERT INTO users (email, senha_hash) VALUES (?, ?)", (email, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def create_database(db_path: str = DB_PATH):
    os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                email TEXT PRIMARY KEY,
                senha_hash TEXT NOT NULL
            )
        """)
        conn.commit()
    finally:
        conn.close()
