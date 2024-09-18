import tkinter as tk
from tkinter import messagebox, filedialog
import os
from usuarios import Usuarios
from banco import Banco


class PaginaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestão")
        self.master.geometry("800x600")

        tk.Button(self.master, text="Adicionar Usuário", command=self.adicionar_usuario).pack(pady=10)
        tk.Button(self.master, text="Alterar Usuário", command=self.alterar_usuario).pack(pady=10)
        tk.Button(self.master, text="Excluir Usuário", command=self.excluir_usuario).pack(pady=10)
        tk.Button(self.master, text="Gerenciar Usuários", command=self.gerenciar_usuarios).pack(pady=10)
        tk.Button(self.master, text="Visualizar PDF", command=self.visualizar_pdf).pack(pady=10)  # Novo botão

    def adicionar_usuario(self):
        AdicionarUsuario(self.master)

    def alterar_usuario(self):
        AlterarUsuario(self.master)

    def excluir_usuario(self):
        ExcluirUsuario(self.master)

    def gerenciar_usuarios(self):
        GerenciarUsuarios(self.master)

    def visualizar_pdf(self):
        # Abre um diálogo para selecionar o arquivo PDF
        pdf_path = filedialog.askopenfilename(
            title="Selecione um arquivo PDF",
            filetypes=(("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*"))
        )

        # Verifica se o arquivo foi selecionado
        if pdf_path:
            try:
                # Abre o PDF no visualizador padrão do sistema
                os.system(f'open "{pdf_path}"' if os.name == 'posix' else f'start "" "{pdf_path}"')
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir o arquivo PDF: {e}")
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")
