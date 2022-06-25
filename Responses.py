from datetime import datetime

def sample_responses(input_text):

    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi'):

        return 'Salve'

    if user_message in ('who are you'):

        return 'Eu sou um bot'

    if user_message in ('time'):

        return str(datetime.now())

    return 'Desconhecido'