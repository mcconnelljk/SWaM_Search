# SWaM_Search #

## I - Local environment Set-up ##

### 1 - Create Postgres database within Docker Container ###

Before you begin, you should install [Docker Desktop] (http://www.docker.com/products/docker-desktop), which comes with Docker Compose.  You should probably also install something on your laptop to connect the local database, such as [DBeaver Community](https://dbeaver.io).

Local development credentials are in plain text in the associated config file [db.env].

To set up the database within a docker container, run the following command

```shell
docker-compose up -d db-loc
```

### 2 - Create a virtual environment within the SWaM_Search parent directory ###

Using ['venv'](https://docs.python.org/3/library/venv.html) or some other such package running on your host machine, create a virtual environment for this project.

For simplicity, I keep my '.venv' folder within the local github repo folder, which I treat as my main project folder.

To activate your venv:

    ```shell
    #Linux
    source .venv/bin/activate

    #PC
    .venv\Scripts\activate.bat
    ```

### 3 - Run 'venv_setup.py' to load package dependencies ###


The 'requirements.txt' file contains all of the package dependencies for the swam_search app.

```shell
pip3 install -r requirements.txt
#optional upgrade
pip3 install --upgrade pip
```

Run 'venv_setup.py' to load these packages into your virtual environment

```shell
python venv_setup.py
```

### 3 - Load Data into database ###

For this demo, I selected to use postgres.  To load raw .csv data into postgres, we can leverage the 'psychopg2' package (loaded to venv in previous step).



### 4 - Run 'venv_setup.py' to load packages into venv

