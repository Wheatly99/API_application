# Импорт библиотек
from fastapi import FastAPI
from transformers import pipeline, RobertaTokenizerFast
from pydantic import BaseModel

# Создание объекта класса Item по переданным параметрам в теле HTTP
class Item(BaseModel):
    text: str

# Создание объектов
app = FastAPI()
fill_mask = pipeline("fill-mask", model="sberbank-ai/ruBert-base")

# Вызывается функция при обращении к корню сервера
@app.get('/')
def root():
    return {'message': 'Software engineering project'}

# Вызывается функция при загрузке текста на сервер
# Необходимо доработать, чтобы выводилось больше вариантов (сейчас выводится только один)
@app.post('/predict/')
def predict(item: Item):
    pred = fill_mask(item.text)
    diction = {idx+1 : value for idx, value in enumerate(pred)}
    return diction
