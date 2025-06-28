import customtkinter
from PIL import Image, ImageTk
import os
import sys
import sqlite3

def verificar_login(username, password):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
    resultado = cursor.fetchone()

    conexao.close()
    return resultado is not None

def tentar_login(root, janela_login, usuario, senha):
    if verificar_login(usuario, senha):
        print("Login válido!")
        janela_login.destroy()
        JanelaMain(root)
    else:
        print("Login inválido!")
        # Pode mostrar uma CTkMessageBox ou CTkLabel com erro


# TELA DE LOGIN
def login_page(root):
    Janelalogin = customtkinter.CTkToplevel()
    Janelalogin.title("Login")
    Janelalogin.geometry("300x270")

    label = customtkinter.CTkLabel(Janelalogin, text="Welcome to the Login Page")
    label.pack(pady=20)

    login_entry = customtkinter.CTkEntry(Janelalogin, placeholder_text="Username")
    login_entry.pack(pady=10)
    password_entry = customtkinter.CTkEntry(Janelalogin, placeholder_text="Password", show="*")
    password_entry.pack(pady=10)

    login_btn = customtkinter.CTkButton(
        Janelalogin,
        text="Login",
        command=lambda: tentar_login(root, Janelalogin, login_entry.get(), password_entry.get())
    )

    login_btn.pack(pady=10)

    # ENCERRA O PROGRAMA AO FECHAR A JANELA DE LOGIN
    def fechar_janela():
        Janelalogin.destroy()
        sys.exit()
    Janelalogin.protocol("WM_DELETE_WINDOW", fechar_janela)

def fechar_janelalogin(root, Janelalogin):
    Janelalogin.destroy()
    JanelaMain(root)


def JanelaMain(root):
    JanelaPrincipal = customtkinter.CTkToplevel()
    JanelaPrincipal.title("Main Window")
    JanelaPrincipal.geometry("700x500")

    label = customtkinter.CTkLabel(JanelaPrincipal, text="Welcome to the Main Window")
    label.pack(pady=20)

    def fechar_janela():
        JanelaPrincipal.destroy()
        sys.exit()
    JanelaPrincipal.protocol("WM_DELETE_WINDOW", fechar_janela)



root = customtkinter.CTk()
root.withdraw()  # Oculta a janela principal

login_page(root)

# Mantém o app rodando
root.mainloop()