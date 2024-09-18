import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3

# Classe de Banco para gerenciar o banco de dados
class Banco:
    def __init__(self):
        self.conn = sqlite3.connect('usuarios.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_usuarios (
            idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            usuario TEXT,
            senha TEXT,
            cidade TEXT
        )""")
        self.conn.commit()

    def get_all_users(self):
        self.cursor.execute("SELECT nome, telefone, email, usuario, cidade FROM tbl_usuarios")
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()


# Função de exportar os dados e o gráfico para PDF
def exportar_para_pdf():
    banco = Banco()
    users = banco.get_all_users()

    # Criar o arquivo PDF
    pdf_file = "relatorio.pdf"
    pdf_pages = PdfPages(pdf_file)

    # Criar o gráfico de exemplo
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot([1, 2, 3], [4, 5, 6])  # Exemplo simples de gráfico
    ax.set_title('Exemplo de Gráfico')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.tight_layout()
    pdf_pages.savefig(fig)

    # Criar a tabela com dados do banco
    fig, ax = plt.subplots(figsize=(10, 6))
    if users:
        df = pd.DataFrame(users, columns=['Nome', 'Telefone', 'Email', 'Usuário', 'Cidade'])
        table = ax.table(cellText=df.values,
                         colLabels=df.columns,
                         cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.auto_set_column_width([0, 1, 2, 3, 4])
    else:
        ax.text(0.5, 0.5, 'Nenhum dado disponível', horizontalalignment='center', verticalalignment='center',
                fontsize=12)

    ax.axis('off')
    plt.tight_layout()
    pdf_pages.savefig(fig)

    # Fechar o PDF
    pdf_pages.close()

    # Mensagem de sucesso
    messagebox.showinfo("Sucesso", f"O relatório foi exportado para {pdf_file}")


# Configurar a interface do tkinter
root = tk.Tk()
root.title("Gerar Relatório em PDF")

# Adicionarum botão para exportar o relatório
btn_exportar = tk.Button(root, text="Exportar Relatório para PDF", command=exportar_para_pdf)
btn_exportar.pack(pady=20)

# Iniciar o loop principal do tkinter
root.mainloop()
