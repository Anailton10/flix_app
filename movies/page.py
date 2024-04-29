import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

movies = [
    {
        'id': 1,
        'title': 'Vingadores: Ultimato'
    },
    {
        'id': 2,
        'title': 'Forrest Gump'
    },
    {
        'id': 3,
        'title': 'O Iluminado'
    }
]


def show_movies():
    st.write('Lista de Filmes')

    df = pd.DataFrame(movies)
    AgGrid(data=df,
           reload_data=True,
           key='movies_grid',
           )

    # st.title('Cadastrar Novo Filme')
    # name = st.text_input('Nome do Filme')
    # if st.button('Cadastrar'):
    #     st.success(f'Filme "{name}" cadastrado(a) com sucesso!')
