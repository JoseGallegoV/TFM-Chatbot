# Chatbot para Extracción de Información de PDFs

Este proyecto de Trabajo de Fin de Máster (TFM) desarrolla un chatbot inteligente que utiliza LangChain y GPT para extraer información de documentos PDF, proporcionando una interfaz de usuario intuitiva con Gradio.

## Descripción

El objetivo de este proyecto es crear una herramienta que facilite la extracción y utilización de información contenida en documentos PDF. El sistema se basa en tecnologías avanzadas de procesamiento de lenguaje natural (NLP) y machine learning, utilizando LangChain y GPT para la generación de respuestas precisas y relevantes. La interfaz de usuario se ha desarrollado con Gradio, permitiendo una interacción sencilla y directa.

## Tecnologías Utilizadas

**LangChain:** Herramienta para la gestión de cadenas de procesamiento de lenguaje natural.

**GPT (Generative Pre-trained Transformer):** Modelo de lenguaje avanzado desarrollado por OpenAI.

**Gradio:** Plataforma para la creación de interfaces de usuario interactivas.

**ChromaDB:** Base de datos vectorial para el almacenamiento y recuperación eficiente de información.

## Funcionalidades

**Lectura y Procesamiento de PDFs:** Un script que lee y procesa documentos PDF, separando su contenido en bloques de texto manejables.

**Generación de Respuestas:** Integración de LangChain y GPT para generar respuestas basadas en el contenido de los PDFs.

**Interfaz de Usuario:** Desarrollo de una interfaz interactiva con Gradio para formular preguntas y recibir respuestas en tiempo real.

**Control de Creatividad:** Ajuste de la temperatura del modelo para controlar el nivel de creatividad de las respuestas generadas.

## Instalación y Uso

### Requisitos

Asegúrate de tener instalados los siguientes requisitos previos:

- Python 3.10.12
- pip (Python package installer)
- Git (para clonar el repositorio, opcional)

### Clonación del repositorio

Primero, clona este repositorio en tu máquina local (opcional si ya descargaste el código):

```
git clone https://github.com/JoseGallegoV/TFM-Chatbot.git
cd TFM-Chatbot
```

### Creación de entorno virtual

Se recomienda crear un entorno virtual para aislar las dependencias del proyecto. Si no tienes instalado venv, puedes hacerlo con:

```
pip install virtualenv
```

A continuación, puedes crear un entorno virtual con los siguientes comandos:

```
python -m venv [nombre del entorno]
source [nombre del entorno]/bin/activate  # En Windows usa `[nombre del entorno]\Scripts\activate`
```

### Instalación de dependencias

Instala las dependencias necesarias usando `pip`:

```
pip install -r requirements.txt
```

### Configuración de la clave de API de OpenAI

Antes de utilizar la aplicación, necesitas crear un archivo .env en el directorio raíz del proyecto y añadir tu clave de API de OpenAI. Crea el archivo .env con el siguiente contenido:

```
OPENAI_API_KEY="tu_clave_de_openai_aqui"
```

### Preparación de datos

Antes de ejecutar la aplicación, debes preparar los datos. Coloca tus archivos PDF en el directorio `data/docs`. Puedes utilizar los archivos PDF de prueba incluidos o reemplazarlos por cualquier PDF en español.

Ejecuta el script `subir_data_chroma.py` para crear la base de datos ChromaDB:

```
python src/subir_data_chroma.py
```

### Ejecución de la aplicación

Una vez que la base de datos ChromaDB esté creada, puedes ejecutar la aplicación:

```
python src/app.py
```

Luego, abre tu navegador web y navega a `http://127.0.0.1:7860` para usar el chatbot.
