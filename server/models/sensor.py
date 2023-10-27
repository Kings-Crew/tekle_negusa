#Här definieras ett pydantiskt schema som representerar hur sensordata kommer att lagras MongoDB atlas-databas.

class StudentSchema(BaseModel):
    sensorvalue: str = Field(...)
    time: float = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "sensorvalue": "xxxx",
                "time": "dd:mm:yyyy-hh:mm:ss",
            }
        }


class UpdateStudentModel(BaseModel):
    sensorvalue: Optional[str]
    time: Optional[float]
    

    class Config:
        schema_extra = {
            "example": {
                "sensorvalue": "xxxx",
                "time": "dd:mm:yyyy-hh:mm:ss"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}