from mcp import MCPServer, tool, prompt, resource

server = MCPServer()

# Herramienta para leer documentos
@tool
def read_document(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Prompt para resumir documentos
@prompt
def summarize_prompt(document_text: str) -> str:
    return f"Resume este documento de manera clara y breve:\n{document_text}"

# Recurso para documentos
@resource
def documents(doc_id: str):
    file_map = {
        "example_doc": "documents/example_doc.pdf"
    }
    return file_map.get(doc_id, "")

server.start(port=5000)
