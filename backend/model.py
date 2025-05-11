from pydantic import BaseModel, Field
from datetime import datetime

class Values(BaseModel):
    temperature: float = Field(..., gt=-90, lt=60)
    wind_speed: float = Field(..., ge=0, le=200)
    humidity: float = Field(..., ge=0, le=100) 
    
class Model(BaseModel):
    time: datetime
    values: Values
