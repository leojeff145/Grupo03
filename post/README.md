# Grupo 03
### Karla Ansatuña
### Leonardo Obando
### Alex Trejo
# Microservicio de Blog

Este proyecto es un microservicio para gestionar publicaciones de un blog utilizando FastAPI y PostgreSQL. A continuación se detalla la configuración, el proceso de instalación y el uso de este microservicio.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
├── alembic.ini
└── migrations/
```

## Configuración del Entorno

1. **Docker**: El proyecto utiliza Docker para la contenedorización. Asegúrate de tener Docker y Docker Compose instalados en tu sistema.
2. **Variables de Entorno**: La configuración de la base de datos se maneja mediante la variable de entorno `DATABASE_URL` en el archivo `docker-compose.yml`.

## Archivos de Configuración

### `docker-compose.yml`

```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: mysecretpassword123
      POSTGRES_DB: cms_db
    ports:
      - "5432:5432"

  app:
    image: my-fastapi-app
    build: .
    environment:
      DATABASE_URL: postgres://admin:mysecretpassword123@db:5432/cms_db
    ports:
      - "8000:8000"
    depends_on:
      - db
```

## Migraciones de Base de Datos

Las migraciones se gestionan con Alembic. Para aplicar las migraciones a la base de datos, usa el siguiente comando:

```bash
docker-compose exec app alembic upgrade head
```

Para verificar la estructura de la base de datos, puedes conectarte al contenedor de PostgreSQL y revisar las tablas:

```bash
docker-compose exec db psql -U admin -d cms_db
```

## Desarrollo

Para desarrollar el proyecto, accede al contenedor de la aplicación:

```bash
docker-compose exec app sh
```

Navega al directorio de migraciones y abre los archivos de migración con `vi` o cualquier editor disponible:

```bash
cd migrations/versions
vi 176bf6dc8c8f_initial_migration.py
```

## Ejemplo de Solicitud POST

Puedes hacer solicitudes POST a la API utilizando herramientas como Thunder Client. Aquí tienes un ejemplo de solicitud para crear una nueva publicación:

- **URL**: `http://localhost:8000/posts/`
- **Método**: `POST`
- **Cuerpo de la Solicitud**:

```json
{
  "title": "string",
  "content": "string"
}
```

- **Respuesta Esperada**:

```json
{
  "title": "string",
  "content": "string",
  "id": 0
}
```

## Notas Adicionales

- **__pycache__**: Carpeta generada automáticamente por Python para almacenar archivos de bytecode compilado.
- **Archivos de Migración**: Se encuentran en el directorio `migrations/versions` y se generan automáticamente con Alembic.

Para cualquier pregunta o problema, por favor, consulta la documentación oficial de FastAPI, PostgreSQL y Alembic.
