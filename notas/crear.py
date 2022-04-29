#!/usr/bin/python3

# author: Jakepy

import os


def crear_archivo():
    try:
        archivo = str(input("[+] Ingrese el nombre del archivo[archivo.md]: "))
        assert len(archivo) < 0, "Ingrese algo"
        if archivo != "":
            os.system(f"touch {archivo}.md")
            print("[!] Archivo creado...")
        else:
            print("[!!] NO ingreso nada")
            exit()
    except KeyboardInterrupt:
        print("\n[!]Saliendo...")
        exit()


def main():
    crear_archivo()


if __name__ == '__main__':
    main() 
