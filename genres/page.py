import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros')

        genre_df = pd.json_normalize(genres)
        AgGrid(
            data=genre_df,
            reload_data=True,
            key='genres_grid',
        )
    else:
        st.warning('Nenhum gênero encontrado.')

    st.title('Cadastrar Novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(name=name)

        if new_genre:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o gênero. Verifique o campo')
