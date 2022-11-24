# Creacion de mis propios paquetes o librerias en python

## Pasos:
- ingresar datos de tu libreria en el archivo setup.py sdist
- ejecutar el archivo setup.py
- luego ingresar al directorio creado llamado dist
- estando dentro del directorio ejecuta pip install mas el nombre del paquete zip o el que aparesca
- si la libreria no tiene errores o no se ingresaron datos erroneos en setup.py, esta se instalara
- para probar su instalacion abre una nueva terminal y escribe python luego llama tu libreria
- ejecuta tus metodos o clases finalizar la verificacion

## Actualizacion:
- si agregar actualizaciones, deberas modificar los datos de version y de paquetes en setup.py si es necesario
- luego  ejecutaras setup.py sdist
- la nueva version de tu libreria se agrega al directorio dist y veras que ya tienes otro paquete para instalar pero con una version diferente.

### Listo as creado tu paquete o libreria, ahora ve y diles a tus compas que eres hacker xd !!.
