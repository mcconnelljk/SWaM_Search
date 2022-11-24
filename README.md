# SWaM_Search #

## Environment Set-up ##

Before you begin, you should install [Docker Desktop] (http://www.docker.com/products/docker-desktop), which comes with Docker Compose.  You should probably also install something on your laptop to connect the local database, such as [DBeaver Community](https://dbeaver.io).

Local development credentials are in plain text in the associated config file [db.env].

```shell
docker-compose up -d db-loc

docker run -d 
--name sql_server 
-e 'ACCEPT_EULA=Y' 
-e 'SA_PASSWORD=someThingComplicated1234' 
-p 1433:1433 mcr.microsoft.com/mssql/server:2019-latest

```

```shell
docker-compose up -d db-loc
```


