from pydantic import BaseModel


class InputSchema(BaseModel):
    Sex: str
    Length: float
    Diameter: float
    Height: float
    Whole_weight: float
    Shucked_weight: float
    Viscera_weight: float
    Shell_weight: float

class PredictionResponseSchema(BaseModel):
    predicted_age: float