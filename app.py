from flask import Flask, jsonify
import google.generativeai as genai
import os

# Configura tu clave de Gemini con variable de entorno
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

@app.route("/contenido/<tipo>")
def contenido(tipo):
    prompts = {
        "chiste": "Cuéntame un chiste corto para una pantalla pequeña.",
        "receta": "Dame una receta sencilla en 2 líneas.",
        "dato": "Dime un dato curioso en una sola frase.",
    }
    prompt = prompts.get(tipo.lower(), "Dime algo breve y curioso.")
    try:
        response = model.generate_content(prompt)
        return jsonify({"respuesta": response.text.strip()})
    except Exception as e:
        return jsonify({"respuesta": f"Error: {e}"})
