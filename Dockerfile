# installer version python

FROM python:3.9

# Installation des requirements après les avoir copier sur l'image disque
COPY requirements.txt .
RUN pip install -r requirements.txt

# Précise le port de l'image
EXPOSE 80

# Copie les repertoires de la racine à l'image du docker
COPY ./app /app
COPY ./ml_pinguins_pkg /ml_pinguins_pkg

# lancer unicorn et l'app via fastapi
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# à lancer dans le shell
# docker build -t nom_image .