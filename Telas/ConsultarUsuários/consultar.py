# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import tkinter as tk
from pathlib import Path
from tkinter import Button, Canvas, Entry, PhotoImage, Text, messagebox, ttk

from cruds.Usuario import consultar_usuarios, deletar_usuarios
from tab_functions import abrir_aba_editar_usuario

ASSETS_PATH = Path(__file__).parent / "assets" / "frame0"

from Telas.defs import *


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def criar_tela_consultar_usuarios(
    frame: ttk.Frame,
    imagens: dict[str, dict],
    notebook: ttk.Notebook,
    imagens_dict: dict[str, dict],
):
    def criar_imagens():
        imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
        imagens["entry_1"] = PhotoImage(file=relative_to_assets("entry_1.png"))
        imagens["button_1"] = PhotoImage(file=relative_to_assets("button_1.png"))
        imagens["button_2"] = PhotoImage(file=relative_to_assets("button_2.png"))
        imagens["image_2"] = PhotoImage(file=relative_to_assets("image_2.png"))
        imagens["button_3"] = PhotoImage(file=relative_to_assets("button_3.png"))
        imagens["image_3"] = PhotoImage(file=relative_to_assets("image_3.png"))

    def criar_canvas():
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

    def criar_input_pesquisa():
        pesquisa = tk.StringVar()
        entry_pesquisa = Entry(
            frame,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=pesquisa,
            font=(FONTE_INPUT, 28),
        )
        entry_pesquisa.place(x=174.0, y=60.0, width=867.0, height=44.0)
        return pesquisa, entry_pesquisa

    def criar_botoes():
        button_pesquisa = Button(
            frame,
            image=imagens["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: atualizar_tabela(),
            relief="flat",
        )
        button_pesquisa.place(x=1124.0, y=55.0, width=176.0, height=60.0)

        button_deletar = Button(
            frame,
            image=imagens["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=confirmar_exclusao,
            relief="flat",
        )
        button_deletar.place(x=1076.0, y=651.0, width=268.0, height=68.0)

        button_editar = Button(
            master=frame,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: abrir_aba_editar_usuario(
                notebook, imagens_dict, tabela.focus()
            ),
            relief="flat",
            text="Editar Usuário",
            font=(FONTE_TELAS, 40),
            background="#FFD708",
            activebackground="#FFD708",
        )
        button_editar.place(x=1076.0, y=551.0, width=268.0, height=68.0)

    def criar_tabela():
        def criar_frame_tabela():
            frame_tabela = ttk.Frame(frame)
            frame_tabela.place(x=36.0, y=185.0, width=1015.0, height=550.0, anchor="nw")
            frame_tabela.columnconfigure(0, weight=1)
            frame_tabela.rowconfigure(0, weight=1)
            return frame_tabela

        def criar_scrollbar(frame_tabela, tabela):
            scrollbar = ttk.Scrollbar(
                frame_tabela, orient=tk.VERTICAL, command=tabela.yview
            )
            scrollbar.grid(row=0, column=1, sticky="ns")
            tabela.configure(yscrollcommand=scrollbar.set)

        frame_tabela = criar_frame_tabela()
        tabela = ttk.Treeview(
            frame_tabela, columns=("nome", "matrícula", "curso"), show="headings"
        )
        criar_scrollbar(frame_tabela, tabela)
        tabela.heading("nome", text="Nome")
        tabela.heading("matrícula", text="Matrícula")
        tabela.heading("curso", text="Curso")
        tabela.grid(row=0, column=0, sticky="nsew")
        return tabela

    def atualizar_tabela():
        termo_pesquisado = pesquisa.get() if pesquisa.get() != "" else None
        tabela.delete(*tabela.get_children())
        usuarios = consultar_usuarios(termo_pesquisado)
        for id, *values in usuarios:
            tabela.insert("", tk.END, iid=id, values=values)

    def obter_iid_selecionado(event):
        iid_selecionado = tabela.focus()
        print("IID do item selecionado:", iid_selecionado)

    def confirmar_exclusao():
        usuarios_ids = list(tabela.selection())
        msg = "Deseja excluir estes usuários?\n"
        for usuario_id in usuarios_ids:
            item = tabela.item(usuario_id)
            msg += f"{item['values'][0]}\n"  # Acessa o nome (índice 0)
        resposta = messagebox.askyesno(title="Confirmação de exclusão", message=msg)
        if resposta:
            deletar_usuarios(usuarios_ids)
            atualizar_tabela()

    # Criação e configuração dos elementos da tela
    criar_imagens()
    criar_canvas()
    pesquisa, entry_pesquisa = criar_input_pesquisa()
    criar_botoes()
    tabela = criar_tabela()

    # Configuração e interação com a tabela
    frame.bind("<F5>", lambda event: atualizar_tabela())
    entry_pesquisa.bind("<Return>", lambda event: atualizar_tabela())
    tabela.bind("<<TreeviewSelect>>", obter_iid_selecionado)
