# Usar una imagen base oficial de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los requisitos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar el contenido del proyecto
COPY . .

# Exponer el puerto en el que Django se ejecutará
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
