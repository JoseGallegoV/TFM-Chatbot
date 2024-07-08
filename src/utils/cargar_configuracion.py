import openai
import os
from dotenv import load_dotenv
import yaml
from langchain_openai import OpenAIEmbeddings
import shutil

load_dotenv()

class CargarConfiguracion:

    def __init__(self) -> None:
        ruta_config="configs/app_config.yml"
        with open(ruta_config) as cfg:
            app_config = yaml.load(cfg, Loader=yaml.FullLoader)

        ruta_config_absoluta=os.path.abspath(ruta_config)
        directorio_base = os.path.dirname(os.path.dirname(ruta_config_absoluta))

        # Configuraciones LLM
        self.motor_llm = app_config["configuracion_llm"]["motor"]
        self.rol_sistema_llm = app_config["configuracion_llm"]["rol_sistema_llm"]
        self.directorio_database = os.path.join(directorio_base, app_config["directorios"]["directorio_database"])
        self.modelo_embedding = OpenAIEmbeddings()

        # Configuraciones de recuperación
        self.directorio_datos = app_config["directorios"]["directorio_datos"]
        self.k = app_config["configuracion_recuperacion"]["k"]
        self.motor_modelo_embedding = app_config["configuracion_modelo_embedding"]["motor"]
        self.tamaño_fragmento = app_config["configuracion_splitter"]["tamaño_fragmento"]
        self.solapamiento_fragmento = app_config["configuracion_splitter"]["solapamiento_fragmento"]

        # Memoria
        self.numero_pares_pregunta_respuesta = app_config["memoria"]["numero_de_pares_pregunta_respuesta"]

        # Cargar credenciales de OpenAI
        self.cargar_cfg_openai()

    def cargar_cfg_openai(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def crear_directorio(self, ruta_directorio: str):
        if not os.path.exists(ruta_directorio):
            os.makedirs(ruta_directorio)