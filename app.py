from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator
import asyncio


# ==========================================
# JANELA PRINCIPAL
# ==========================================

root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')


# ==========================================
# FRAME
# ==========================================

frame1 = Frame(
    root,
    width=590,
    height=370,
    relief=RIDGE,
    borderwidth=5,
    bg='#F7DC6F'
)

frame1.place(x=0, y=0)


# ==========================================
# TÍTULO
# ==========================================

Label(
    root,
    text='Language Translator',
    font=('Helvetica', 20, 'bold'),
    fg='black',
    bg='#F7DC6F'
).pack(pady=10)


# ==========================================
# IDIOMAS
# ==========================================

languages = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Azerbaijani': 'az',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Chichewa': 'ny',
    'Chinese': 'zh-cn',
    'Corsican': 'co',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'tl',
    'Finnish': 'fi',
    'French': 'fr',
    'Frisian': 'fy',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian Creole': 'ht',
    'Hausa': 'ha',
    'Hawaiian': 'haw',
    'Hebrew': 'he',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Macedonian': 'mk',
    'Malagasy': 'mg',
    'Malay': 'ms',
    'Malayalam': 'ml',
    'Maltese': 'mt',
    'Maori': 'mi',
    'Marathi': 'mr',
    'Mongolian': 'mn',
    'Myanmar': 'my',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Odia': 'or',
    'Pashto': 'ps',
    'Persian': 'fa',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Punjabi': 'pa',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Samoan': 'sm',
    'Scots Gaelic': 'gd',
    'Serbian': 'sr',
    'Sesotho': 'st',
    'Shona': 'sn',
    'Sindhi': 'sd',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Somali': 'so',
    'Spanish': 'es',
    'Sundanese': 'su',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tajik': 'tg',
    'Tamil': 'ta',
    'Tatar': 'tt',
    'Telugu': 'te'
}


# ==========================================
# FUNÇÃO ASSÍNCRONA DE TRADUÇÃO
# ==========================================

async def make_translation(text, language_code):

    async with Translator() as translator:

        result = await translator.translate(
            text,
            dest=language_code
        )

        return result.text


# ==========================================
# FUNÇÃO DO BOTÃO TRANSLATE
# ==========================================

def translate():

    # Pega o texto digitado
    text = text_entry1.get(
        "1.0",
        "end-1c"
    ).strip()

    # Pega o idioma escolhido
    selected_language = choose_language.get()

    # --------------------------------------
    # Verifica se existe texto
    # --------------------------------------

    if text == '':
        messagebox.showerror(
            'Language Translator',
            'Enter the text to translate!'
        )
        return

    # --------------------------------------
    # Verifica se existe idioma
    # --------------------------------------

    if selected_language == '':
        messagebox.showerror(
            'Language Translator',
            'Choose a language!'
        )
        return

    try:

        # Pega o código do idioma
        language_code = languages[selected_language]

        print("-----------------------------------")
        print("Texto:", text)
        print("Idioma escolhido:", selected_language)
        print("Código:", language_code)

        # ----------------------------------
        # FAZ A TRADUÇÃO
        # ----------------------------------

        translated_text = asyncio.run(
            make_translation(
                text,
                language_code
            )
        )

        # ----------------------------------
        # MOSTRA NO TERMINAL
        # ----------------------------------

        print("Tradução:", translated_text)
        print("-----------------------------------")

        # ----------------------------------
        # LIMPA A CAIXA DE SAÍDA
        # ----------------------------------

        text_entry2.delete(
            "1.0",
            "end"
        )

        # ----------------------------------
        # MOSTRA A TRADUÇÃO
        # ----------------------------------

        text_entry2.insert(
            "1.0",
            translated_text
        )

    except Exception as error:

        print("-----------------------------------")
        print("ERRO:", error)
        print("-----------------------------------")

        messagebox.showerror(
            'Translation Error',
            f'An error occurred:\n\n{error}'
        )


# ==========================================
# FUNÇÃO CLEAR
# ==========================================

def clear():

    text_entry1.delete(
        "1.0",
        "end"
    )

    text_entry2.delete(
        "1.0",
        "end"
    )


# ==========================================
# COMBOBOX - IDIOMA DE ORIGEM
# ==========================================

a = tk.StringVar()

auto_select = ttk.Combobox(
    frame1,
    width=27,
    textvariable=a,
    state='readonly',
    font=('verdana', 10, 'bold')
)

auto_select['values'] = (
    'Auto Select',
)

auto_select.place(
    x=15,
    y=60
)

auto_select.current(0)


# ==========================================
# COMBOBOX - IDIOMA DE DESTINO
# ==========================================

l = tk.StringVar()

choose_language = ttk.Combobox(
    frame1,
    width=27,
    textvariable=l,
    state='readonly',
    font=('verdana', 10, 'bold')
)

choose_language['values'] = tuple(
    languages.keys()
)

choose_language.place(
    x=305,
    y=60
)

# Português como idioma inicial
choose_language.set('Portuguese')


# ==========================================
# CAIXA DE TEXTO - ENTRADA
# ==========================================

text_entry1 = Text(
    frame1,
    width=20,
    height=7,
    borderwidth=5,
    relief=RIDGE,
    font=('verdana', 15)
)

text_entry1.place(
    x=10,
    y=100
)


# ==========================================
# CAIXA DE TEXTO - SAÍDA
# ==========================================

text_entry2 = Text(
    frame1,
    width=20,
    height=7,
    borderwidth=5,
    relief=RIDGE,
    font=('verdana', 15)
)

text_entry2.place(
    x=300,
    y=100
)


# ==========================================
# BOTÃO TRANSLATE
# ==========================================

btn1 = Button(
    frame1,
    command=translate,
    text='Translate',
    relief=RAISED,
    borderwidth=2,
    font=('verdana', 10, 'bold'),
    bg='#248aa2',
    fg='white',
    cursor='hand2'
)

btn1.place(
    x=185,
    y=300
)


# ==========================================
# BOTÃO CLEAR
# ==========================================

btn2 = Button(
    frame1,
    command=clear,
    text='Clear',
    relief=RAISED,
    borderwidth=2,
    font=('verdana', 10, 'bold'),
    bg='#248aa2',
    fg='white',
    cursor='hand2'
)

btn2.place(
    x=300,
    y=300
)


# ==========================================
# INICIA O PROGRAMA
# ==========================================

root.mainloop()