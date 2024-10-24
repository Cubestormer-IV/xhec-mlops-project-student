# Code with FastAPI (app = FastAPI(...))


from fastapi import FastAPI

# Other imports

app = FastAPI(title="...", description="...")


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionResponseSchema, status_code=201)
def predict(payload: InputSchema) -> dict:
    # TODO: complete and replace the "InsertHereAPydanticClass" with the correct Pydantic classes defined in web_service/lib/models.py
