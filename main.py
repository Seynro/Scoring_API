from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from scoring_model import scoring_func

app = FastAPI(
    title='Trading app'
)


class Param(BaseModel):
    PIN_CODE: str
    UNICAL_CODE: int
    APP_ID: str


@app.post('/scoring')
def scoring(param: list[Param]):
    result = scoring_func(param)
    print(result)
    if result == 'APP_ID' or result == 'UNICAL_CODE' or result == 'PIN_CODE':
        error = result + ' is invalid'
        return {"status": 404, "score": error}
    else:
        return {"status": 200, "score": result}