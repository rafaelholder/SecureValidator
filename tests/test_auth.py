import sqlite3

import pytest

from utils import check_senha, password_hashing
from utils.create_account import register
from utils.login import authenticate


@pytest.fixture
def db_path(tmp_path):
    return str(tmp_path / "data" / "users.db")


def test_hash_nao_guarda_a_senha_em_texto():
    senha_hash = password_hashing.hash("minha-senha")
    assert "minha-senha" not in senha_hash
    assert senha_hash.startswith("$2b$")


def test_hash_usa_salt_diferente_a_cada_vez():
    assert password_hashing.hash("minha-senha") != password_hashing.hash("minha-senha")


def test_check_senha():
    senha_hash = password_hashing.hash("minha-senha")
    assert check_senha.check("minha-senha", senha_hash)
    assert not check_senha.check("outra-senha", senha_hash)


def test_registro_cria_o_banco_e_a_pasta(db_path):
    assert register("ana@exemplo.com", "senha-forte", db_path)
    conn = sqlite3.connect(db_path)
    (senha_hash,) = conn.execute("SELECT senha_hash FROM users WHERE email = ?", ("ana@exemplo.com",)).fetchone()
    conn.close()
    assert senha_hash != "senha-forte"


def test_email_duplicado_e_recusado(db_path):
    assert register("ana@exemplo.com", "senha-forte", db_path)
    assert not register("ana@exemplo.com", "outra-senha", db_path)


def test_login_com_senha_correta(db_path):
    register("ana@exemplo.com", "senha-forte", db_path)
    assert authenticate("ana@exemplo.com", "senha-forte", db_path)


def test_login_com_senha_errada(db_path):
    register("ana@exemplo.com", "senha-forte", db_path)
    assert not authenticate("ana@exemplo.com", "senha-errada", db_path)


def test_login_com_email_inexistente(db_path):
    assert not authenticate("ninguem@exemplo.com", "qualquer", db_path)


def test_injecao_de_sql_nao_autentica(db_path):
    register("ana@exemplo.com", "senha-forte", db_path)
    assert not authenticate("' OR '1'='1", "' OR '1'='1", db_path)
