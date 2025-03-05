import gradio as gr
import requests


def send_prompt(prompt, loop=False):
    # Send prompt
    params = {"query": prompt, "alert": loop}
    url = f"http://localhost:5432/query"
    response = requests.get(url, params=params)
    return response.text


def gradio_interface(prompt, is_alert):
    if is_alert is None:
        is_alert = "No"
    loop = True if "yes" in is_alert.lower() else False
    try:
        return send_prompt(prompt, loop=loop)
    except Exception as e:
        return f"Could not send prompt. Ensure demo is running. Error: {e}"


# Create Gradio interface
interface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Radio(["Yes", "No"], label="Is this an Alert?"),
    ],
    outputs="text",
    title="ResponderLLM",
    description="Enter a prompt and specify if it's an alert.",
)

# Launch the interface
interface.launch()
