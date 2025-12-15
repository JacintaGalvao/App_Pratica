import streamlit as st
from streamlit_option_menu import option_menu
#import numpy as np
import pandas as pd
import openpyxl
#import matplotlib.pyplot as plt
#import time
#import re
#from dateline impot date 
st.header("Introduzindo os Elementos do Streamlit")
menu=option_menu(menu_title ="Menu", 
                     options=["inicio","Gráficos estaticos", "Gráficos denâmicos", "Widgets", "Formulário"],
                     icons=["house", "bar-chart", "bar-chart-line", "toggles", "bar-chart" ],
                     menu_icon="cast",
                     default_index=0,
                     orientation="horizontal") 

with st.sidebar: 
  st.success("**UPLOAD DE DADOS**")
  dados = st.file_uploader("carregue ..-", type=["xlsx","xls"])
  if dados: 
    def carregar_dados(dados):
      try:
        df=pd.read_excel(dados)
        return df
      except FileNotFoundError:
        return pd.DataFrame()
    df=carregar_dados(dados)
    st.table(df)
  else:
    st.info("Carregar um ficheiro Excel para começar")

if menu == "Inicio":
  with st.expander("**Sobre o Instetuto Nacional de Estatística**"):
    st.write("Acess o site WWW.ine.cv")st.image("INE.png")

if  menu == "widgets":
  bt = st.button("Dê um clique!")
  if bt:
    st.info("Clicaste num botão acima!")

  sd = st.slider("Mova o ponto do slider!", min_values=25, \
                max_value=35, value=30, step=1)
  testo = f"Eu tenho {sd} anos!"
  st.success(texto)

