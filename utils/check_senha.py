"""
    Verifica se a senha fornecida corresponde à senha criptografada.
    
    :param senha: A senha em texto simples a ser verificada.
    :param senha_criptografada: A senha criptografada para comparação.
    :return: True se a senha corresponder, False caso contrário.
    """
from bcrypt import checkpw

def check(senha: str, senha_criptografada: str) -> bool:
    result = checkpw(senha.encode('utf-8'), senha_criptografada.encode('utf-8')) 
    return result