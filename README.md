# InternshipMeduzzen

## Start project

#### Clone repository

`git clone https://github.com/username/repository.git`

#### Create new environment

`python -m venv venv `

#### activate environment

On Windows

`venv\Scripts\activate`

MacOS & Linux

`source venv/bin/activate`

#### Install packages

`pip install -r requirements.txt`

### Create an .env file using the .env.sample example 

### Add Docker

#### Create new image

`docker build -t myimage .`

#### Starting a Docker container

`docker run -d --name [name your container] -p [your port]:8080 myimage`

#### Apply migrations

`alembic upgrade head`




