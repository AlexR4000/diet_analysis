How to Create Docker image
- Have Dockerfile and diet_analysis.py
- docker build -t diet-analysis .
- docker run -it diet-analysis

For DockerHub (bukopandan)
- docker login
- docker tag diet-analysis yourdockerhubusername/diet-analysis
- docker push yourdockerhubusername/diet-analysis

- https://hub.docker.com/r/bukopandan/diet-analysis
