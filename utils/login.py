from utils import check_senha
import sqlite3

def login():
    email_login = input("Digite seu email: ")
    senha_login= input("Digite sua senha: ")
    
    conn = sqlite3.connect("./data/users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT senha_hash FROM users WHERE email = ?", (email_login,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        senha_hash = resultado[0]
        if check_senha.check(senha=senha_login, senha_criptografada=senha_hash):
            print("Autenticação bem-sucedida!")
            return True
        else:
            print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")
    
    return False
    
    
    
    
    
    
    
    
    
    
    
    
    # with open(f"./data/{email_login}.txt", "r") as f:
    #     lines = f.readlines()
    #     stored_password = None
    #     for line in lines:
    #         if line.startswith("senha:"):
    #             stored_password = line.split(":", 1)[1].strip()
    #             break
            
    # if stored_password is not None:
    #     if check_senha.check(senha=senha_login, senha_criptografada=stored_password): print("Senha correta!")
    #     else: print("Senha incorreta!")
        