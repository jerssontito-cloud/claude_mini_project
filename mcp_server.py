from mcp.server import Server
import asyncio

# Crear servidor
server = Server("claude-mini-project")

# Herramienta para leer documentos
@server.tool()
def read_document(file_path: str) -> str:
    """Lee el contenido de un archivo de texto"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: Archivo no encontrado - {file_path}"

# Herramienta para sumar números (ejemplo simple)
@server.tool()
def add_numbers(a: int, b: int) -> int:
    """Suma dos números"""
    return a + b

# Prompt para resumir documentos
@server.prompt()
def summarize_prompt(document_text: str) -> str:
    """Genera un prompt para resumir un documento"""
    return f"Resume este documento de manera clara y breve:\n\n{document_text}"

# Prompt para tutor de matemáticas
@server.prompt()
def math_tutor_prompt(question: str) -> str:
    """Genera un prompt para actuar como tutor de matemáticas"""
    return f"Actúa como un tutor de matemáticas. Ayuda al estudiante a resolver: {question}. Da pistas, no la respuesta directa."

# Recurso para documentos
@server.resource()
def documents(doc_id: str) -> str:
    """Proporciona acceso a documentos por ID"""
    file_map = {
        "example_doc": "documents/example_doc.txt",
        "readme": "README.md"
    }
    return file_map.get(doc_id, "")

# Iniciar servidor
if __name__ == "__main__":
    print("🚀 MCP Server iniciado en puerto 5000")
    print("📦 Herramientas disponibles: read_document, add_numbers")
    print("📝 Prompts disponibles: summarize_prompt, math_tutor_prompt")
    print("📁 Recursos disponibles: documents")
    print("\nPresiona Ctrl+C para detener el servidor\n")
    
    # Mantener el servidor corriendo
    try:
        while True:
            asyncio.run(asyncio.sleep(1))
    except KeyboardInterrupt:
        print("\n✅ Servidor detenido correctamente")
