# Chatbot para Extracción de Información de PDFs

Este proyecto de Trabajo de Fin de Máster (TFM) desarrolla un chatbot inteligente que utiliza LangChain y GPT para extraer información de documentos PDF, proporcionando una interfaz de usuario intuitiva con Gradio.

## Descripción

El objetivo de este proyecto es crear una herramienta que facilite la extracción y utilización de información contenida en documentos PDF. El sistema se basa en tecnologías avanzadas de procesamiento de lenguaje natural (NLP) y machine learning, utilizando LangChain y GPT para la generación de respuestas precisas y relevantes. La interfaz de usuario se ha desarrollado con Gradio, permitiendo una interacción sencilla y directa.

## Tecnologías Utilizadas

LangChain: Herramienta para la gestión de cadenas de procesamiento de lenguaje natural.

GPT (Generative Pre-trained Transformer): Modelo de lenguaje avanzado desarrollado por OpenAI.

Gradio: Plataforma para la creación de interfaces de usuario interactivas.

ChromaDB: Base de datos vectorial para el almacenamiento y recuperación eficiente de información.

## Funcionalidades

    Lectura y Procesamiento de PDFs: Un script que lee y procesa documentos PDF, separando su contenido en bloques de texto manejables.
    Generación de Respuestas: Integración de LangChain y GPT para generar respuestas basadas en el contenido de los PDFs.
    Interfaz de Usuario: Desarrollo de una interfaz interactiva con Gradio para formular preguntas y recibir respuestas en tiempo real.
    Control de Creatividad: Ajuste de la temperatura del modelo para controlar el nivel de creatividad de las respuestas generadas.

Instalación

    Clona este repositorio:

    bash

git clone https://github.com/tu_usuario/chatbot-pdf.git

Navega al directorio del proyecto:

bash

cd chatbot-pdf

Instala las dependencias:

bash

    pip install -r requirements.txt

Uso

    Ejecuta el script principal:

    bash

python app.py

Abre el navegador y accede a la interfaz en http://localhost:7860.
