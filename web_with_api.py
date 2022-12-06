import streamlit as st
import json
import requests

st.title('Заполнение пропусков в словах')
st.text('Это приложение реализовано в рамках "Software engineering project"')


text_input = st.text_input(label='Введите предложение, замените одно слово на [MASK]'
                                 'и нажмите кнопку, или просто нажмите enter',
                           value='Введите предложение, замените одно слово на [MASK] и нажмите кнопку')


def predict():
    diction = {"text": text_input}
    result = requests.post(url="http://127.0.0.1:8000/predict", data=json.dumps(diction)).json()
    print(result)
    for variant in result:
        s: str = result[variant]['sequence']
        predicted: str = result[variant]['token_str']
        formated = s.replace(predicted, f' **{predicted.replace(" ","")}**')
        st.markdown(formated.capitalize())


st.button(label='Тык!', on_click=predict())