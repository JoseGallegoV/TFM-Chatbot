import openai
import re
import html
from langchain_community.vectorstores import Chroma
from typing import List
from utils.cargar_configuracion import CargarConfiguracion

Chatbot_app = CargarConfiguracion()

client = openai.OpenAI(api_key=Chatbot_app.api_key)

class ChatBot:
    """
    Clase que representa un chatbot con capacidades de recuperación de documentos y generación de respuestas.
    """

    @staticmethod
    def responder(chatbot: List, mensaje: str, temperatura: float = 0.0) -> List:
        vectordb = Chroma(
            persist_directory=Chatbot_app.directorio_database,
            embedding_function=Chatbot_app.modelo_embedding
        )

        # Realizar la búsqueda por similitud en la base de datos de vectores
        docs = vectordb.similarity_search(mensaje, k=Chatbot_app.k)
        
        # Limpiar el contenido de los documentos recuperados
        contenido_docs_recuperados = ChatBot.limpiar_referencias(docs)

        chat_history = str(chatbot[-Chatbot_app.numero_pares_pregunta_respuesta:])

        
        prompt = (
            f"# Historial de chat:\n{chat_history}\n\n"
            f"# Numero de contenido recuperado:\n{len(docs)}\n\n"
            f"{contenido_docs_recuperados}\n\n"
            f"# Nueva pregunta del usuario:\n{mensaje}"
        )
        print(prompt)

        # Llamar a la API de OpenAI y manejar posibles errores
        try:
            respuesta = client.chat.completions.create(
                model=Chatbot_app.motor_llm,
                messages=[
                    {"role": "system", "content": Chatbot_app.rol_sistema_llm},
                    {"role": "user", "content": prompt}
                ],
            temperature=temperatura
            )
            # Añadir solo la respuesta del modelo al historial
            chatbot.append((mensaje, respuesta.choices[0].message.content))
        except openai.error.OpenAIError as e:
            print(f"Error al interactuar con la API de OpenAI: {e}")
            chatbot.append((mensaje, "Lo siento, hubo un error al procesar tu solicitud. Por favor, intenta nuevamente."))
            
        return chatbot


    @staticmethod
    def limpiar_referencias(docs: List) -> str:

        docs_recuperados = ""

        for doc in docs:
            # Extraer contenido y metadatos
            content = doc.page_content
            source = doc.metadata.get('source', 'Fuente desconocida')

            content = bytes(content, "utf-8").decode("unicode_escape")

            content = re.sub(r'\\n', '\n', content)
            content = re.sub(r'\s*<EOS>\s*<pad>\s*', ' ', content)
            content = re.sub(r'\s+', ' ', content).strip()

            content = html.unescape(content)

            content = content.encode('latin1').decode('utf-8', 'ignore')

            content = re.sub(r'á', 'a', content)
            content = re.sub(r'é', 'e', content)
            content = re.sub(r'í', 'i', content)
            content = re.sub(r'ó', 'o', content)
            content = re.sub(r'ú', 'u', content)
            content = re.sub(r'ñ', 'n', content)
            content = re.sub(r'Á', 'A', content)
            content = re.sub(r'É', 'E', content)
            content = re.sub(r'Í', 'I', content)
            content = re.sub(r'Ó', 'O', content)
            content = re.sub(r'Ú', 'U', content)
            content = re.sub(r'Ñ', 'N', content)

            docs_recuperados += content + "\n\n" + \
                f"Fuente: {source}" + "\n\n"

        return docs_recuperados