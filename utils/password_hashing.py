from bcrypt import gensalt, hashpw

def hash(senha: str) -> str:
    salt = gensalt()
    hash_with_salt = hashpw(senha.encode('utf-8'), salt)
    return hash_with_salt.decode('utf-8')
    