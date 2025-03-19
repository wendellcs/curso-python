import gradio as gr 
import math

def factorial(num):
    if num < 0:
        return 'Factorial not defined for negative numbers'
    
    return math.factorial(num)

iface = gr.Interface(
    fn = factorial,
    inputs = 'number',
    outputs = 'text',
    title = 'Factorial Calculator',
    description = 'Returns the factorial of a given number',
    theme = 'default'
)

iface.launch()