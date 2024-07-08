from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from typing import List
from langchain_openai import OpenAIEmbeddings

class PrepararVectorDB:

    def __init__(
            self,
            directorio_datos: str,
            directorio_database: str,
            motor_modelo_embedding: str,
            tamaño_fragmento: int,
            solapamiento_fragmento: int
    ) -> None:

        self.motor_modelo_embedding = motor_modelo_embedding
        self.divisor_texto = RecursiveCharacterTextSplitter(
            chunk_size=tamaño_fragmento,
            chunk_overlap=solapamiento_fragmento,
            separators=["\n\n", "\n", " ", ""]
        )
        self.directorio_datos = directorio_datos
        self.directorio_database = directorio_database
        self.embedding = OpenAIEmbeddings()

    def __cargar_todos_los_documentos(self) -> List:

        contador_documentos = 0
        if isinstance(self.directorio_datos, list):
            print("Cargando los documentos subidos...")
            documentos = []
            for directorio_doc in self.directorio_datos:
                documentos.extend(PyPDFLoader(directorio_doc).load())
                contador_documentos += 1
            print("Número de documentos cargados:", contador_documentos)
            print("Número de páginas:", len(documentos), "\n\n")
        else:
            print("Cargando documentos manualmente...")
            lista_documentos = os.listdir(self.directorio_datos)
            documentos = []
            for nombre_doc in lista_documentos:
                documentos.extend(PyPDFLoader(os.path.join(
                    self.directorio_datos, nombre_doc)).load())
                contador_documentos += 1
            print("Número de documentos cargados:", contador_documentos)
            print("Número de páginas:", len(documentos), "\n\n")

        return documentos

    def __dividir_documentos(self, documentos: List) -> List:
    
        print("Dividiendo documentos...")
        documentos_divididos = self.divisor_texto.split_documents(documentos)
        print("Número de fragmentos:", len(documentos_divididos), "\n\n")
        return documentos_divididos

    def preparar_y_guardar_vectordb(self):

        documentos = self.__cargar_todos_los_documentos()
        documentos_divididos = self.__dividir_documentos(documentos)
        print("Preparando vectordb...")
        vectordb = Chroma.from_documents(
            documents=documentos_divididos,
            embedding=self.embedding,
            persist_directory=self.directorio_database
        )
        print("VectorDB creado y guardado.")
        print("Número de vectores en vectordb:",
            vectordb._collection.count(), "\n\n")
        return vectordb
