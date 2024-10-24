# Code with FastAPI (app = FastAPI(...))


from fastapi import FastAPI
from src.web_service.lib.inference import infer_age
from src.web_service.lib.models import InputSchema, PredictionResponseSchema

# Other imports

app = FastAPI(title="Artefact MLOps Project", description="Very simple API using the ")


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionResponseSchema, status_code=201)
def predict(payload: InputSchema) -> dict:
    # TODO: complete and replace the "InsertHereAPydanticClass" with the correct Pydantic classes defined in web_service/lib/models.py
    prediction = infer_age(payload)
    return {"abalone_age_prediction": y}
    
