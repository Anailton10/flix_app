import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

reviews = [
    {
        'id': 1,
        'stars': 9
    },
    {
        'id': 2,
        'stars': 7
    },
    {
        'id': 3,
        'stars': 10
    }
]


def show_reviews():
    st.write('Lista de Avaliações:')

    df = pd.DataFrame(reviews)
    AgGrid(data=df,
           reload_data=True,
           key='reviews_grid',
           )

    # st.title('Cadastrar Novo Filme')
    # name = st.text_input('Nome do Filme')
    # if st.button('Cadastrar'):
    #     st.success(f'Filme "{name}" cadastrado(a) com sucesso!')
