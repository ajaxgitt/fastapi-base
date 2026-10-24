# crear un entorno virtual
python -m venv venv
source venv/bin/activate


# librerías necesarias

`fastapi`
`pydantic-settings`
`uvicorn`
`sqlalchemy`
`alembic`
`psycopg2-binary`


# pip freeze > requirements.txt

# configurar alembic el ORM

`alembic init alembic`


# si ves esto todo bien !
![alt text](image.png)

# levantar el proyecto con docker

El repo ya trae un `.env` listo. Si no lo tienes, créalo a partir del ejemplo:

```bash
cp .env.example .env
```

> **Nota:** en este repo **sí subimos el `.env`** porque es un proyecto de ejemplo y sirve como guía de cómo deben ir tus configuraciones.
> En un proyecto real el `.env` **nunca** se sube: agrégalo al `.gitignore` y comparte solo el `.env.example` (sin claves reales).

## ambiente de desarrollo

```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

- API: http://localhost:8000/docs
- Recarga automática (`--reload`): el código está montado como volumen, así que los cambios se ven al instante
- Base de datos accesible desde tu máquina en `localhost:5433` (DBeaver, psql, etc.)

## ambiente de producción

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d
```

- La API solo escucha en `127.0.0.1:8000` (para ponerle delante un proxy como nginx)
- Corre con 2 workers, healthcheck y límites de CPU/memoria
- La base de datos **no publica ningún puerto**: solo la ve la app

## redes

| red       | quién está                 | para qué                                              |
|-----------|----------------------------|-------------------------------------------------------|
| `web`     | app (y db solo en dev)     | comunicación con el exterior                          |
| `backend` | app + db                   | red interna (`internal: true`), sin salida a internet |

## comandos útiles

```bash
# ver logs
docker compose -f docker-compose.yml -f docker-compose.dev.yml logs -f

# entrar al contenedor de la app
docker exec -it fastapi_base_app bash

# entrar a la base de datos
docker exec -it fastapi_base_db psql -U fastapi_user -d fastapi_base

# bajar los contenedores (-v borra también el volumen de la db)
docker compose -f docker-compose.yml -f docker-compose.dev.yml down
```
