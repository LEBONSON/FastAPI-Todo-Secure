from fastapi import FastAPI
from schemas.tache import Tache

app = FastAPI()
@app.get("/")
def getAllTache():
    return {"message":"Recupération de toutes les taches"}

@app.get("/taches/{tache_id}")
def getTache(tache_id : int ):
    return {"tache_id":tache_id,
            "titre":f"Recupération des infos de la Tache{tache_id}"}

@app.post("/taches/")
def createTache(t: Tache):
    return{"message": "tache reçue",
           "tache":t}
@app.put("/taches/{tache_id}")
def updateTache(tache_id: int, t:Tache):
    return{"message": f"je vais modifier la tache {tache_id}", "nouvelle valeur": t}

@app