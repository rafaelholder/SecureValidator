from os import path
import sqlite3
from utils import password_hashing



def create():
    create_database()
    senha = input("Digite sua senha: ")
    email = input("Digite seu email: ")
    # Criptografa a senha
    hashed_password = password_hashing.hash(senha)

    conn = sqlite3.connect("./data/users.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (email, senha_hash) VALUES (?, ?)", (email, hashed_password))
        conn.commit()
        print("Usuário registrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: email já está registrado.")
    finally:
        conn.close()

def create_database():
    if not path.exists("./data"):
        path.makedirs("./data")
    conn = sqlite3.connect("./data/users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            senha_hash BLOB
        )   
    """)
    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso!")