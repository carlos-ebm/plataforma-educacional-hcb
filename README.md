# plataformaeducacional

¡Bienvenido al repositorio de la Plataforma Educativa *Hogar Casa Belén*!

Esta plataforma educativa, desarrollada utilizando el framework Django en Python, ofrece una solución integral para facilitar la enseñanza y el aprendizaje en entornos virtuales, especialmente durante situaciones desafiantes como la pandemia. Permite a los profesores cargar actividades y recursos, mientras que los estudiantes pueden visualizar las actividades, entregar tareas y mantener una interacción fluida.

## Características

- **Gestión de Usuarios:** Profesores y estudiantes pueden registrarse e iniciar sesión en la plataforma.

- **Carga de Actividades:** Los profesores pueden subir actividades con descripciones detalladas y adjuntar archivos relevantes.

- **Entrega de Tareas:** Los estudiantes pueden acceder a las actividades, cargar sus tareas completadas y adjuntar archivos.

- **Interacción y Comentarios:** Profesores y estudiantes pueden interactuar a través de comentarios en las actividades, fomentando la colaboración y el diálogo constructivo.

- **Seguimiento del Progreso:** Tanto profesores como estudiantes pueden hacer un seguimiento de su progreso individual y revisar las actividades completadas.

## Instalación y Uso

1. Clona este repositorio en tu máquina local.

   ```bash
   git clone https://github.com/tu-usuario/nombre-de-la-aplicacion.git

2. Navega a la carpeta del proyecto.
   ```bash
   cd nombre-de-la-aplicacion
   
3. Instala las dependencias utilizando pip.
   ```bash
   pip install -r requirements.txt

4. Configura la base de datos en settings.py y realiza las migraciones.
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Crea un superusuario para administrar la plataforma.
   ```bash
   python manage.py createsuperuser

6. Inicia el servidor de desarrollo.
   ```bash
   python manage.py runserver

## Contribución

Si deseas contribuir a este proyecto, ¡eres bienvenido! Sigue estos pasos:

1. Realiza un fork de este repositorio.
2. Crea una rama para tu función o corrección: git checkout -b feature/nueva-funcion.
3. Realiza tus cambios y realiza commits descriptivos.
4. Sube tus cambios a tu repositorio fork: git push origin feature/nueva-funcion.
5. Abre un Pull Request describiendo tus cambios detalladamente.

## Tecnologías Utilizadas
- Framework Backend: Django
- Base de Datos: SQLite

## Créditos
Esta plataforma fue desarrollada por Carlos Brito y Ánibal Ramos para Hogar Casa Belén.
