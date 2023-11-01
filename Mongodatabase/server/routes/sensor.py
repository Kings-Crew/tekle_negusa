# JSON-schema
from jsonschema import validate
from pydantic import BaseModel

from pydantic import BaseModel #Detta är en validator som säkerstället att valideringen går rätt till innan den hamnar i vår collection. 


schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "timestamp": {
            "type": "string",
            "format": "date-time"
        }
    },
    "required": ["id", "timestamp"]
}


class sensorschema(BaseModel):
	id: str
	timestamp: str


# Valideringsfunktion
def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
        return True
    except schema.exceptions.ValidationError as err:
        return False