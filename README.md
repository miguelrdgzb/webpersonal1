# webpersonal1
[Django] Código desarrollo backend

Desarrollo de appweb en dos modulos.

Los textos son estandár y al igual que los archivos estaticos, que son totalmente customizables.

Se puede clonar el repositorio y ejecutar desde la misma carpeta en terminal con el comando django manage.py webpersonal1 runserver.


<--- Estructura --->

Se compone de dos apps:
*Core : Que es el eje central de la app, que incluye todas las vistas y templates excepto el de portfolio.
*Portfolio : contiene el modelo del que se compone la base de datos, en este caso SQLite, en el que solo encontramos una tabla compuesta por la estructura de los campos del Portfolio. Incluye su html en concreto que sigue heredando del html en core/templates.

Por otro lado, en el apartado principal 'webpersonal' encontramos las configuraciones de las vistas y urls del proyecto.
Tambien aqui es donde se irían almacenando los archivos multimedia de los formularios del portfolio.


