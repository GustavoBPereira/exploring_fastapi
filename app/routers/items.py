from fastapi import APIRouter

router = APIRouter()


@router.post('/')
def create():
    return {'Hello': 'post'}


@router.get('/')
def read():
    return {'Hello': 'get'}


@router.put('/')
def update():
    return {'Hello': 'put'}


@router.delete('/{_id}')
def delete(_id: int):
    return {'Hello': f'delete -{_id}'}
