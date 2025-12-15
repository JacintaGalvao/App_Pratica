import streamlit as st
from streamlit_option_menu import option_menu
#import numpy as np
#importpandas as pd
#import matplotlib.pyplot as plt
#import time
#import re
#from dateline impot date 
st.header("Introduzindo os Elementos do Streamlit")
menu =  option_menu (menu_title ="Menu", 
                     options=["inicio","Gráficos estaticos", "Gráficos denâmicos", "Widgets", "Formulário"],
                     icons=["house", "bar-chart", "bar-chart-line", "toggles", "bar-chart" ],
                     menu_icon="cast",
                     defaukt_ibdex=0,
                     orientation="horizontal")
