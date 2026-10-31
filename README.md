# SecureValidator

[![Testes](https://github.com/rafaelholder/SecureValidator/actions/workflows/tests.yml/badge.svg)](https://github.com/rafaelholder/SecureValidator/actions/workflows/tests.yml)

Cadastro e login de usuários pelo terminal, em Python, com foco em **armazenamento seguro de senhas**: as senhas são guardadas apenas como hash `bcrypt` com salt, em um banco **SQLite** local.

---

## Funcionalidades

- Cadastro de usuário com e-mail e senha
- Login com verificação da senha contra o hash armazenado
- Banco SQLite criado automaticamente em `data/users.db` na primeira execução

## Decisões de segurança

| Prática | Onde |
| --- | --- |
| Senhas guardadas só como hash `bcrypt`, com salt aleatório por senha | `utils/password_hashing.py` |
| Consultas parametrizadas (`?`), sem concatenar entrada do usuário no SQL | `utils/create_account.py`, `utils/login.py` |
| Senha lida com `getpass`, sem aparecer no terminal | `utils/create_account.py`, `utils/login.py` |
| Mesma mensagem para e-mail inexistente e senha errada, contra enumeração de usuários | `utils/login.py` |
| Verificação bcrypt também quando o e-mail não existe, para o tempo de resposta não revelar quais e-mails estão cadastrados | `utils/login.py` |
| Banco de dados fora do controle de versão (`.gitignore`) | `.gitignore` |

## Estrutura

```
.
├── main.py                  # menu: criar conta ou fazer login
├── utils/
│   ├── create_account.py    # cadastro e criação do banco
│   ├── login.py             # autenticação
│   ├── password_hashing.py  # hash bcrypt
│   └── check_senha.py       # comparação de senha com o hash
└── tests/
    └── test_auth.py         # testes com pytest
```

## Tecnologias

- Python 3.10+
- [bcrypt](https://pypi.org/project/bcrypt/)
- SQLite3 (embutido no Python)
- pytest e GitHub Actions

---

## Como executar

```bash
git clone https://github.com/rafaelholder/SecureValidator.git
cd SecureValidator
python -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Digite `c` para criar uma conta ou `l` para fazer login.

## Testes

```bash
pip install -r requirements-dev.txt
pytest
```

Os testes usam um banco temporário e cobrem o hash, o cadastro, e-mail duplicado, login com senha certa e errada, e-mail inexistente e uma tentativa de injeção de SQL.
