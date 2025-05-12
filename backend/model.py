from pydantic import BaseModel, Field

class Values(BaseModel):
    temperature: float = Field(..., gt=-90, lt=60)
    wind_speed: float = Field(..., ge=0, le=200)
    humidity: float = Field(..., ge=0, le=100) 

class Measurement(BaseModel):
    time: str
    values: Values

class Model(BaseModel):
    date: str
    measurement: Measurement
