import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

genres = [
    {
        'id': 1,
        'name': 'Ação'
    },
    {
        'id': 2,
        'name': 'Comédia'
    },
    {
        'id': 3,
        'name': 'Terror'
    },
]


def show_genres():
    st.write('Lista de Gêneros')

    df = pd.DataFrame(genres)
    AgGrid(data=df,
           reload_data=True,
           key='genres_grid',
           )

    st.title('Cadastrar Novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        st.success(f'Genêro "{name}" cadastrado com sucesso!')
