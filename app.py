import streamlit as st


def main():
    st.title('Flix App')

    menu_option = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Inicio', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações']
    )

    if menu_option == 'Inicio':
        st.write('Inicio')

    if menu_option == 'Gêneros':
        st.write('Lista de Gêneros')

    if menu_option == 'Atores/Atrizes':
        st.write('Lista de Atores/Atrizes')

    if menu_option == 'Filmes':
        st.write('Lista de Filmes')

    if menu_option == 'Avaliações':
        st.write('Lista de Avaliações')


if __name__ == '__main__':
    main()
