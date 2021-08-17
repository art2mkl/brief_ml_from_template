# Documention de l'API "PINGUINS"

## RESUME
API "PINGUINS" predict pinguins species with https request

## Equipe
* https://github.com/clement-camara
* https://github.com/art2mkl

## Introduction
L’API PINGUINS fournit une API de services Web pratique, puissante et rapide afin de réaliser des prédictions de classifications d'espèces de pinguins à l'aide d'un modèle de Machine Learning complexe.

## Connexion
URL de base : https://darkpinguins.azurewebsites.net

## Authentification
L'accès à l'API Pinguins est publique. Il ne nécessite pas d'authentification pour accéder à ses fonctionalités selon le principe :

*Tous Les Pinguins sont Libres et Egaux en droits*

## Fonctionnement
Les appels à cette API seront réalisés via l'URL de base en rajoutant le chemin vers l'action désirée

*Exemple*
````shell
https://darkpinguins.azurewebsites.net/<chemin_action>

````

### Vérification de la connexion
*Exemple*
````shell
https://darkpinguins.azurewebsites.net

````
En cas de succès de connexion, une requête sur l'URL de base renvoie la valeur :
```shell
=> {api is ready}
```

### Visualisation du Dataset de Machine Learning
*Exemple*
````shell
https://darkpinguins.azurewebsites.net/df

````
Cette requête permet de visualiser le Dataset utilisé pour entraîner notre modèle de Machine Learning

Il renvoie un Tableau Json presentant toutes les données d'entrainement initiales :
````shell
=>  {"species":

        {"0":"Adelie","1":"Adelie","2":"Adelie",...

        ..."342":"Female","343":"Male"}
    }
````
### Prediction d'une espèce
*Exemple*
````shell
https://darkpinguins.azurewebsites.net/prediction?island=<island>&bill_length_mm=<bill_length_mm>&bill_depth_mm=<bill_depth_mm>&flipper_length_mm=<flipper_length_mm>&body_mass_g=<body_mass_g>&sex=<sex>

````
Cette requête permet de prédire l'appartenance à une espèce en fonction des paramètres envoyés à l'API via une méthode GET.

Ces paramètres doivent respecter les contraintes suivantes :
* **< island >** représente l'ile de l'individu à prédire, il peut présenter les valeurs suivantes : 
    * *Torgersen*
    * *Biscoe*
    * *Dream*

* **< bill_length >** représente la longueur du bec, ses valeurs varient de 32 à 60 mm

* **< bill_depth_mm >** représente la profondeur du bec, ses valeurs varient de 13 à 22 mm

* **< flipper_length_mm >** représente la longueur de la nageoire, ses valeurs varient de 172 à 231 mm

* **< body_mass_gm >** représente le poids de l'individu, ses valeurs varient de 2700 à 6300 g


* **< sex >** représente le sexe de l'individu, il peut présenter les valeurs suivantes : 
    * *Male*
    * *Female*


La prédiction retourne un Tableau indiquant le type d'espèce de l'individu:
````shell
=> ["Gentoo"]
````

## Liste des Erreurs

Chaque appel à l'API donne lieu à une réponse retournant un code spécifique en fonction du résultat obtenu. L'analyse de ce code vous permet de vous assurer que la requête a été traitée avec succès.

Tous les codes >= 400 indiquent que la requête n'a pas été traitée avec succès par nos serveurs.

* 200: OK
* 400: Paramètre manquant, ou valeur incorrecte
* 403: Action non autorisée (URL non autorisée, etc)
* 404: Page inaccessible (URL inconnue / impossible d'accéder à l'adresse)
* 503: L'API est momentanément indisponible, réessayez dans quelques minutes

## Focus Code API
### Construction
L'API Pinguins est construite à l'aide du célèbre package ML_PINGUINS_PKG https://github.com/art2mkl/brief_ml_from_template/tree/master/ml_pinguins_pkg

La construction du modèle est réalisée en instanciant un objet pinguins_model et en lui passant un Dataset chargé à l'aide de la librairie python Seaborn et en lui précisant que la valeur à prédire sera contenur dans la colonne *"species"*

````python
#creation du model
df = sns.load_dataset('penguins')
model = Pinguins_model(df,'species')
````
### Enraînement
L'entrainement du modèle est réalisé à l'aide d'un algorythme de Random Forest :
```python
model.prepare_model(RandomForestClassifier())
```
### Prédiction
La prédiction est réalisée à l'aide de la méthode predict_model

Cette dernière reçoit les paramètres de prédictions via une requête GET et l'associe au modèle prédemment instancié pour retourner la prédiction d'espèce sous forme de tableau:
```python
@app.get('/prediction')

async def prediction(island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex):
    					
    quest = pd.DataFrame({
        'species': "query",
        'island': [str(island)],
        'bill_length_mm': [float(bill_length_mm)],
        'bill_depth_mm': [float(bill_depth_mm)],
        'flipper_length_mm': [float(flipper_length_mm)],
        'body_mass_g': [float(body_mass_g)],
        'sex': [str(sex)]                         
    })

    model.transform_null(quest)
    pred = model.predict_model(model.model, model.X)[0]
    return [pred]
    ```
