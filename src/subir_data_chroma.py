import os
from utils.preparacion_vectordb import PrepararVectorDB
from utils.cargar_configuracion import CargarConfiguracion

CONFIG = CargarConfiguracion()

def subir_datos_manualmente() -> None:
    os.makedirs(CONFIG.directorio_database, exist_ok=True)
    
    instancia_preparar_vectordb = PrepararVectorDB(
        directorio_datos=CONFIG.directorio_datos,
        directorio_database=CONFIG.directorio_database,
        motor_modelo_embedding=CONFIG.motor_modelo_embedding,
        tamaño_fragmento=CONFIG.tamaño_fragmento,
        solapamiento_fragmento=CONFIG.solapamiento_fragmento,
    )
    
    if not len(os.listdir(CONFIG.directorio_database)) != 0:
        instancia_preparar_vectordb.preparar_y_guardar_vectordb()
    else:
        print(f"VectorDB ya existe en {CONFIG.directorio_database}")
    return None

if __name__ == "__main__":
    subir_datos_manualmente()

