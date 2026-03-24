import requests
import json

# Configuración del cliente
SERVER_URL = "http://localhost:5000"

def call_tool(tool_name: str, arguments: dict) -> any:
    """Llama a una herramienta del servidor MCP"""
    try:
        response = requests.post(
            f"{SERVER_URL}/tools/{tool_name}",
            json=arguments,
            timeout=10
        )
        return response.json()
    except Exception as e:
        return f"Error: {str(e)}"

def call_prompt(prompt_name: str, arguments: dict) -> str:
    """Llama a un prompt del servidor MCP"""
    try:
        response = requests.post(
            f"{SERVER_URL}/prompts/{prompt_name}",
            json=arguments,
            timeout=10
        )
        return response.json().get("result", "")
    except Exception as e:
        return f"Error: {str(e)}"

def get_resource(resource_id: str) -> str:
    """Obtiene un recurso del servidor MCP"""
    try:
        response = requests.get(
            f"{SERVER_URL}/resources/{resource_id}",
            timeout=10
        )
        return response.json().get("content", "")
    except Exception as e:
        return f"Error: {str(e)}"

# === PRUEBAS ===
if __name__ == "__main__":
    print("🔌 Conectando al servidor MCP...\n")
    
    # Prueba 1: Leer documento
    print("📄 Prueba 1: Leer documento")
    doc = call_tool("read_document", {"file_path": "documents/example_doc.txt"})
    print(f"Contenido: {doc}\n")
    
    # Prueba 2: Sumar números
    print("🔢 Prueba 2: Sumar números")
    result = call_tool("add_numbers", {"a": 5, "b": 3})
    print(f"5 + 3 = {result}\n")
    
    # Prueba 3: Prompt de resumen
    print("📝 Prueba 3: Prompt de resumen")
    prompt = call_prompt("summarize_prompt", {"document_text": "Este es un documento de prueba."})
    print(f"Prompt generado: {prompt}\n")
    
    # Prueba 4: Prompt de matemáticas
    print("🧮 Prueba 4: Prompt de matemáticas")
    math_prompt = call_prompt("math_tutor_prompt", {"question": "2x + 3 = 7"})
    print(f"Prompt generado: {math_prompt}\n")
    
    print("✅ Todas las pruebas completadas!")
