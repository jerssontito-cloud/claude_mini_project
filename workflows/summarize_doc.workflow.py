# Workflow simple: leer + resumir
def summarize_workflow(client, doc_id):
    file_path = client.call_resource("documents", {"doc_id": doc_id})
    text = client.call_tool("read_document", {"file_path": file_path})
    summary = client.call_prompt("summarize_prompt", {"document_text": text})
    return summary
