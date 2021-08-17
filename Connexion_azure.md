Documentation to put in production an ML API on AZURE using fastapi & Docker


## 1. Fast API :

1.1 Dowload and install fastapi : pip install fastapi[all]    
All information on : https://fastapi.tiangolo.com/tutorial/    
1.2 Use main file in api folder to create your api app.    
Instanciate your api "app = FastAPI()" and then customize your path operations        
1.3 Use "uvicorn main:app --reload" to launch the api        
API docs available : "http://127.0.0.1:8000/docs"        


## 2. Install Docker

2.1 dowload and install docker https://docs.docker.com/get-docker/          
__Choose version depending on you system__    
2.2 create Dockerfile       
2.3 add custom api to it   
2.4 Build docker image      
"docker build -t  <image_name>.    
2.5 Launch docker container on localhost        
"docker run --name <custom_container_name> -p <Hostport>:<Containerport> <image_name>"      
2.6 test the api   

## 3. Azure
3.1 Utilisation d'azure container registries     
 **When creating a registry avoid uppercase to limit authentifications issues**        
https://docs.microsoft.com/fr-fr/azure/app-service/quickstart-custom-container?tabs=python&pivots=container-linux     
https://docs.microsoft.com/fr-fr/azure/container-registry/container-registry-get-started-portal    
3.2 Install  AZURE CLI   
https://docs.microsoft.com/fr-fr/cli/azure/install-azure-cli-linux?pivots=apt    
3.3 Create azure container       
 * Connect to portal.azure         
 * Select create container registries & create a container registry       
 * connect to registry with azure cli :       
 az login    
 az acr login --name <registry-name>     
 3.4 Add a docker container to Azure registry  
 * Connection to azure remote registry from terminal :     
 az acr login --name <registry-name>    
 * Before you push an image to the registry, you must tag it with the full name of your Registry Connection server. The name of the connection server is in the format <registry-name> .azurecr.io (all in lowercase)(==login-server). For example: mycontainerregistry.azurecr.io.  
 **attention nom serveur en miniscule**  
 docker tag <dockerimagename> <login-server>/<nomimagesurazure>:v1   
 * push tagged image to azure  :        
docker push <login-server>/<nomimagesurazure>:v1      
* remove local docker image :    
docker rmi <login-server>/<nomimagesurazure>:v1    
* execute from azure registry container image :    
docker run <login-server>/<nomimagesurazure>:v1    

3.5 Deploy image on app services      
**if using vscode with azure and docker extension** go to folder registries to the image previously created    
Click on "Deploy Image to Azure App Service" and follow the instructions     
**If error of service subscription after previous instruction set example: Microsoft.Web** please add this service to your subscription by following the next steps : 
 https://docs.microsoft.com/fr-fr/azure/azure-resource-manager/templates/error-register-resource-provider     
 **If error of access right pleasee check in your container registry the access keys and admin user setups**    
3.6  Add a setting named WEBSITES_PORT        
https://docs.microsoft.com/en-us/azure/developer/python/tutorial-deploy-containers-02        
* To set WEBSITES_PORT, switch to the Azure: App Service explorer, expand the node for your new App Service (refresh if necessary), then right-click Application Settings and select Add New Setting. At the prompts, enter WEBSITES_PORT as the key and the port number for the value.



