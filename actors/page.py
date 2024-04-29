import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

actors = [
    {
        'id': 1,
        'name': 'Robert Downey Jr.'
    },
    {
        'id': 2,
        'name': 'Scarlett Johansson'
    },
    {
        'id': 3,
        'name': 'Tom Hanks'
    }
]


def show_actors():
    st.write('Lista de Gêneros')

    df = pd.DataFrame(actors)
    AgGrid(data=df,
           reload_data=True,
           key='actors_grid',
           )

    st.title('Cadastrar Novo Ator/Atriz')
    name = st.text_input('Nome do Ator')
    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz "{name}" cadastrado(a) com sucesso!')
