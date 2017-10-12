#Entrevista Django#

Esta es la pre-entrevista de django para Magnet. El código es simplemente un
proyecto básico de django 1.8 que tiene 3 modelos dentro de
polls/models.py:

* Poll
* Question
* Choice.

Lo primero que debes hacer es clonar el proyecto, ejecutar las migraciones para cargar los
fixtures y hacer correr el proyecto. Con el proyecto corriendo entra a la ruta /polls, ahí 
verás la lista de polls que hay en la base de datos, con sus questions y choices asociados. 

Esta página tiene un problema, se demora muchísimo en cargar, por lo que tu misión será hacer
que cargue en un tiempo razonable para la cantidad de datos que tiene. Es importante que **no** ocupes un paginador en tu solución. Adicionalmente, necesitamos 
la respuesta a las siguientes preguntas:

* ¿Cuál fue el problema?
* ¿Cómo lo solucionaste?

Comparte con nosotros un link con los archivos que hayas modificado (no crees nuevos archivos).