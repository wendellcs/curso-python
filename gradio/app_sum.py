import gradio as gr

def sum(a , b):
    return a + b

iface = gr.Interface(
    fn = sum,
    inputs = ['number', 'number'],
    outputs = 'number',
    title = 'Sum Calculator',
    description = 'Sum two numbers',
    theme = 'default'
)

iface.launch()