# SecureValidator

**SecureValidator** é um sistema simples de gerenciamento de usuários com foco em **armazenamento seguro de senhas** usando hashing (`bcrypt`) e persistência de dados com **SQLite**. Ideal para estudos e projetos de segurança cibernética.

---

## Funcionalidades

- Registro de usuários com e-mail e senha
- Armazenamento seguro das senhas (bcrypt + salt)
- Verificação/autenticação de senha
- Banco de dados local (SQLite)
- Estrutura modular (código organizado por pastas)

---

## 🛠 Tecnologias utilizadas

- Python 3.10+
- [bcrypt](https://pypi.org/project/bcrypt/)
- SQLite3 (embutido no Python)

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/SecureValidator.git
cd SecureValidator
