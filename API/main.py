# Импорт библиотек
from fastapi import FastAPI
from transformers import pipeline, RobertaTokenizerFast
from pydantic import BaseModel

# Создание объекта класса Item по переданным параметрам в теле HTTP
class Item(BaseModel):
    text: str

# Создание объектов
app = FastAPI()
tokenizer = RobertaTokenizerFast.from_pretrained('blinoff/roberta-base-russian-v0', max_len=512)
fill_mask = pipeline("fill-mask", model="blinoff/roberta-base-russian-v0", tokenizer=tokenizer)

# Вызывается функция при обращении к корню сервера
@app.get('/')
def root():
    return {'message': 'Software engineering project'}

# Вызывается функция при загрузки текста на сервер
# Необходимо доработать,чтобы выводилось больше вариантов (сейчас выводится только один)
@app.post('/predict/')
def predict(item: Item):
    return fill_mask(item.text)[0]