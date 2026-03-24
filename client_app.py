from mcp import MCPClient

client = MCPClient("http://localhost:5000")

# Leer documento usando la herramienta
doc_text = client.call_tool("read_document", {"file_path": "documents/example_doc.pdf"})
# Resumir documento usando prompt
summary = client.call_prompt("summarize_prompt", {"document_text": doc_text})

print("Resumen del documento:")
print(summary)
