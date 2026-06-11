---
tags:
  - Docker
Type: 
source: 
page: 
Date: 
deadline: 
status:
---
getting-started-app on docker github repo we need to fork it and clone the repo that we now own to use it in our pipeline 

==yml is used for github action ==
1- getting-started-app -> directory
2- .github/workflows -> sub-directory. this is how github understands that i want to create a pipeline workflow its a must !! for github to understand that i want a pipeline to automate or execute commands on it
3- create a yml file under the workflows 

![[Docker+CI.html]]

```HTML
Go to [https://github.com/docker/getting-started-app](https://github.com/docker/getting-started-app)

Fork it

In the terminal, run:

git remote set-url origin https://github.com/abohmeed/getting-started-app.git

cat Dockerfile

Add the new file in VS Code:

# .github/workflows/docker-image.yml

name: Docker Image CI

on:

  push:

    branches:

      - main

  pull_request:

    branches:

      - main

jobs:

  build:

    runs-on: ubuntu-latest

    steps:

    - name: Checkout code

      uses: actions/checkout@v3

    - name: Set up Docker Buildx

      uses: docker/setup-buildx-action@v3 //plugins on github that            builds and push the image

    - name: Log in to GitHub Container Registry

      uses: docker/login-action@v3

      with:

        registry: ghcr.io

        username: ${{ github.repository_owner }}

        password: ${{ secrets.GITHUB_TOKEN }}

    - name: Build and push Docker image

      uses: docker/build-push-action@v5

      with:

        context: .

        push: true

        tags: |

          ghcr.io/${{ github.repository_owner }}/koki/getting-                    started:latest

          ghcr.io/${{ github.repository_owner }}/koki/getting-                    started:${{ github.sha }}
```

🔧 Buildx Purpose  --> **(uses: docker/setup-buildx-action@v3)** 
- Initializes a **Buildx builder** that can be used in subsequent steps of your GitHub Actions workflow.
- Essential for **building and pushing multi-platform images** with `docker/build-push-action`

git add -A
git commit -m ""
git push --> using ssh authentication easier 

#Docker_best_practice 
best practice in docker is to avoid using latest as version tag because we might be lost if multiple occurs.. 

pull the image from github repository 
run the image map your ports 
the image build is automated on push and pull actionsExternal sources citation Books articles Research papers blogs video-courses courses lectures 