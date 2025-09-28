import gradio as gr
import joblib

# Load your model
model = joblib.load("breast_cancer_model.pkl")

def predict(features):
    prediction = model.predict([features])
    return "Cancer" if prediction[0] == 1 else "No Cancer"

# Define the interface
demo = gr.Interface(
    fn=predict,
    inputs=[gr.inputs.Textbox(label="Enter features as comma-separated values")],
    outputs="text",
)

demo.launch()

