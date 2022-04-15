# web-automovil
## Ejercicio de Programación

Este ejercicio de programación se corresponde con el desarrollo de una web de automóviles en
Django.

### Modelo de datos
El modelo de datos se debe de componer de lo siguiente:
+ Marca
+ Modelo
+ Coche
  + Fecha de creación
  + Un coche se compone de una marca
  + Un coche se compone de un modelo

Los campos de cada modelo son libres (Se permite cualquier tipo de campo, siempre y cuando
este tenga sentido en el modelo correspondiente) cumpliendo las restricciones anteriormente
citadas.

Así mismo, se permite crear tantos modelos como sean necesarios siempre y cuando los
campos/modelos necesarios indicados anteriormente existan en el ejercicio.

Todos los modelos de datos se deben de agregar al panel de administración de Django (Django
admin)

### Ejercicio a realizar
#### Objetivo base
Con el modelo de datos indicado anteriormente, se pretende la realización de una web en
Django que permita la gestión de todos los modelos de datos creados. Por lo tanto, por cada
modelo de datos se deberán realizar las siguientes acciones:
- Listar todas las entradas del modelo de datos.
- Permitir crear nuevas entradas de datos en el modelo correspondiente.
- Poder editar modelos datos. Ej.: Poder editar la marca o el modelo de un coche ya
creado.
- Poder eliminar entradas del modelo de datos.
- Listar todos los coches de determinadas marcas.

Además de todas estas funcionalidades asociadas a la web, se deben de desarrollar las siguientes
utilidades:

- Funcionalidad para obtener un diccionario en la cual las “keys” deberán de ser todas las
marcas y los “values” deberán de ser todos los coches de la correspondiente marca.
- Funcionalidad para devolver todos los coches cuya fecha de creación sea anterior a la
dada por parámetro.

- Funcionalidad para devolver un coche según el identificador dado por parámetro. Debe
de existir la posibilidad de que el id no exista en la base de datos.

#### Objetivos extra
- Crear formulario que permita la búsqueda o el filtrado de todos los coches mediante los
correspondientes elementos de su modelo de datos (Ej.: Filtrar todos los coches de
determinada marca o modelo, etc....)
- Desarrollo de una API Rest CRUD (Consultar, crear, editar y eliminar). Para este punto
se puede utilizar librerías externas.
- En caso de usar DRF para la API Rest, otro punto positivo es el uso de serializadores.

La realización de los ejercicios extra se valuará positivamente.

### Entrega del ejercicio
Todo el código debe de estar subido a un repositorio GIT. Por lo que solo será necesario que se
nos proporcione el enlace a dicho proyecto.

Debe de existir un fichero requirements.txt con todas las dependencias utilizadas.

En caso de que el ejercicio requiera de instrucciones específicas para la ejecución del proyecto,
se deberá de incluir un documento que contenga todos los pasos a realizar.
