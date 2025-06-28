# 🧪 Sistema de Login com CustomTkinter e SQLite

Este projeto é um exemplo simples de um sistema de **login com interface gráfica** moderna usando [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) e banco de dados **SQLite** para autenticação de usuários.

---

## 🎯 Funcionalidades

- Interface de login com campos de usuário e senha
- Verificação de credenciais em um banco SQLite
- Transição de tela após login bem-sucedido
- Encerramento completo do app ao fechar a janela

---

## 💻 Tecnologias usadas

- Python 3.10+
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Pillow (para manipular imagens)
- SQLite3 (banco de dados local)

---

## 🚀 Como rodar o projeto

Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
venv\Scripts\activate  # no Windows

Instale as dependências:
pip install customtkinter pillow

Crie o banco de dados (ou use o SQLiteStudio):
Você pode usar esse SQL:
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
INSERT INTO usuarios (username, password) VALUES ('admin', '1234');

Execute o projeto:
python main.py
