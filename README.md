# FastAPI + Nuxt boilerplate (todo app)

## Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Postgres](https://www.postgresql.org/)
- [Nuxt 3](https://nuxt.com/)
- [Docker compose](https://docs.docker.com/compose/)

## Run app

```bash
docker compose up [--build] [--renew-anon-volumes] [--detach]
```

Use `--build --renew-anon-volumes` if npm/pip dependencies have been updated  
Use `--detach` to run containers in the background

You will need to install both Skaffold and Minikube.

## Stop app

```bash
docker compose down
```

## Upgrade db

```bash
docker compose exec api alembic upgrade head
```

## App UI

- [Todo App](http://localhost:3000)

## Api docs

- [Swagger](http://localhost:8000/docs)
- [Redoc](http://localhost:8000/redoc)

## VSCode

Open project using workspace file:

```bash
code .vscode/fastapi-nuxt-boilerplate.code-workspace
```

You can run the app using launch config:

- docker compose: up (root)

You can attach vscode python debugger to container using launch config:

- docker compose: debug backend
