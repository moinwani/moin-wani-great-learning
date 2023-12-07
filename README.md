# Project
I am working on the iris dataset and training a classification model. Making it accessible organisation wide is my responsibility. I am expected to adhere to the company guidelines

README

This project provides a simple and efficient way to automate building and pushing Docker images directly from your Github repository. It is designed to be used with the Docker Build and Push workflow, which can be triggered on pushes to the main branch or other events.

The workflow uses QEMU and Buildx to support multi-architecture builds and faster build times. It also uses secrets to store your Docker Hub username and password securely.

To use this workflow, you will need to:

Create a Dockerfile in the root directory of your repository.
Create a Github Actions workflow file in the .github/workflows directory.
Add the following code to your workflow file:
YAML
name: Docker Build and Push

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest


    
steps:

      
-
 
name:
 
Checkout
 
Repository

        
uses:
 
actions/checkout@v2


      
-
 
name:
 
Set
 
up
 
QEMU

        
uses:
 
docker/setup-qemu-action@v2


      
-
 
name:
 
Set
 
up
 
Docker
 
Buildx

        
uses:
 
docker/setup-buildx-action@v1


      
-
 
name:
 
Login
 
to
 
Docker
 
Hub

        
uses:
 
docker/login-action@v1

        
with:

          
username:
 
${{
 
secrets.DOCKER_USERNAME
 
}}

          
password:
 
${{
 
secrets.DOCKER_PASSWORD
 
}}


      
-
 
name:
 
Build
 
and
 
Push
 
Docker
 
Image

        
uses:
 
docker/build-push-action@v2

        
with:

          
context:
 
.

          
push:
 
true
          tags: fardinqadri/mlmodel:latest
Use code with caution. Learn more
Create secrets in your Github repository for your Docker Hub username and password.
Once you have completed these steps, you can push your changes to your repository and the workflow will automatically start running.
