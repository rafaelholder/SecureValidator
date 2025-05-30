from os import makedirs 
from utils import create_account, login

if __name__ == "__main__":
    op = input("Digite 'c' para criar uma conta ou 'l' para fazer login: ").strip().lower()
    if op not in ['c', 'l']:
        print("Opção inválida. Por favor, digite 'c' ou 'l'.")
        exit(1)
    if op == 'c':
        create_account.create()
    elif op == 'l':
        login.login()