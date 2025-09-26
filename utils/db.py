# utils/db.py
import sqlite3
import hashlib

DB_PATH = "sofia.db"

def hash_password(senha: str) -> str:
    """Gera hash SHA-256 da senha."""
    return hashlib.sha256(senha.encode()).hexdigest()

def init_db():
    """Cria a tabela de usuários se não existir."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_user_by_email(email: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    user = c.fetchone()
    conn.close()
    return user

def update_password(email: str, nova_senha: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE usuarios SET senha = ? WHERE email = ?", (hash_password(nova_senha), email))
    conn.commit()
    conn.close()
