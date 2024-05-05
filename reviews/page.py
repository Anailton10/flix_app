import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from movies.service import MovieService
from reviews.service import ReviewService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_review()
    if reviews:
        st.write('Lista de Avaliações:')

        reviews_df = pd.json_normalize(reviews)
        AgGrid(data=reviews_df,
               reload_data=True,
               key='reviews_grid',
               )
    else:
        st.warning('Nenhuma avaliação encontrado')

    st.title('Cadastrar Nova avaliação')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_title = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_title.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )

    comment = st.text_area('Comentário')
    if st.button('Cadastrar'):
        new_review = review_service.create_review(
            movie=movie_title[selected_movie_title],
            stars=stars,
            comment=comment,
        )
        
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar review, verifique os campos.')
