import random
import gradio as gr
import base64

def random_response(message, history):
    bot_response = random.choice(["Yes", "No"])
    
    audio_file = "gradio/talking_benn_yes.mp3" if bot_response == "Yes" else "gradio/talking_benn_no.mp3"
    
    # Ses dosyasını base64'e çevir ve HTML'e göm
    with open(audio_file, "rb") as f:
        audio_base64 = base64.b64encode(f.read()).decode()
    
    # Görünmez audio tag
    audio_html = f'<audio autoplay style="display:none"><source src="data:audio/mpeg;base64,{audio_base64}"></audio>'
    
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": bot_response + audio_html})
    
    return history

with gr.Blocks() as demo:
    gr.HTML("<h1 style='text-align: center;'>Talking Ben Chatbot</h1>")
    chatbot = gr.Chatbot(
        type="messages", 
        avatar_images=(None, "gradio/talking_benn.png")
    )
    msg = gr.Textbox(autofocus=False, placeholder="Bir şey yazın...")
    
    msg.submit(random_response, [msg, chatbot], [chatbot])

demo.launch()