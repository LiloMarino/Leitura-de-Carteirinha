# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from datetime import date
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkcalendar import DateEntry
import tkinter as tk
import sys
from cruds.Presenca import consultar_presencas_pelo_id

from cruds.Reuniao import atualizar_reuniao, consultar_reuniao_pelo_id


ASSETS_PATH = Path(__file__).parent / "assets" / "frame0"
ROOT_PATH = Path(__file__).parent.parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.append(str(ROOT_PATH))
from Telas.defs import *


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


from tkinter import Tk, Canvas, Text, Button, PhotoImage


def criar_tela_editar_rg(frame: ttk.Frame, imagens: dict[str, dict], id_reuniao: int):
    def criar_imagens():
        imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
        imagens["entry_1"] = PhotoImage(file=relative_to_assets("entry_1.png"))
        imagens["button_1"] = PhotoImage(file=relative_to_assets("button_1.png"))
        imagens["button_2"] = PhotoImage(file=relative_to_assets("button_2.png"))

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
        canvas.create_image(289.0, 92.0, image=imagens["entry_1"])
        canvas.create_text(
            81.0,
            57.0,
            anchor="nw",
            text="Data:",
            fill="#FFFFFF",
            font=(FONTE_TELAS, 48 * -1),
        )
        canvas.create_text(
            36.0,
            142.0,
            anchor="nw",
            text="Lista de usuários:",
            fill="#FFFFFF",
            font=(FONTE_TELAS, 40 * -1),
        )

    def criar_input_data():
        date_entry = DateEntry(master=frame, font=(FONTE_TELAS, 20))
        date_entry.place(x=180.0, y=67.0, width=201.0)
        data_reuniao = consultar_reuniao_pelo_id(id_reuniao)
        date_entry.set_date(data_reuniao)
        return date_entry

    def criar_tabela():
        def criar_frame_tabela():
            frame_tabela = ttk.Frame(frame)
            frame_tabela.place(x=36.0, y=185.0, width=1014.0, height=530.0, anchor="nw")
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
            frame_tabela, columns=("nome", "curso", "presente"), show="headings"
        )
        criar_scrollbar(frame_tabela, tabela)
        tabela.heading("nome", text="Nome")
        tabela.heading("curso", text="Curso")
        tabela.heading("presente", text="Presente")
        tabela.tag_configure("presente", background="pale green")
        tabela.tag_configure("ausente", background="light coral")
        tabela.grid(row=0, column=0, sticky="nsew")
        return tabela

    def atualizar_tabela():
        tabela.delete(*tabela.get_children())
        presentes = consultar_presencas_pelo_id(id_reuniao)
        for id_usuario, nome, curso, presenca in presentes:
            tabela.insert(
                "",
                tk.END,
                iid=id_usuario,
                values=(nome, curso, "Sim" if presenca else "Não"),
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
                valores_atuais[2] = "Não"
                tags_atuais.remove("presente")
                tags_atuais.append("ausente")
            else:
                valores_atuais[2] = "Sim"
                tags_atuais.remove("ausente")
                tags_atuais.append("presente")

            tabela.item(item_id, values=valores_atuais, tags=tags_atuais)

    def deletar_rg():
        ...

    def salvar_rg():
        lista_presencas = []
        todos_itens = tabela.get_children()
        for item_id in todos_itens:
            # Obtém a presença
            valores = tabela.item(item_id, "values")
            presente = 1 if valores[2] == "Sim" else 0

            # Obtém o id do usuário
            tabela.focus(item_id)
            id_usuario = tabela.focus()
            lista_presencas.append((id_usuario, presente))

        atualizar_reuniao(id_reuniao, lista_presencas, date_entry.get_date())

    def obter_iid_selecionado(event):
        iid_selecionado = tabela.focus()
        print("IID do item selecionado:", iid_selecionado)

    def criar_botoes():
        button_salvar = Button(
            frame,
            image=imagens["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: salvar_rg(),
            relief="flat",
        )
        button_salvar.place(x=1154.0, y=342.0, width=170.0, height=68.0)

        button_deletar = Button(
            frame,
            image=imagens["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: deletar_rg(),
            relief="flat",
        )
        button_deletar.place(x=1154.0, y=486.0, width=170.0, height=68.0)

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
        button_editar.place(x=1154.0, y=630.0, width=170.0, height=68.0)

    # Criação e configuração dos elementos da tela
    criar_imagens()
    criar_canvas()
    criar_botoes()
    date_entry = criar_input_data()
    tabela = criar_tabela()
    frame.bind("<F5>", lambda event: atualizar_tabela())
    tabela.bind("<<TreeviewSelect>>", obter_iid_selecionado)
