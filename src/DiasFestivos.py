# -*- coding: utf-8 -*-

"""
DiasFestivos.py

Copyright (c) 2025 David Bueno Vallejo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---
Código generado con la ayuda de Microsoft Copilot.
Repositorio preparado con la ayuda de Gemini.
"""

from holidays_es import Province, HolidaySpain
import csv
import os
import argparse
import sys
from datetime import datetime

def main():
    # --- Manejo de argumentos ---
    parser = argparse.ArgumentParser(description="Genera un archivo CSV con los días festivos de las provincias de España para un año determinado.")
    parser.add_argument("--year", type=int, default=datetime.now().year,
                        help="El año para el que se generarán los festivos. Por defecto, el año actual.")
    args = parser.parse_args()
    año = args.year
    current_year = datetime.now().year
    # --------------------------

    # --- Mensajes de interfaz ---
    if '--year' in sys.argv:
        print(f"Generando fichero para el año {año}.")
    elif '--help' not in sys.argv: # No mostrar el mensaje si se pide la ayuda
        print(f"Generando fichero para el año {año}. Para otro año, use: python src/DiasFestivos.py --year <AÑO>")
    # --------------------------

    # --- Validación del año ---
    if año > current_year:
        print(f"Error: Solo se permite generar la información para el año actual ({current_year}) o anteriores.")
        return
    # --------------------------

    # Directorio de salida relativo a la ubicación del script
    output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(output_dir, exist_ok=True)

    # Nombre del archivo de salida
    output_file = os.path.join(output_dir, f"festivos_provincias_{año}.csv")

    # Crear archivo CSV
    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Provincia", "Fecha", "Descripción", "Ámbito"])

            for provincia in Province:
                festivos = HolidaySpain(province=provincia, year=año).holidays
                for festivo in festivos:
                    fecha = festivo.date.strftime("%d/%m/%Y")
                    writer.writerow([provincia.name, fecha, festivo.description, festivo.scope.value])

        print(f"Archivo CSV '{output_file}' creado con éxito.")
    except Exception as e:
        print(f"Error al generar el archivo CSV: {e}")

if __name__ == "__main__":
    main()
