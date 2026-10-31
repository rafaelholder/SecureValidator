import secrets
import sqlite3
from getpass import getpass
from utils import check_senha, password_hashing
from utils.create_account import DB_PATH, create_database

# Hash de uma senha aleatória, usado quando o e-mail não existe. Assim o login
# faz uma verificação bcrypt nos dois casos e leva o mesmo tempo, sem revelar
# pelo tempo de resposta quais e-mails estão cadastrados.
HASH_FICTICIO = password_hashing.hash(secrets.token_hex(16))


def login():
    email_login = input("Digite seu email: ").strip()
    senha_login = getpass("Digite sua senha: ")

    if authenticate(email_login, senha_login):
        print("Autenticação bem-sucedida!")
        return True

    # A mesma mensagem para e-mail inexistente e senha errada evita enumeração de usuários
    print("E-mail ou senha inválidos.")
    return False


def authenticate(email: str, senha: str, db_path: str = DB_PATH) -> bool:
    create_database(db_path)

    conn = sqlite3.connect(db_path)
    try:
        resultado = conn.execute("SELECT senha_hash FROM users WHERE email = ?", (email,)).fetchone()
    finally:
        conn.close()

    if resultado is None:
        check_senha.check(senha=senha, senha_criptografada=HASH_FICTICIO)
        return False
    return check_senha.check(senha=senha, senha_criptografada=resultado[0])
