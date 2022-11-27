# SWaM_Search #

## I - Local environment Set-up ##

### 1 - Create Postgres database within Docker Container ###

Before you begin, you should install [Docker Desktop] (http://www.docker.com/products/docker-desktop), which comes with Docker Compose.  You should probably also install something on your laptop to connect the local database, such as [DBeaver Community](https://dbeaver.io).

Local development credentials are in plain text in the associated config file [db.env].

To set up the database within a docker container, run the following command

```shell
docker-compose up -d db-loc
```

### 2 - Load Data into database ###

### 3 - Create a virtual environment within the SWaM_Search parent directory ###

### 4 - Run 'setup.py' to load packages into venv

