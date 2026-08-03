from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud.tache
from db.database import SessionLocal
from schemas.tacheCreation import TacheCreation

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI(title="API de gestion des tâches",
              description=
              """"
              Cette application permet de :
              -Lister les tâches
              -Récupérer les details d'une tâche
              -Ajouter une tâche
              _Mettre à jour une tâche
              _Supprimer une tâche
              """)

@app.get("/taches/",
         summary="Récupèrer toutes les tâches",
         description="Toutes les taches de la base de données sont dans un JSON",
         response_description="Liste de toutes les tâches au format JSON")
def getAllTache(db: Session = Depends(get_db)):
    return {"message": "Fonction qui va récuperer toute les tâches"}
@app.get("/taches/{tache_id}", summary="")
def getTache(tache_id:int):
    return {
        "tache_id": tache_id,
        "titre":f"recuperer la tache {tache_id}"
    }

@app.post("/taches/")
def createTache(t:TacheCreation, db: Session = Depends(get_db)):
    db_tache= crud.tache.createTache(t,db)
    return db_tache
@app.put("/taches/{tache_id}")
def updateTache(tache_id:int, t: TacheCreation):
    return {"message":f"le message update porte l'identifiant {tache_id}", "tache":t}

@app.delete("/taches/{tache_id}")
def deleteTache(tache_id:int):
    return {"message": f"je vais supprimer la tache {tache_id}"}
