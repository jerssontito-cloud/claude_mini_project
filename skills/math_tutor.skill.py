from mcp import prompt, tool

@prompt
def math_tutor(question: str) -> str:
    return f"Actúa como tutor. Da pistas para resolver: {question}"

@tool
def solve_math(question: str) -> str:
    # Solo para ejemplo: devuelve la pregunta como respuesta
    return f"Resolver: {question}"
