from fastapi import FastAPI

app = FastAPI()


@app.post('/')
def create():
    return {'Hello': 'post'}


@app.get('/')
def read():
    return {'Hello': 'get'}


@app.put('/')
def update():
    return {'Hello': 'put'}


@app.delete('/{_id}')
def delete(_id: int):
    return {'Hello': f'delete {_id}'}
