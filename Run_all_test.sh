#!/bin/bash

echo "Ejecutando tests Acciones"
python3 -m unittest "tests/test_Acciones.py"
echo "Ejecutando tests ListasAcciones"
python3 -m unittest "tests/test_ListasAcciones.py"
echo "Ejecutando tests Ficheros"
python3 -m unittest "tests/test_Ficheros.py"
echo "Ejecutando tests Llamadas al sistema"
python3 -m unittest "tests/test_LlamadasSistema.py"
echo "Ejecutando tests LectorMercado"
python3 -m unittest "tests/test_lectorMercado.py"
