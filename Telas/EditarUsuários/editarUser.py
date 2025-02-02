# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


import tkinter as tk
from datetime import date
from msilib.text import tables
from pathlib import Path
from tkinter import Button, Canvas, Entry, PhotoImage, Tk, ttk

from cruds.Presenca import (atualizar_presencas_pelo_usuario,
                            consultar_dias_presentes,
                            consultar_presencas_pelo_usuario)
from cruds.Usuario import atualizar_usuario, consultar_usuario_pelo_id
from widgets_functions import cria_menu_cursos

ASSETS_PATH = Path(__file__).parent / "assets" / "frame0"

from Telas.defs import *


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def criar_tela_edicao_usuarios(
    frame: ttk.Frame, imagens: dict[str, dict], id_usuario: int
):
    def criar_imagens():
        imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
        imagens["image_2"] = PhotoImage(file=relative_to_assets("image_2.png"))
        imagens["entry_1"] = PhotoImage(file=relative_to_assets("entry_1.png"))
        imagens["entry_2"] = PhotoImage(file=relative_to_assets("entry_2.png"))
        imagens["entry_3"] = PhotoImage(file=relative_to_assets("entry_3.png"))
        imagens["button_3"] = PhotoImage(file=relative_to_assets("button_3.png"))

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
        canvas.create_image(569.0, 648.0, image=imagens["image_2"])
        canvas.create_image(391.0, 152.5, image=imagens["entry_1"])
        canvas.create_image(458.0, 241.5, image=imagens["entry_2"])
        canvas.create_image(391.5, 424.5, image=imagens["entry_3"])
        canvas.create_text(
            514.0,
            25.0,
            anchor="nw",
            text="EDIÇÃO DE USUÁRIOS",
            fill="#FFFFFF",
            font=(FONTE_TELAS, 48 * -1),
        )
        canvas.create_text(
            22.0,
            132.0,
            anchor="nw",
            text="NOME:",
            fill="#FFFFFF",
            font=(FONTE_TELAS, 40 * -1),
        )
        canvas.create_text(
            22.0,
            219.0,
            anchor="nw",
            text="N° DE CARTEIRINHA:",
            fill="#FFFFFF",
            font=(FONTE_TELAS, 40 * -1),
        )
        canvas.create_text(
            22.0,
            302.0,
            anchor="nw",
            text="CURSO",
            fill="#FFFFFF",
            font=(FONTE_TELAS, 40 * -1),
        )
        canvas.create_text(
            22.0,
            403.0,
            anchor="nw",
            text="EMAIL:",
            fill="#FFFFFF",
            font=(FONTE_TELAS, 40 * -1),
        )
        canvas.create_text(
            22.0,
            484.0,
            anchor="nw",
            text="N° DE DIAS PRESENTES:",
            fill="#FFFFFF",
            font=(FONTE_TELAS, 40 * -1),
        )

    def configurar_variaveis():
        nome, n_carteirinha, email, curso = consultar_usuario_pelo_id(id_usuario)
        nome_var = tk.StringVar(value=nome)
        id_curso_var = tk.StringVar()
        n_carteirinha_var = tk.StringVar(value=n_carteirinha)
        email_var = tk.StringVar(value=email)
        n_presencas_var = tk.StringVar(value=consultar_dias_presentes(id_usuario))
        return (
            nome_var,
            id_curso_var,
            n_carteirinha_var,
            email_var,
            curso,
            n_presencas_var,
        )

    def criar_entry(frame, text_variable, x, y, width, height):
        entry = Entry(
            frame,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=(FONTE_INPUT, 25),
            textvariable=text_variable,
        )
        entry.place(x=x, y=y, width=width, height=height)
        return entry

    def criar_tabela():
        def criar_frame_tabela():
            frame_tabela = ttk.Frame(frame)
            frame_tabela.place(x=743.0, y=109.0, width=553.0, height=550.0, anchor="nw")
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
            frame_tabela, columns=("data_rg", "presente"), show="headings"
        )
        criar_scrollbar(frame_tabela, tabela)
        tabela.heading("data_rg", text="Data da RG")
        tabela.heading("presente", text="Presente")
        tabela.tag_configure("presente", background="pale green")
        tabela.tag_configure("ausente", background="light coral")
        tabela.grid(row=0, column=0, sticky="nsew")
        return tabela

    def atualizar_tabela():
        tabela.delete(*tabela.get_children())
        reunioes = consultar_presencas_pelo_usuario(id_usuario)
        for id_reuniao, data, presenca in reunioes:
            data: date
            tabela.insert(
                "",
                tk.END,
                iid=id_reuniao,
                values=(data.strftime("%d/%m/%Y"), "Sim" if presenca else "Não"),
                tags="presente" if presenca else "ausente",
            )

    def alternar_presenca():
        itens_selecionados = tabela.selection()

        for item_id in itens_selecionados:
            # Obtém os dados do item
            valores_atuais = tabela.item(item_id, "values")
            tags_atuais = tabela.item(item_id, "tags")
            valores_atuais = list(valores_atuais)
            tags_atuais = list(tags_atuais)
            # Alterna a presença
            if "presente" in tags_atuais:
                valores_atuais[1] = "Não"
                tags_atuais.remove("presente")
                tags_atuais.append("ausente")
            else:
                valores_atuais[1] = "Sim"
                tags_atuais.remove("ausente")
                tags_atuais.append("presente")

            tabela.item(item_id, values=valores_atuais, tags=tags_atuais)

    def atualizar_presencas():
        lista_presencas = []
        todos_itens = tabela.get_children()
        for item_id in todos_itens:
            # Obtém a presença
            valores = tabela.item(item_id, "values")
            presente = 1 if valores[1] == "Sim" else 0

            # Obtém o id do usuário
            tabela.focus(item_id)
            id_reuniao = tabela.focus()
            lista_presencas.append((id_reuniao, presente))

        atualizar_presencas_pelo_usuario(id_usuario, lista_presencas)
        
        n_presencas_var.set(consultar_dias_presentes(id_usuario))

    def criar_botoes():
        button_editar = Button(
            master=frame,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: alternar_presenca(),
            relief="flat",
            text="Alternar\nPresença",
            font=(FONTE_TELAS, 20),
            background="#FFD708",
            activebackground="#FFD708",
        )
        button_editar.place(x=1126.0, y=665.0, width=170.0, height=68.0)

        button_salvar = Button(
            frame,
            image=imagens["button_3"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (
                atualizar_usuario(
                    id_usuario=id_usuario,
                    nome=nome_var.get(),
                    email=email_var.get(),
                    id_curso=id_curso_var.get(),
                    n_carteirinha=n_carteirinha_var.get(),
                ),
                atualizar_presencas(),
            ),
            relief="flat",
        )
        button_salvar.place(x=125.0, y=606.0, width=325.0, height=84.0)

    def criar_menu_cursos():
        menu_cursos = cria_menu_cursos(
            frame=frame, id_curso_var=id_curso_var, x=135, y=303
        )
        menu_cursos.set(curso)
        menu_cursos.event_generate("<<ComboboxSelected>>")

    # Criação e configuração dos elementos da tela
    criar_imagens()
    criar_canvas()
    tabela = criar_tabela()
    (
        nome_var,
        id_curso_var,
        n_carteirinha_var,
        email_var,
        curso,
        n_presencas_var,
    ) = configurar_variaveis()
    criar_entry(frame, nome_var, 126.0, 130.0, 530.0, 43.0)
    criar_entry(frame, n_carteirinha_var, 272.0, 219.0, 372.0, 43.0)
    criar_entry(frame, email_var, 139.0, 402.0, 505.0, 43.0)
    entry_presencas = criar_entry(frame, n_presencas_var, 307.0, 484.0, 87.0, 45.0)
    entry_presencas.config(state="disabled", justify="center")
    criar_botoes()
    criar_menu_cursos()
    frame.bind("<F5>", lambda event: atualizar_tabela())
