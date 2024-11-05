# Utiliser une image de base légère de Python 3.12
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY web_app /app
COPY requirements.txt /app

# Installer les dépendances nécessaires
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir fastapi pydantic pandas uvicorn scikit-learn catboost jinja2

# Exposer le port sur lequel FastAPI va s'exécuter
EXPOSE 8000

# Démarrer l'application FastAPI avec Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
