import gradio as gr
from utils.chatbot import ChatBot

def enviar_mensaje(mensaje, temperatura, historial_chat):
    historial_chat.append((mensaje, ""))
    historial_actualizado = ChatBot.responder(historial_chat[:-1], mensaje, temperatura)
    historial_chat[-1] = (mensaje, historial_actualizado[-1][1])
    return "", historial_chat

def cambiar_placeholder_a_cargando():
    return gr.update(placeholder="⏳ Cargando...")

def restaurar_placeholder():
    return gr.update(placeholder="Escribe algo...")

def borrar_chat():
    return []

with gr.Blocks(theme='gstaff/xkcd') as demo:
    with gr.Row():
        gr.Markdown(f"<h1 style='text-align: center;'>Chatbot Demo</h1>")

    with gr.Row():
        chatbot = gr.Chatbot(
            [],
            label="Chatbot",
            height=800,
            avatar_images=("imagenes/usuario.png", "imagenes/openai.png"),
            placeholder="Escribe algo...",
            elem_id="chatbot"
        )
    
    with gr.Row():
        with gr.Column(scale=9):
            caja_texto = gr.Textbox(label="Escribe tu mensaje aquí", placeholder="Escribe aquí...", elem_id="caja-texto")
        with gr.Column(scale=3):
            boton_enviar = gr.Button("Enviar")
    
    with gr.Row():
        with gr.Column(scale=9):
            deslizador_temperatura = gr.Slider(
                minimum=0, maximum=1, value=0, step=0.01,
                label="Temperatura"
            )
        with gr.Column(scale=3):
            boton_borrar = gr.Button("Borrar chat")
    
    boton_enviar.click(
        cambiar_placeholder_a_cargando,
        inputs=None,
        outputs=[chatbot]
    ).then(
        enviar_mensaje,
        inputs=[caja_texto, deslizador_temperatura, chatbot],
        outputs=[caja_texto, chatbot]
    ).then(
        restaurar_placeholder,
        inputs=None,
        outputs=[chatbot]
    )
    
    boton_borrar.click(
        borrar_chat,
        inputs=[],
        outputs=chatbot
    )

if __name__ == "__main__":
    demo.launch()
