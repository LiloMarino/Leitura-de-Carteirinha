# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import Canvas, Entry, Text, Button, PhotoImage, ttk
import sys
import tkinter as tk

from cruds.Usuario import cadastrar_usuario
from widgets_functions import cria_menu_cursos


ASSETS_PATH = Path(__file__).parent / "assets" / "frame0"
ROOT_PATH = Path(__file__).parent.parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.append(str(ROOT_PATH))
from Telas.defs import *
from cruds.Curso import consultar_cursos


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def criar_tela_cadastro_usuarios(frame: ttk.Frame, imagens: dict[str, dict]):
    # Imagens
    imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
    imagens["entry_1"] = PhotoImage(file=relative_to_assets("entry_1.png"))
    imagens["entry_2"] = PhotoImage(file=relative_to_assets("entry_2.png"))
    imagens["entry_3"] = PhotoImage(file=relative_to_assets("entry_3.png"))
    imagens["image_2"] = PhotoImage(file=relative_to_assets("image_2.png"))
    imagens["image_3"] = PhotoImage(file=relative_to_assets("image_3.png"))
    imagens["button_1"] = PhotoImage(file=relative_to_assets("button_1.png"))

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

    canvas.create_text(
        514.0,
        42.0,
        anchor="nw",
        text="CADASTRO DE USUÁRIOS",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 48 * -1),
    )

    canvas.create_text(
        67.0,
        172.0,
        anchor="nw",
        text="NOME:",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 48 * -1),
    )
    canvas.create_text(
        67.0,
        293.0,
        anchor="nw",
        text="N° DA CARTEIRINHA:",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 48 * -1),
    )
    canvas.create_text(
        67.0,
        426.0,
        anchor="nw",
        text="CURSO",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 48 * -1),
    )
    canvas.create_text(
        67.0,
        550.0,
        anchor="nw",
        text="EMAIL:",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 48 * -1),
    )

    canvas.create_image(112.0, 54.0, image=imagens["image_2"])
    canvas.create_image(1253.0, 54.0, image=imagens["image_3"])

    # Variáveis dos campos
    nome_var = tk.StringVar()
    n_carteirinha_var = tk.StringVar()
    email_var = tk.StringVar()
    id_curso_var = tk.StringVar()

    # Entrada de texto
    entry_nome = Entry(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 25),
        textvariable=nome_var,
    )
    entry_nome.place(x=204.0, y=179.0, width=647.0, height=43.0)

    entry_n_carteirinha = Entry(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 25),
        textvariable=n_carteirinha_var,
    )
    entry_n_carteirinha.place(x=374.0, y=300.0, width=372.0, height=43.0)

    entry_email = Entry(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 25),
        textvariable=email_var,
    )
    entry_email.place(x=214.0, y=557.0, width=647.0, height=43.0)

    cria_menu_cursos(frame, id_curso_var, x=199, y=430)

    button_cadastrar = Button(
        frame,
        image=imagens["button_1"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: cadastrar_usuario(
            nome=nome_var.get(),
            email=email_var.get(),
            id_curso=id_curso_var.get(),
            n_carteirinha=n_carteirinha_var.get(),
        ),
        relief="flat",
    )
    button_cadastrar.place(x=1012.0, y=644.0, width=303.0, height=84.0)
