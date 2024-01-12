# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import Entry, PhotoImage, Canvas, Text, Button, ttk
import tkinter as tk
import sys
from cruds.Usuario import consultar_usuario

from tab_functions import abrir_aba_editar_usuario


ASSETS_PATH = Path(__file__).parent / "assets" / "frame0"
ROOT_PATH = Path(__file__).parent.parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.append(str(ROOT_PATH))
from Telas.defs import *


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def criar_tela_consultar_usuarios(
    frame: ttk.Frame,
    imagens: dict[str, dict],
    notebook: ttk.Notebook,
    imagens_dict: dict[str, dict],
):
    # Imagens
    imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
    imagens["entry_1"] = PhotoImage(file=relative_to_assets("entry_1.png"))
    imagens["button_1"] = PhotoImage(file=relative_to_assets("button_1.png"))
    imagens["button_2"] = PhotoImage(file=relative_to_assets("button_2.png"))
    imagens["image_2"] = PhotoImage(file=relative_to_assets("image_2.png"))
    imagens["button_3"] = PhotoImage(file=relative_to_assets("button_3.png"))
    imagens["image_3"] = PhotoImage(file=relative_to_assets("image_3.png"))

    # Canvas
    canvas = Canvas(
        frame,
        bg="#FFFFFF",
        height=768,
        width=1365,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    # Adiciona imagens, textos, retângulos ao canvas
    canvas.create_image(682.0, 384.0, image=imagens["image_1"])
    canvas.create_image(607.5, 83.0, image=imagens["entry_1"])
    canvas.create_rectangle(103.0, 55.0, 1050.0, 112.0, fill="#FFFFFF", outline="")
    canvas.create_image(1211.0, 421.0, image=imagens["image_2"])
    canvas.create_image(135.0, 82.0, image=imagens["image_3"])
    canvas.create_text(
        36.0,
        142.0,
        anchor="nw",
        text="Lista de usuários:",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 40 * -1),
    )

    # Botões
    button_1 = Button(
        frame,
        image=imagens["button_1"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Deletar"),
        relief="flat",
    )
    button_1.place(x=1076.0, y=651.0, width=268.0, height=68.0)

    button_3 = Button(
        master=frame,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: abrir_aba_editar_usuario(notebook, imagens_dict),
        relief="flat",
        text="Editar Usuário",
        font=(FONTE_TELAS, 40),
        background="#FFD708",
        activebackground="#FFD708",
    )
    button_3.place(x=1076.0, y=551.0, width=268.0, height=68.0)

    def cria_tabela_usuarios(frame_pai: ttk.Frame):
        pesquisa = tk.StringVar()

        entry_pesquisa = Entry(
            frame_pai,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=pesquisa,
            font=(FONTE_INPUT, 28),
        )
        entry_pesquisa.place(x=174.0, y=60.0, width=867.0, height=44.0)

        button_pesquisa = Button(
            frame,
            image=imagens["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: atualizar_tabela(),
            relief="flat",
        )
        button_pesquisa.place(x=1124.0, y=55.0, width=176.0, height=60.0)

        # Novo Frame para conter a tabela e a barra de rolagem
        frame_tabela = ttk.Frame(frame_pai)
        frame_tabela.place(x=36.0, y=185.0, width=1015.0, height=550.0, anchor="nw")
        tabela = ttk.Treeview(
            frame_tabela, columns=("nome", "matrícula", "email"), show="headings"
        )
        tabela.heading("nome", text="Nome")
        tabela.heading("matrícula", text="Matrícula")
        tabela.heading("email", text="Email")
        tabela.grid(row=0, column=0, sticky="nsew")

        def atualizar_tabela(event=None):
            nonlocal pesquisa

            # Obtém o termo pesquisado caso ele exista
            termo_pesquisado = pesquisa.get() if pesquisa.get() != "" else None

            # Limpa os dados existentes na tabela
            tabela.delete(*tabela.get_children())

            # Obtém novos dados da função consultar_usuario
            usuarios = consultar_usuario(termo_pesquisado)

            # Insere os novos dados na tabela se eles não forem vazios
            for id, *values in usuarios:
                tabela.insert("", tk.END, iid=id, values=values)

        def obter_iid_selecionado(event):
            iid_selecionado = tabela.focus()
            print("IID do item selecionado:", iid_selecionado)

        # Adiciona o bind a função de recarregar a tabela
        frame_pai.bind("<F5>", lambda event: atualizar_tabela())
        entry_pesquisa.bind("<Return>", lambda event: atualizar_tabela())
        tabela.bind("<<TreeviewSelect>>", obter_iid_selecionado)
        # Adiciona uma barra de rolagem
        scrollbar = ttk.Scrollbar(
            frame_tabela, orient=tk.VERTICAL, command=tabela.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        tabela.configure(yscrollcommand=scrollbar.set)

        # Configuração para expandir a tabela e a barra de rolagem com o tamanho do frame_tabela
        frame_tabela.columnconfigure(0, weight=1)
        frame_tabela.rowconfigure(0, weight=1)

    cria_tabela_usuarios(frame)
