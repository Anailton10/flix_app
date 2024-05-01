import requests
import streamlit as st


def verify_status(response, code: int):
    """Verifica o status de uma resposta HTTP e
    retorna o conteúdo em formato JSON, se bem-sucedido.

    Args:
        response (requests.Response): A resposta HTTP a ser verificada.
        code (int): O status code esperado para uma resposta bem-sucedida.

    Raises:
        Exception: Se o status code da resposta não corresponder ao esperado e
        não for 401, uma exceção é levantada com uma mensagem apropriada.

    Returns:
        dict:  Se o status code for igual o esperado retorna no formato Json.
        None : O status for 401 a função logout é chama e retorna None.
    """
    from login.service import logout
    if response.status_code == code:
        return response.json()

    if response.status_code == 401:
        logout()
        return None
    raise Exception(
        f' Erro ao obter dados da API. Status code: {response.status_code}'
    )


class ActorRepository:

    def __init__(self):
        self.__base_url = 'http://107.22.32.210:8000/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__headers
        )

        json_data = verify_status(response=response, code=200)
        return json_data

    def create_actors(self, actor):
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,
            data=actor
        )

        json_data = verify_status(response=response, code=201)
        return json_data
