#!/bin/bash

# Función para instalar Python si no está instalado
install_python_if_not_installed() {
    if ! command -v python3 &>/dev/null; then
        echo "Python no está instalado. Instalando Python..."
        sudo apt update
        sudo apt install -y python3
        if [ $? -eq 0 ]; then
            echo "Python instalado correctamente."
        else
            echo "Error al instalar Python."
            exit 1
        fi
    else
        echo "Python ya está instalado."
    fi
}

# Verificar si el usuario es superusuario
check_superuser() {
    if [ "$EUID" -ne 0 ]; then
        echo "Este script requiere permisos de superusuario."
        echo "Por favor, ingresa la contraseña de superusuario cuando se te solicite."
        sudo -E bash -c "$(declare -f install_python_if_not_installed); install_python_if_not_installed"
    else
        install_python_if_not_installed
    fi
}

# Lista de bibliotecas a instalar
#//////////////////////////
#       IMPORTANTE
#//////////////////////////
libraries_to_install=("python-telegram-bot" "yfinance" "os" "subprocess")

# Función para instalar bibliotecas
install_libraries() {
    for lib in "${libraries_to_install[@]}"; do
        sudo apt install -y "$lib"
        if [ $? -eq 0 ]; then
            echo "$lib instalada correctamente."
        else
            echo "Error al instalar $lib."
        fi
    done
}

# Verificar si el usuario es superusuario y/o instalar Python
check_superuser

# Instalar las bibliotecas
install_libraries
