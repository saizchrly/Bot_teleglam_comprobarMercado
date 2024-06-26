#!/bin/bash

# Ejecutar todos los tests que coincidan con el patrón test_*.py
echo "Ejecutando tests Acciones"
python3 -m unittest "tests/test_Acciones.py"
echo "Ejecutando tests ListasAcciones"
python3 -m unittest "tests/test_ListasAcciones.py"
