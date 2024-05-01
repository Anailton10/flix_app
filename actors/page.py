from datetime import datetime

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Gêneros')

        actor_df = pd.json_normalize(actors)
        AgGrid(data=actor_df,
               reload_data=True,
               key='actors_grid',
               )
    else:
        st.warning('Nenhum ator/atriz encontrado(a)')

    st.title('Cadastrar Novo Ator/Atriz')

    name = st.text_input('Nome do Ator')

    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality_dropdown = ['BRAZIL', 'USA']

    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )

    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Error ao cadastrar, verifique os campos!!')
