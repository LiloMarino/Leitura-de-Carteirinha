# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import tkinter as tk
import sys
from cruds.Conexao import Conexao
from cruds.Presenca import ler_carteirinha
from tab_functions import abrir_aba_comecar_rg
from Telas.defs import *

ASSETS_PATH = Path(__file__).parent / "assets" / "frame0"
ROOT_PATH = Path(__file__).parent.parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.append(str(ROOT_PATH))


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def criar_tela_leitura(
    frame: ttk.Frame,
    imagens: dict[str, dict],
    notebook: ttk.Notebook,
    imagens_dict: dict[str, dict],
    id_reuniao: int,
    local_de_salvamento: Path,
):
    # Imagens
    imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
    imagens["image_2"] = PhotoImage(file=relative_to_assets("image_2.png"))
    imagens["entry_image"] = PhotoImage(file=relative_to_assets("entry_1.png"))
    imagens["button_image_1"] = PhotoImage(file=relative_to_assets("button_1.png"))
    imagens["button_image_2"] = PhotoImage(file=relative_to_assets("button_2.png"))

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

    # Adiciona imagens ao canvas
    canvas.create_image(682.0, 384.0, image=imagens["image_1"])
    canvas.create_image(683.0, 275.0, image=imagens["image_2"])
    canvas.create_image(703.5, 524.0, image=imagens["entry_image"])

    # Entrada de texto
    entry_1 = Text(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 35),
    )
    entry_1.place(x=520.0, y=490.0, width=367.0, height=66.0)

    n_carteirinha_var = tk.StringVar()

    # Botões
    button_enviar = Button(
        frame,
        image=imagens["button_image_1"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ler_carteirinha(n_carteirinha_var, id_reuniao),
        relief="flat",
    )
    button_enviar.place(x=552.0, y=610.0, width=261.0, height=92.0)

    button_terminar = Button(
        frame,
        image=imagens["button_image_2"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: terminar_reuniao(local_de_salvamento),
        relief="flat",
    )
    button_terminar.place(x=33.0, y=681.0, width=143.0, height=47.0)

    def terminar_reuniao(local_de_salvamento):
        notebook.forget(frame)
        abrir_aba_comecar_rg(notebook, imagens_dict)
        Conexao.fazer_backup(local_de_salvamento)
