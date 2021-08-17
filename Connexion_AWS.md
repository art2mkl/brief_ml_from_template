# - Docker en local



### Assurez-vous d'avoir un compte AWS

### téléchargez Docker Desktop

1) Installez Docker , si vous ne l'avez pas déjà, ajoutez un Dockerfile à la racine du projet :

2) Ensuite, ajoutez un fichier docker-compose.yml à la racine du projet :

3) Construisez l'image avec le docker compose: 
   
````shell
docker-compose build
````

4) Une fois l'image créée, exécutez le conteneur : 

````shell
docker-compose up -d
````

5) Accédez à http://localhost:8008 pour afficher la requete de votre fastapi





# - Docker en prod



### téléchargez Docker Desktop

--> https://www.docker.com/products/docker-desktop

### inscrivez-vous pour un Docker ID

--> https://hub.docker.com/editions/community/docker-ce-desktop-mac?utm_source=awsedge

### ----------------------------- ###

# - procédure pour le déploiement via ECS

https://docs.docker.com/cloud/ecs-integration/

1) Lancez une instance avec l' AMI Amazon Linux 2

--> https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Instances:

2) Connectez-vous à votre instance en suivant la commande example client ssh

--> vous etes desormais connecte a l'instance Linux

3) Mettez à jour les packages installés
````shell
sudo yum update -y
````

4) Installez le package Docker Engine le plus récent. Amazon Linux 2

```shell
sudo amazon-linux-extras install docker
```

5) Lancez le service Docker

````shell
sudo service docker start
````

6) Ajoutez ec2-user au groupe docker afin de pouvoir exécuter les commandes Docker sans utiliser sudo

````shell
sudo usermod -a -G docker ec2-user
````

7) Déconnectez-vous et reconnectez-vous pour récupérer les nouvelles autorisations de groupe docker

--> pomme q

````shell
ssh -i "clefs_de_la_demo_pour_micka.pem" ec2-user@ec2-3-237-68-44.compute-1.amazonaws.com
````

8) Vérifiez que ec2-user peut exécuter les commandes Docker sans sudo

````shell
docker info
````





# - Transmettre votre image à Amazon Elastic Container Registry ECR

--> https://console.aws.amazon.com/ecr/repositories?region=us-east-1

1) installé et configuré l'AWS CLI

--> https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html#cliv2-mac-install-gui

2) Votre utilisateur doit disposer des autorisations IAM requises pour accéder au service Amazon ECR

--> Cela permet aux utilisateurs spécifiés ou
--> aux instances Amazon EC2 d'accéder à vos référentiels et images de conteneurs

3) Créez un référentiel Amazon ECR pour stocker votre image

--> récupérer la valeur dans le dictionnaire qui apparait :

"repositoryUri": "426584999926.dkr.ecr.us-east-1.amazonaws.com/repo_demo_mickael"

4) Balisez l'image avec la valeur repositoryUri de l'étape précédente


    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:426584999926:repository/repo_demo_mickael",
        "registryId": "426584999926",
        "repositoryName": "repo_demo_mickael",
        "repositoryUri": "426584999926.dkr.ecr.us-east-1.amazonaws.com/repo_demo_mickael",
        "createdAt": "2021-08-09T22:52:07+02:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"

5) Exécutez la commande aws ecr get-login-password.

--> Spécifiez l'URI du registre sur lequel vous souhaitez vous authentifier

aws ecr get-login-password | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com

EXEMPLE

````shell
aws ecr get-login-password | docker login --username AWS --password-stdin 426584999926.dkr.ecr.us-east-1.amazonaws.com/repo_demo_mickael
````

Si ca a marché il y aura marqué "Login Succeeded"

6) Créez votre image Docker à l'aide de la commande suivante

````shell
docker build -t 426584999926.dkr.ecr.us-east-1.amazonaws.com/repo_demo_mickael .
````

7) pousser l'image sur le repo aws

````shell
docker push 426584999926.dkr.ecr.us-east-1.amazonaws.com/repo_demo_mickael:latest
````

--> si ca marche l'image apparaitra dans le repo créé sur amazon
















