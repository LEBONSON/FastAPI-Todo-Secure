from pydantic import BaseModel

class Tache(BaseModel):
    titre: str
    description: str
    etat: str
