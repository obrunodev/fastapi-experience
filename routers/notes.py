from fastapi import APIRouter
from schemas.notes import NoteSchema

router = APIRouter(tags=['Notes'], prefix='/notes')


@router.get('/', response_model=list[NoteSchema])
def get_notes():
    return [
        {
            'title': 'Lavar o carro',
            'description': 'Usar produtos XYZ',
        },
        {
            'title': 'Lavar o carro',
            'description': 'Usar produtos XYZ',
        },
        {
            'title': 'Lavar o carro',
            'description': 'Usar produtos XYZ',
        },
    ]
