from __future__ import with_statement
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from app.db.base import Base
from app.core.config import settings

# Configuración del archivo de configuración de Alembic.
config = context.config

# Interpretar el archivo de configuración de la base de datos .ini.
fileConfig(config.config_file_name)

# Añadir aquí los modelos para que 'autogenerate' pueda detectar los cambios.
target_metadata = Base.metadata

# URL de la base de datos.
config.set_main_option('sqlalchemy.url', settings.DATABASE_URL)

def run_migrations_offline():
    """Ejecutar migraciones en modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecutar migraciones en modo 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
