import sqlite3, os, shutil

DB_PATH = os.path.abspath("sofia.db")

# 1) cria backup
backup_path = DB_PATH + ".backup"
shutil.copy2(DB_PATH, backup_path)
print("Backup criado em:", backup_path)

# 2) apaga todos os registros da tabela usuarios
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute("DELETE FROM usuarios;")
conn.commit()
conn.close()

print("Tabela 'usuarios' limpa com sucesso.")
