## 🏷️ Lista de tareas

### Automatización

 - [x] Añadir automatización al crear las carpetas principales en Linux (y permisos).
 - [x] Actualizar 'makefile' y el módulo 'Utils.psm1' con el archivo 'permissions.sh'.
 - [x] Añadir la lectura y automatización de la carpeta principal de música para generar los registros automáticamente desde el Administrador.
 - [x] Crear un **CRON** para la importación asíncrona de la carpeta *'root'* y que genere registros sin colapsar la UI.

### Modelos

 - [ ] **Añadir campo que almacene la extensión del archivo.**
 - [x] Evitar la eliminación de los campos género o artista si el usuario no es Admin.
 - [x] Que el usuario pueda marcar género o artista para eliminar. El Admin puede eliminar dichos registros.
 - [x] Informar correctamente al usuario mediante notificaciones.
 - [x] Añadir el modelo *'Opciones'* que permita la configuración global del módulo.
 - [x] Quitar el *'favorito'* de los álbumes puesto que son globales.
 - [x] Implementar diferenciación de artistas (pueden haber dos artistas con el mismo nombre).
 - [ ] **Añadir un modelo *'disk'* que almacene la información de un disco (un disco puede tener muchas canciones pero puede pertenecer a un solo álbum.**
 - [x] Implementar una solución para la *'homonimia'* de artistas y álbumes.
 - [x] Implementar cálculo automático para saber si un álbum está completo o no.

### Adaptadores
 - [x] Crear Numeradores para tipo de archivo (*PNG*, *JPEG*, ... ), tipo de descargador (*PyTube*, ...), tipo de metadatos (*MP3*, *FLAC*, ...).


### Servicios

 - [ ] **Añadir Pydub para la conversión de archivos de diferentes formatos.**
 - [x] Añadir método que se encargue de mover los archivos.
 - [x] Añadir método que se encargue de actualizar nombre de archivo.
 - [x] Añadir método que se encargue de devolver los ID3 tipo Dict.
 - [x] Añadir excepciones específicas en los servicios.
 - [x] Arreglar el guardado de metadatos: Actualmente da problemas.
 - [x] Comprobar que el archivo se elimine al eliminar el registro.
 - [x] Por ahora no hay lógica que elimine carpetas vacías. Implementar de forma recursiva.
 - [x] Añadir la etiqueta *'TCMP'* para marcar las canciones como compilatorias.

### Módulo

 - [x] Preparar bien los diferentes pasos del formulario principal.
 - [x] Convertir el formulario principal en un *'Wizard'*.
 - [x] Método al pulsar *'save'* que devuelva las etiquetas añadidas al archivo y actualice los campos.
 - [x] Arreglar botón *'save'*. *'Constrains'* detecta que no hay URL ni archivo y da error.
 - [ ] **Crear test para revisar todos los servicios creados.**
 - [ ] **Por ahora no hay problemas de sobreescritura (comprobar al haber dos usuarios modificando el mismo archivo).**
 - [x] Qué ocurre si la canción se elimina y el registro se mantiene: Comprobación del *'path'* una vez se abre el formulario.
 - [x] Implementar lógica que controle *'collection'*: Si se marca, *'various artists'*, si no que calcule según artista original.
 - [ ] **Cuando se agrega un archivo desde un USB no se calcula su duración. Tener en cuenta al momento de desplegar el proyecto.**
 - [x] Añadir documentación y tipado de los modelos.
 - [x] Añadir textos informativos al actualizar los metadatos de las canciones.
 - [ ] **Implementar soporte multilenguaje.**
   - [x] Inglés.
   - [ ] **Francés.**
   - [x] **Español.**
   - [x] **Catalán.**
 - [ ] ~~Cuando se elimine un registro (*'user general'*) se elimine su propietario, pero que Admin pueda ver qué registros no tienen propietario.~~
 - [x] Error al eliminar Género y Artista de forma automática al eliminar todos los registros. No se tienen permisos de Admin.
 - [x] Al agregar una canción ya existente, el registro queda guardado habiendo dado error. Un registro en blanco aparece.
 - [x] Crear menús y vistas de *'Albums'* y *'Artists'* según el tipo de usuario (*'General'*, *'Admin'*).
 - [x] Los artistas son globales y, por tanto, configurar si es favorito o no también. Eliminar dicho atributo y añadirlo a álbum.
 - [x] **Revisar textos en inglés.**
 - [x] Revisar excepciones dadas.
 - [ ] **Conseguir que los formularios se muestren de modo *'solo lectura'* cuando el usuario no es propietario (*'artist'*, *'genre'*).**
 - [x] El administrador no puede ver los resultados obtenidos agrupados por usuario en *'artist'* y *'genre'* en las pestañas álbum o canciones.
 - [ ] ~~Incluir en *'file_service'* la lectura de archivo (*'read_bytes'*) y pasar dichos datos a *'metadata_service'*.~~
 - [x] Cuando el usuario agregue varios artistas, dichas etiquetas deben colocarse en orden alfabético *(Artistas: Lester Frances, Sarah Trevino)* de forma automática.

### Marco legal

 - [ ] **Incluir ID de Transacción único por cada usuario al subir su archivo.**
 - [ ] **Ocultar el concepto *'descargar desde YouTube'* cuando el usuario no es administrador.**