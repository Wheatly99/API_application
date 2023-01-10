import streamlit as st
import json
import requests
import sys
import argparse

st.title('Заполнение пропусков в словах')
st.text('Это приложение реализовано в рамках "Software engineering project"')


text_input = st.text_input(label='Введите предложение, замените одно слово на [MASK]'
                                 'и нажмите кнопку, или просто нажмите enter',
                           value='Введите предложение, замените одно слово на [MASK] и нажмите кнопку')


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip_api', default='127.0.0.1')
    parser.add_argument('port_api', default='8000')
    return parser

def predict():
    diction = {"text": text_input}

    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    result = requests.post(url=f"http://{namespace.ip_api}:{namespace.port_api}/predict", data=json.dumps(diction)).json()

    print(result)
    for variant in result:
        s: str = result[variant]['sequence']
        predicted: str = result[variant]['token_str']
        formated = s.replace(predicted, f' **{predicted.replace(" ","")}**')
        st.markdown(formated.capitalize())


st.button(label='Тык!', on_click=predict())