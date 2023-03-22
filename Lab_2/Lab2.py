import gradio as gr
import pandas as pd

def plik(nazwa):
    x = pd.read_csv(nazwa)
    l_wier, la = x.shape
    return x, l_wier

def wer(wiersze, l_wier,x):
    wiersze = int(wiersze)
    if wiersze > 0 and wiersze <= l_wier:
        tab = x.head(wiersze)
        return tab

def wyswietl_tabele(nazwa, wiersze):
    x, l_wier = plik(nazwa)
    tab = wer(wiersze, l_wier,x)

    l_obiekt, l_atrybut = tab.shape

    liczba_decyzji = len(tab['Exited'].unique())
    wielkosc_decyzji = tab['Exited'].value_counts().to_dict()

    dodatki = f'Liczba klas decyzyjnych wynosi = {liczba_decyzji}\nWielkość każdej klasy decyzyjnej wynosi = {wielkosc_decyzji}'
    opis = f'plik zawiera {l_obiekt} obiektów oraz {l_atrybut} atrybotów'
    return opis, dodatki, tab

inp = [gr.inputs.Textbox(label="Nazwa pliku", default="Churn_Modelling.csv"),
        gr.inputs.Number(label="Liczba wyświetlanych wierszy", default=5),]

out = [gr.outputs.Textbox(label="Informacje:"),
       gr.outputs.Textbox(label="Dodatki:"),
       gr.outputs.Textbox(label="Tabela")]

interfejs = gr.Interface(
    fn=wyswietl_tabele,
    inputs=inp,
    outputs=out,
    title="Interfejs do wyświetlania tabeli"
)
interfejs.launch()