import streamlit as st
from streamlit_option_menu import option_menu
#import numpy as np
#importpandas as pd
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

with st.sidebert: 
  st.sucess("**UPLOAD DE DADOS**")
  dados = st.title_uploader("carregue ..-", type=["xlsx","xls"])
  if dados: 
    def carregar_dados(dados):
      try:
        df=pd.read_excel(dados)
        return df
      except FilenotFoundError:
        Return pd.DataFrame ()
    df= = carregar_dados(daDOS)
    st.TABLE(df)

else:
    st.info("Carregar um ficheiro Excel para começar")
