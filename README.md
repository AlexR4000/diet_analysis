How to Create Docker image
- Have Dockerfile and diet_analysis.py
- docker build -t diet-analysis .
- docker run -it diet-analysis

For DockerHub (bukopandan)
- docker login
- docker tag diet-analysis yourdockerhubusername/diet-analysis
- docker push yourdockerhubusername/diet-analysis

- https://hub.docker.com/r/bukopandan/diet-analysis

How to Process data with simulated function using Azurite
#Run the docker image to install/run Azurite
- docker run -p 10000:10000 -p 10001:10001 mcr.microsoft.com/azure-storage/azurite
#Install Storage Explorer to upload file
- sudo snap install storage-explorer
#Open storage explorer
- storage-explorer
#Create new "datasets" blob container and upload the csv file
#Now run the simulated serverless function to simulate the data processing workflow in cloud
- python3 serverless_func.py
