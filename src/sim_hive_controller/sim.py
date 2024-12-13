from fastapi import FastAPI, HTTPException

from ._pv import PV
from ._signal_generator import Signal_Generator

app = FastAPI()

polling_rate = PV("polling_rate", 10, True, True)
temperature = PV("temperature", Signal_Generator("sin"), True, False)
humidity = PV("humidity", Signal_Generator("square"), True, False)


values = {
    "temperature": temperature,
    "humidity": humidity,
    "polling_rate": polling_rate,
}


# Define a root route
@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/get_vals")
def get_val(fields: str):
    response: dict = {}
    requested_fields: list = fields.split(",")
    for field in requested_fields:
        if thisField := values.get(field, None):
            if PV.is_getable(thisField):
                response[field] = thisField.curr()
            else:
                raise HTTPException(status_code=402, detail="Field is not settable")
    return response


@app.get("/set_vals")
def set_val(field: str, value: str):
    if thisField := values.get(field, None):
        if PV.is_setable(thisField):
            thisField.set_value(float(value))
        else:
            raise HTTPException(status_code=402, detail="Field is not settable")

    return {field: value}
