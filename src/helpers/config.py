"""Implementa ConfigHelper"""

import os
import yaml

class ConfigHelper():
    """
    Helper para recoger archivos de configuración
    """
    # Almacenará una instancia por tipo de archivo de configuración cargado
    _instances = {}

    def __init__(self):
        raise RuntimeError('Call instance() instead')


    @classmethod
    def instance(cls, file_name:str):
        """Carga el archivo de config dado y devuelve una instancia YAML
        Es singleton, solo lo carga una vez.

        file - nombre del archivo de la carpeta config, sin extensión
        """
        if file_name not in cls._instances:
            file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = file_path + f"/config/{file_name}.yaml"

            with open(file_path, "r", encoding="utf-8") as ymlfile:
                cls._instances[file_name] = yaml.safe_load(ymlfile)

        return cls._instances[file_name]
