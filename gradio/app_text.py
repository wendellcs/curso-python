import gradio as gr 

def reverse_text(txt):
    reversed_text = txt[::-1]
    return reversed_text, len(reversed_text)

iface = gr.Interface(
    fn = reverse_text,
    inputs = 'text',
    outputs = ['text', 'number'],
    title = 'Text Reverser',
    description = 'Reverse the text and return its lenght',
    theme = 'default'
)

iface.launch()