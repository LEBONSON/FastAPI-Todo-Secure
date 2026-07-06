# 📝 To-Do FastAPI - Application Full-Stack Sécurisée

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue.svg)](https://www.postgresql.org/)

## 🎯 Description du projet

Ce projet est une application complète de **gestion de tâches (To-Do List)** développée avec **FastAPI** (backend) et un frontend statique en HTML/CSS/JavaScript. 

Il est structuré sous forme de **tutoriel progressif** où chaque étape clé de la construction (endpoints, base de données, authentification JWT, rôles, HTTPS) est isolée dans un commit ou une branche dédiée. L'objectif est de fournir à la fois un outil fonctionnel et une feuille de route pédagogique pour apprendre les bonnes pratiques du développement full-stack sécurisé.

---

## 🗺️ Feuille de route (Étapes du tutoriel)

Chaque étape correspond à un état spécifique du projet :

| Étape | Sujet | Description |
| :---: | :--- | :--- |
| **00** | `FrontFixe` | Intégration de l'interface utilisateur statique (HTML/CSS/JS) prête à l'emploi. |
| **01** | `Endpoints` | Création des routes CRUD pour les tâches avec validation stricte via **Pydantic**. |
| **02** | `BDD` | Connexion à une base de données **PostgreSQL** et mapping des modèles avec **SQLAlchemy**. |
| **03** | `Fonctionnel` | Raccordement du frontend aux endpoints (ajout, liste, modification, suppression de tâches). |
| **04** | `JWT` | Implémentation de l'authentification via **JSON Web Tokens** sur les routes protégées. |
| **05** | `JWTetFront` | Appels des routes d'auth (`/register`, `/login`, `/refresh`) depuis le frontend. |
| **06** | `RoleHttpOnly` | Ajout de la notion de **rôles** (admin/user) et stockage des tokens dans des cookies **HttpOnly** (sécurité XSS). |
| **07** | `HTTPSNginx` | Mise en place d'un serveur **Nginx** pour la terminaison **HTTPS** et la communication sécurisée. |

---

## 🧰 Stack technique

- **Backend** : FastAPI, Uvicorn, Pydantic, SQLAlchemy
- **Base de données** : PostgreSQL
- **Sécurité** : JWT (Python-JOSE), Cookies HttpOnly, Bcrypt
- **Serveur/Proxy** : Nginx
- **Frontend** : HTML5, CSS3, JavaScript (Vanilla)

---

## ⚙️ Installation et lancement

### Prérequis
- Python 3.10 ou supérieur
- PostgreSQL (installé et en cours d'exécution)
- Git

### 1. Cloner le dépôt
```bash
git clone https://github.com/votre-utilisateur/To-Do-FastAPI.git
cd To-Do-FastAPI
```

### 2. Créer et activer l'environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate  # Sur Mac/Linux
# .venv\Scripts\activate   # Sur Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement
Créez un fichier `.env` à la racine :
```env
DATABASE_URL=postgresql://user:password@localhost:5432/todo_db
SECRET_KEY=votre_cle_secrete_jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Initialiser la base de données (Étape 02 ou supérieure)
```bash
# Créer la base de données dans PostgreSQL (via psql ou PgAdmin)
# Puis lancer les migrations (si Alembic est configuré)
alembic upgrade head
# ou directement via les modèles SQLAlchemy
```

### 6. Lancer le serveur
```bash
uvicorn app.main:app --reload --port 8000
```
Le backend sera accessible sur `http://localhost:8000` et la documentation interactive sur `http://localhost:8000/docs`.

---

## 📁 Structure du projet (aperçu)

```
To-Do FastAPI/
├── 00FrontFixe/          # Frontend statique
├── app/                  # Code backend (évolutif selon les étapes)
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── auth.py
├── .env                  # Variables sensibles (à ignorer)
├── .gitignore            # Fichiers à exclure du versioning
└── requirements.txt      # Dépendances Python
```

---

## 🔍 Naviguer entre les étapes

Pour explorer une étape spécifique du tutoriel, utilisez les branches ou tags :

```bash
# Lister les branches/tags disponibles
git branch -a
git tag

# Basculer sur une étape (ex: l'étape JWT)
git checkout 04JWT
```

---

## 🤝 Contribution

Ce projet est avant tout un outil pédagogique. Si vous souhaitez proposer des améliorations ou corriger des bugs, n'hésitez pas à ouvrir une *issue* ou une *pull request*.

---

## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer.
é