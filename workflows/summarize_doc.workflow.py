"""
Workflow: Leer y resumir un documento
Combina múltiples herramientas para crear un flujo de trabajo automatizado
"""

def summarize_workflow(client, doc_id: str) -> dict:
    """
    Workflow completo para resumir documentos
    
    Pasos:
    1. Obtener la ruta del documento desde el recurso
    2. Leer el contenido del documento
    3. Generar un prompt de resumen
    4. Retornar resultados
    """
    print(f"🔄 Iniciando workflow para documento: {doc_id}")
    
    # Paso 1: Obtener ruta del documento
    file_path = client.get_resource(doc_id)
    print(f"📁 Ruta del documento: {file_path}")
    
    # Paso 2: Leer contenido
    content = client.call_tool("read_document", {"file_path": file_path})
    print(f"📄 Contenido leído: {len(content)} caracteres")
    
    # Paso 3: Generar prompt de resumen
    prompt = client.call_prompt("summarize_prompt", {"document_text": content})
    print(f"📝 Prompt generado: {prompt[:100]}...")
    
    return {
        "doc_id": doc_id,
        "file_path": file_path,
        "content_length": len(content),
        "summary_prompt": prompt
    }

if __name__ == "__main__":
    # Ejemplo de uso
    print("🚀 Workflow: Resumir Documento")
    print("=" * 50)
    
    # Simular cliente (en producción usarías el cliente MCP real)
    class MockClient:
        def get_resource(self, doc_id):
            return "documents/example_doc.txt"
        
        def call_tool(self, tool_name, args):
            return "Contenido de ejemplo del documento..."
        
        def call_prompt(self, prompt_name, args):
            return "Resume este documento de manera clara y breve..."
    
    client = MockClient()
    result = summarize_workflow(client, "example_doc")
    
    print("\n✅ Resultados del workflow:")
    print(result)
