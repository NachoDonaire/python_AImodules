#! /bin/bash

#mostrar una lista de paquetes instalados
conda list

#mostrar los metadatos del paquete numpy
conda info numpy

#eliminar paquete numpy
conda remove numpy

#reinstalar paquete numpy
conda install numpy=(version)

#congelar los paquetes de python en un archivo
conda list --explicit > requirements.txt

#crear entorno conda en base a los paquetes congelados 
conda create --name mi_entorno --file paquetes.txt

