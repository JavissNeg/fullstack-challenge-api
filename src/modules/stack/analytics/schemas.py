from pydantic import BaseModel, Field

class StackStats(BaseModel):
    """
    Estadísticas de preguntas de Stack Exchange.
    """
    total: int = Field(
        ...,
        description="Número total de preguntas encontradas",
        examples=[50]
    )
    answered: int = Field(
        ...,
        description="Número de preguntas contestadas",
        examples=[35]
    )
    not_answered: int = Field(
        ...,
        description="Número de preguntas sin contestar",
        examples=[15]
    )

    class Config:
        schema_extra = {
            "example": {
                "total": 50,
                "answered": 35,
                "not_answered": 15
            }
        }

class HighestReputation(BaseModel):
    """
    Usuario con mayor reputación.
    """
    user: str = Field(
        ...,
        description="Nombre de usuario del usuario con mayor reputación",
        examples=["Jon Skeet"]
    )
    reputation: int = Field(
        ...,
        description="Puntuación de reputación del usuario",
        examples=[1500000]
    )
    question: str = Field(
        ...,
        description="Título de la pregunta realizada por este usuario",
        examples=["¿Cómo analizar JSON en JavaScript?"]
    )

    class Config:
        schema_extra = {
            "example": {
                "user": "Jon Skeet",
                "reputation": 1500000,
                "question": "¿Cómo analizar JSON en JavaScript?"
            }
        }

class LowestViews(BaseModel):
    """
    Pregunta con menos vistas.
    """
    title: str = Field(
        ...,
        description="Título de la pregunta",
        examples=["Ayuda con regex de Perl oscuro"]
    )
    views: int = Field(
        ...,
        description="Número de vistas de la pregunta",
        examples=[12]
    )

    class Config:
        schema_extra = {
            "example": {
                "title": "Ayuda con regex de Perl oscuro",
                "views": 12
            }
        }

class QuestionAge(BaseModel):
    """
    Información de edad de pregunta.
    """
    title: str = Field(
        ...,
        description="Título de la pregunta",
        examples=["Pregunta antigua de Perl de 2010"]
    )
    creation_date: int = Field(
        ...,
        description="Fecha de creación de la pregunta como timestamp Unix",
        examples=[1262304000]
    )

    class Config:
        schema_extra = {
            "example": {
                "title": "Pregunta antigua de Perl de 2010",
                "creation_date": 1262304000
            }
        }